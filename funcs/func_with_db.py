import sqlite3


def get_users_name_from_users_id(users_id):
    with sqlite3.connect('data/database.db') as connect:
        cursor = connect.cursor()

        sql = f"""
        SELECT users_name FROM users
        WHERE users_id = "{users_id}"
        """

        users_name = cursor.execute(sql).fetchone()[0]
        return users_name


def get_users_spin_from_users_id(users_id):
    with sqlite3.connect('data/database.db') as connect:
        cursor = connect.cursor()

        sql = f"""
        SELECT users_spin FROM users
        WHERE users_id = "{users_id}"
        """

        users_name = cursor.execute(sql).fetchone()[0]
        return users_name


def check_here_users_id(users_id):
    with sqlite3.connect('data/database.db') as connect:
        cursor = connect.cursor()

        sql = f"""
        SELECT users_id FROM users
        """

        ids = [id[0] for id in cursor.execute(sql).fetchall()]
        return users_id in ids


def put_to_db(users_id, users_name=None, registration=False):
    if registration:
        with sqlite3.connect('data/database.db') as connect:
            cursor = connect.cursor()

            sql = f"""
            UPDATE users
            SET users_name = "{users_name}", users_spin = 1000
            WHERE users_id = "{users_id}"
            """

            cursor.execute(sql)
            connect.commit()
            return 'Успешно'



    else:
        if check_here_users_id(users_id):
            return True
        with sqlite3.connect('data/database.db') as connect:
            cursor = connect.cursor()

            sql = f"""
            INSERT INTO users(users_id)
            VALUES("{users_id}")
            """

            cursor.execute(sql)
            connect.commit()
            return True


def lose_one_spin(users_id):
    count_of_spin = get_users_spin_from_users_id(users_id)
    with sqlite3.connect('data/database.db') as connect:
        cursor = connect.cursor()

        sql = f"""
        UPDATE users
        SET users_spin = "{count_of_spin - 1}"
        WHERE users_id = "{users_id}"
        """

        cursor.execute(sql)
        connect.commit()
        return True

