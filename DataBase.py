import sqlite3


class Database:
    def __init__(self, path_to_db='UsersOrder.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()

        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE UsersOrder(
        user_id INTEGER NOT NULL,
        id_purchase INTEGER NOT NULL,
        status TEXT NOT NULL,
        purchase_text TEXT NOT NULL,
        ship_type TEXT NOT NULL,
        place TEXT);
        """
        return self.execute(sql)

    def add_user(self, user_id: int, id_purchase: str, status: str, purchase_text: str, ship_type: str,
                 place: str = None):
        sql = "INSERT INTO UsersOrder(user_id, id_purchase, status, purchase_text, ship_type, place) " \
              "VALUES  (?, ?, ?, ?, ?, ?)"
        parameters = (user_id, id_purchase, status, purchase_text, ship_type, place)
        self.execute(sql, parameters=parameters, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f'{item} = ?' for item in parameters
        ])
        return sql, tuple(parameters.values())


def logger(statement):
    print(f"""
___________________________
EXECUTING
{statement}
___________________________
""")


db = Database()
