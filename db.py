import psycopg2


class DatabaseConnection:
    def __init__(self):

        try:
            connection_str = "dbname='diarytestdb' user='postgres' host='localhost' password='12345'"
            self.connection = psycopg2.connect(connection_str)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

        except Exception as e:
            self.connection.rollback()
            print(e)
            print("Failed to connect to the database")

    def create_table_users(self):
        create_database_table = " CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, \
         name  VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL UNIQUE, \
         password VARCHAR NOT NULL, create_date TIMESTAMP DEFAULT  CURRENT_TIMESTAMP)"
        self.cursor.execute(create_database_table)

    def delete_table(self):
        delete = "TRUNCATE TABLE users RESTART IDENTITY CASCADE"
        self.cursor.execute(delete)

    def close(self):
        self.cursor.close()


if __name__ == "__main__":
    database_connection = DatabaseConnection()
    database_connection.create_table_users()
