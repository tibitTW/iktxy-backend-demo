import csv
import sqlite3


class SQLiteDB(object):
    _db_path: str
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(
        self,
        db_path: str,
    ) -> None:
        self._db_path = db_path
        self._connect()

    def _connect(self) -> None:
        self.conn = sqlite3.connect(self._db_path)
        self.cursor = self.conn.cursor()

    def load_sql(self, sql_filepath: str) -> None:
        with open(sql_filepath, "r", encoding="utf8") as sql_file:
            sql_script = sql_file.read()

        self.cursor.executescript(sql_script)

    def inject_data_from_csv(self, csv_path: str, table_name: str):
        with open(csv_path, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            headers = next(csv_reader)
            placeholders = ", ".join(["?"] * len(headers))

            sql_insert = f'INSERT INTO {table_name} ({", ".join(headers)}) \
                VALUES ({placeholders})'

            for row in csv_reader:
                self.cursor.execute(sql_insert, row)
