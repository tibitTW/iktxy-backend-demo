import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../../data/database.db")
SQL_SRC_PATH = os.path.join(BASE_DIR, "../../specs/db/struct.sql")
