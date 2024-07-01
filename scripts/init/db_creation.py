from src.base.constants.path import (
    CSV_INJECTION_DIR_PATH,
    DB_PATH,
    SQL_SRC_PATH,
)
from src.db.sqlite3.main import SQLiteDB


def main() -> None:
    print(DB_PATH)
    db = SQLiteDB(db_path=DB_PATH)

    # create database structure with existing .sql file
    db.load_sql(sql_filepath=SQL_SRC_PATH)

    # sample data injection
    db.inject_csv_data(
        csv_path=f"{CSV_INJECTION_DIR_PATH}/users.csv",
        table_name="users",
    )

    users_table = db.get_table_in_df(table_name="users")
    print(users_table)

    db.disconnect()


if __name__ == "__main__":
    main()
