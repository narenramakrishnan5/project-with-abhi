import sqlite3


class DatabaseConnectioncursor():
    def __init__(self, db_file):
        self.connection = None
        self.file = db_file
        self.cursor = None

    def __enter__(self) -> sqlite3.Connection.cursor:
        self.connection = sqlite3.connect(self.file)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
