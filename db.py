import psycopg2
import os

class DatabaseConnection:
    def __init__(self):

        try:
            connection_str = os.environ.get('DATABASE_URL')
            self.connection = psycopg2.connect(connection_str)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

        except Exception as e:
            self.connection.rollback()
            print(e)
            print("Failed to connect to the database")

    def create_table_users(self):
        Query_string = " CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, \
         name  VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL UNIQUE, \
         password VARCHAR NOT NULL, create_date TIMESTAMP DEFAULT  CURRENT_TIMESTAMP)"
        self.cursor.execute(Query_string)
    
    def create_table_entries(self):
        Query_string = "CREATE TABLE IF NOT EXISTS entries(entry_id SERIAL PRIMARY KEY NOT NULL, \
         diaryTitle TEXT NOT NULL, diaryBody TEXT NOT NULL, diaryDate DATE NOT NULL, \
          user_id INT REFERENCES users(id))"
        self.cursor.execute(Query_string)
    
    def delete_table(self):
        delete = "TRUNCATE TABLE users RESTART IDENTITY CASCADE"
        self.cursor.execute(delete)

    def close(self):
        self.cursor.close()


if __name__ == "__main__":
    database_connection = DatabaseConnection()
    database_connection.create_table_users()
    database_connection.create_table_entries()
