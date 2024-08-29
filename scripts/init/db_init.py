from src.base.constants import DatabasePaths as DBPath
from src.db.sqlite3.main import SQLiteDB


def main():
    db = SQLiteDB(db_path=DBPath.DB_PATH)

    # clear old database
    db.clear()
    db.connect()

    # create database structure with existing .sql file
    db.load_sql(sql_filepath=DBPath.SQL_SRC_PATH)

    # insert sample data
    tables = ["users", "programs", "holly_houses", "participate_records"]
    for table in tables:
        db.insert_csv_data(
            csv_path=f"{DBPath.CSV_INJECTION_DIR_PATH}/{table}.csv",
            table_name=table,
        )

        # get data
        users_table = db.get_query(table_name=table)
        print(f"{table=}")
        print(users_table, end="\n\n")

    db.disconnect()


if __name__ == "__main__":
    main()
