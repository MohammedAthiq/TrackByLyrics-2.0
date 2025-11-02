from app import app, db

print("Creating tables in Neon...")

with app.app_context():
    db.create_all()
    print("✅ Tables created successfully in Neon!")