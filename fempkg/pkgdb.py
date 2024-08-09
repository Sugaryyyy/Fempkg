"""
 Fempkg's database managment library.
"""

import sqlite3
from pathlib import Path


class packageDB:

    def __init__(self):
        self.db_path = Path(".")  # Package database location file

    def initDB(self):
        con = sqlite3.connect(self.db_path / "packages.db")
        cur = con.cursor()

        cur.execute(
            "CREATE TABLE IF NOT EXISTS packages(id INT PRIMARY KEY, name VARCHAR, repo VARCHAR, version VARCHAR, description VARCHAR, install_type VARCHAR, critical BOOL, date INT)"
        )

        cur.execute(
            "CREATE TABLE IF NOT EXISTS files(id INT PRIMARY KEY, belongs_to INT, path VARCHAR, chksum VARCHAR)"
        )
        cur.execute(
            "CREATE TABLE IF NOT EXISTS dependency(id INT PRIMARY KEY, parent VARCHAR, child VARCHAR)"
        )

    def loadDB(self):
        con = sqlite3.connect(self.db_path / "packages.db")
        cur = con.cursor()
        return cur

if __name__ == "__main__":
    packageDB = packageDB()
    packageDB.initDB()
