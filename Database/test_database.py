# Database	           Python library
# MySQL	             pip install mysql-connector-python
# PostgreSQL	     pip install psycopg
# SQLite	         pip install sqlite3   (Python's built-in)
# SQL Server	     pip install pyodbc
# Oracle	         pip install oracledb


from Database.db_utils import Database

def test_user_details():

    db = Database()

    result = db.execute_query(
        """
        SELECT name, email, status
        FROM users
        WHERE email = %s
        """,
        ("harendra.desala@gmail.com",)
    )

    print(result)

    assert result is not None
    assert len(result) == 1

    assert result[0][0] == "hari"
    assert result[0][1] == "harendra.desala@gmail.com"
    assert result[0][2] == "active"

    db.close()







