import csv
import sqlite3

import pandas as pd


class SQLiteDB(object):
    _db_path: str
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(
        self,
        db_path: str,
    ) -> None:
        self._db_path = db_path
        self.connect()

    def connect(self) -> None:
        self.conn = sqlite3.connect(self._db_path)
        self.cursor = self.conn.cursor()

    def disconnect(self) -> None:
        self.conn.commit()
        self.conn.close()

    def load_sql(self, sql_filepath: str) -> None:
        with open(sql_filepath, "r", encoding="utf8") as sql_file:
            sql_script = sql_file.read()

        self.cursor.executescript(sql_script)

    def inject_csv_data(self, csv_path: str, table_name: str):
        with open(csv_path, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            headers = next(csv_reader)
            placeholders = ", ".join(["?"] * len(headers))

            sql_insert = f'INSERT INTO {table_name} ({", ".join(headers)}) \
                VALUES ({placeholders})'

            for row in csv_reader:
                self.cursor.execute(sql_insert, row)

    def get_table_in_df(
        self,
        table_name: str,
        columns: list | None = None,
    ) -> pd.DataFrame:
        if not columns:
            columns_str = "*"
        else:
            columns_str = ",".join(columns)

        query = f"SELECT {columns_str} FROM {table_name}"

        df = pd.read_sql_query(query, self.conn)
        return df

    def get_query(
        self,
        table: str,
        columns: list | None = None,
    ) -> pd.DataFrame:
        return pd.read_sql_query("SELECT * FROM users", self.conn)
