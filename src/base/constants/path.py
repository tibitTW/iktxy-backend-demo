import os

# project root dir
__current_path = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.normpath(os.path.join(__current_path, "../../../"))
DB_PATH = os.path.join(BASE_DIR, "data/database.db")
SQL_SRC_PATH = os.path.join(BASE_DIR, "specs/sql/struct.sql")
CSV_INJECTION_DIR_PATH = os.path.join(BASE_DIR, "specs/csv")
