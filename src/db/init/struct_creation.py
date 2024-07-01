import sqlite3

from src.base.path import DB_PATH, SQL_SRC_PATH


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(SQL_SRC_PATH, "r", encoding="utf8") as sql_file:
        sql_script = sql_file.read()

    cursor.executescript(sql_script)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
