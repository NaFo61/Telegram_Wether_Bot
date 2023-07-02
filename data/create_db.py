import sqlite3


def create_customer_table():
    with sqlite3.connect('data/database.db') as connect:
        cursor = connect.cursor()

        sql = """
        CREATE TABLE IF not exists users(
            id         INTEGER PRIMARY KEY AUTOINCREMENT
                               UNIQUE,
            users_id   INTEGER UNIQUE
                               NOT NULL,
            users_name STRING  DEFAULT NULL,
            users_spin INTEGER DEFAULT (1) 
                               NOT NULL
        );
        """

        cursor.execute(sql)
        connect.commit()