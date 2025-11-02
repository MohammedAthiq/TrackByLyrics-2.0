from app import app, db
from sqlalchemy import text

print("Connecting to Neon database...")

try:
    with app.app_context():
        with db.engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            print("✅ Connected successfully!")
            print(result.fetchone())
except Exception as e:
    print("❌ Connection failed:", e)