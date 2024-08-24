from src.base.constants.path import (
    CSV_INJECTION_DIR_PATH,
    DB_PATH,
    SQL_SRC_PATH,
)
from src.dbapi.sqlite3.main import SQLiteDB


def main():
    print(DB_PATH)
    db = SQLiteDB(db_path=DB_PATH)

    # clear old database
    db.clear()
    db.connect()

    # create database structure with existing .sql file
    db.load_sql(sql_filepath=SQL_SRC_PATH)

    # insert sample data
    tables = ["users", "programs", "holly_houses", "participate_records"]
    for table in tables:
        db.insert_csv_data(
            csv_path=f"{CSV_INJECTION_DIR_PATH}/{table}.csv",
            table_name=table,
        )

        # get data
        users_table = db.get_query(table_name=table)
        print(f"{table=}")
        print(users_table, end="\n\n")

    db.disconnect()


if __name__ == "__main__":
    main()
