from enum import Enum
import os


class BasePaths(Enum):
    """
    Enum for defining base paths within the project structure.
    """

    BASE_DIR = os.path.normpath(
        os.path.join(
            os.path.abspath(__file__),
            "../" * 3,
        )
    )


class DatabasePaths(Enum):
    """
    Enum for defining database paths within the project structure.
    """

    DB_PATH = os.path.join(
        BasePaths.BASE_DIR,
        "data/database.db",
    )
    SQL_SRC_PATH = os.path.join(
        BasePaths.BASE_DIR,
        "specs/sql/struct.sql",
    )
    CSV_INJECTION_DIR_PATH = os.path.join(
        BasePaths.BASE_DIR,
        "specs/csv",
    )
