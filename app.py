import os
import sqlite3
from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from utils import search_song

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect("trackbylyrics.db")
    conn.row_factory = sqlite3.Row
    return conn

# ------------------ AUTH ROUTES ------------------ #
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            flash("Email already registered. Try logging in.")
            conn.close()
            return redirect(url_for("login"))

        hashed_pw = generate_password_hash(password)
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                       (username, email, hashed_pw))
        conn.commit()
        conn.close()

        flash("Signup successful! Please log in.")
        return redirect(url_for("login"))

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user"] = user["username"]
            flash("Login successful!")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials. Try again.")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully.")
    return redirect(url_for("login"))

# ------------------ MAIN APP ROUTES ------------------ #
@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", username=session["user"])

@app.route("/api/search", methods=["POST"])
def api_search():
    if "user" not in session:
        return jsonify({"error": "Please log in first."}), 403

    data = request.get_json()
    lyrics = data.get("lyrics", "")
    if not lyrics:
        return jsonify({"error": "Please provide lyrics"}), 400

    result = search_song(lyrics)

    # Store search in DB
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO search_history (user_email, query, result_song) VALUES (?, ?, ?)",
        (session["user"], lyrics, result.get("name"))
    )
    conn.commit()
    conn.close()

    return jsonify(result)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)