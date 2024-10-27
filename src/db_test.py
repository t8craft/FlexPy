# src/db_test.py

from db import SessionLocal
from sqlalchemy import text  # Import text for raw SQL expressions

def test_connection():
    try:
        # Attempt to create a session and query the database
        session = SessionLocal()
        session.execute(text("SELECT 1"))  # Wrap 'SELECT 1' with text()
        print("Database connection successful!")
    except Exception as e:
        print("Failed to connect to the database.")
        print(f"Error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    test_connection()




# # src/db_test.py

# from db import SessionLocal

# def test_connection():
#     try:
#         # Attempt to create a session and query the database
#         session = SessionLocal()
#         session.execute("SELECT 1")
#         print("Database connection successful!")
#     except Exception as e:
#         print("Failed to connect to the database.")
#         print(f"Error: {e}")
#     finally:
#         session.close()

# if __name__ == "__main__":
#     test_connection()
