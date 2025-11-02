import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from utils import search_song
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
# Initialize Flask app
app = Flask(__name__)

# Load environment variables
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# =========================
# Database Models
# =========================
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class SearchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    lyrics = db.Column(db.String(255), nullable=False)
    song = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


# =========================
# Routes
# =========================
@app.route("/", methods=["GET", "POST"])
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))
    
    result = None
    if request.method == "POST":
        lyrics = request.form["song"]
        result = search_song(lyrics)

        if result and "name" in result:
            # Save search to history
            history = SearchHistory(
                username=session["username"],
                lyrics=lyrics,
                song=result["name"]
            )
            db.session.add(history)
            db.session.commit()

    history_items = SearchHistory.query.filter_by(username=session["username"]).order_by(SearchHistory.timestamp.desc()).limit(5).all()
    return render_template("index.html", result=result, history=history_items)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid credentials.")
    
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        try:
            username = request.form["username"]
            email = request.form["email"]
            password = generate_password_hash(request.form["password"])

            existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
            if existing_user:
                return render_template("login.html", error="User already exists. Please log in.")

            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            session["user_id"] = new_user.id
            session["username"] = username
            print(f"✅ New user created: {username}")
            return redirect(url_for("home"))
        except Exception as e:
            print(f"❌ Signup error: {e}")
            return render_template("login.html", error="An unexpected error occurred.")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# =========================
# Run App
# =========================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensures tables exist in Neon DB
    app.run(host="0.0.0.0", port=5001, debug=True)