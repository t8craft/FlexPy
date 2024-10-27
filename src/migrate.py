import sys
import os

# Add the project root directory (Base_Two) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db import engine, Base
from sqlalchemy import inspect
from Entities import *  # Import all models from Entities/__init__.py
from datetime import datetime

def init_db():
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    new_tables_created = []
    duplicate_attempted = False

    for table in Base.metadata.sorted_tables:
        if table.name not in existing_tables:
            try:
                Base.metadata.create_all(bind=engine, tables=[table])
                new_tables_created.append(table.name)
                print(f"{table.name} has been created on {datetime.now()}")
            except Exception:
                duplicate_attempted = True
                print(f"Error: {table.name} already exists")
        elif duplicate_attempted:
            print(f"Error: {table.name} already exists")

    if not new_tables_created and not duplicate_attempted:
        print("No new tables to transfer.")

if __name__ == "__main__":
    init_db()





# from db import engine, Base
# from Entities import *  # Ensure all models are imported
# from sqlalchemy import inspect
# from datetime import datetime

# def init_db():
#     inspector = inspect(engine)
#     existing_tables = inspector.get_table_names()

#     for table in Base.metadata.sorted_tables:
#         print(f"Found table in metadata: {table.name}")
#         if table.name not in existing_tables:
#             print(f"Creating table: {table.name}")
#             Base.metadata.create_all(bind=engine, tables=[table])
#             print(f"{table.name} has been created on {datetime.now()}")
#         else:
#             print(f"Table already exists: {table.name}")

# if __name__ == "__main__":
#     init_db()



# from db import engine, Base
# from sqlalchemy import inspect
# from Entities import *  # Import all models from Entities/__init__.py
# from datetime import datetime

# def init_db():
#     inspector = inspect(engine)
#     existing_tables = inspector.get_table_names()
#     new_tables_created = []
#     duplicate_attempted = False

#     for table in Base.metadata.sorted_tables:
#         if table.name not in existing_tables:
#             try:
#                 Base.metadata.create_all(bind=engine, tables=[table])
#                 new_tables_created.append(table.name)
#                 print(f"{table.name} has been created on {datetime.now()}")
#             except Exception:
#                 duplicate_attempted = True
#                 print(f"Error: {table.name} already exists")
#         elif duplicate_attempted:
#             print(f"Error: {table.name} already exists")

#     if not new_tables_created and not duplicate_attempted:
#         print("No new tables to transfer.")

# if __name__ == "__main__":
#     init_db()
