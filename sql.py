import sqlite3

class sqll:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()
    
    def user_in_base(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `user_info` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def get_api_token(self, user_id):
        get_q = f'SELECT API_TOKEN FROM user_info WHERE user_id = {user_id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            return str(*result).replace("('", '').replace("',)", '')

    def add_user(self, user_id, reg_date, API_TOKEN, subscription):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'user_info' ('user_id', 'reg_date', 'API_TOKEN', 'subscription') VALUES (?,?,?,?)", (user_id, reg_date, API_TOKEN, subscription))