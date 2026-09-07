import mysql.connector





class Database:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Testing@2022",
            database="testmydata"
        )

        self.cursor = self.connection.cursor()

    def execute_query(self, query, values=None):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
