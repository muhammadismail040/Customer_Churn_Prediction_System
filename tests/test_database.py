from src.database.database import engine

try:
    connection = engine.connect()

    print("=" * 50)
    print("✅ PostgreSQL Connected Successfully!")
    print("=" * 50)

    connection.close()

except Exception as e:
    print("=" * 50)
    print("❌ Connection Failed")
    print(e)
    print("=" * 50)