import os
import pymysql
from flask import Flask

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_DATABASE_HOST', 'localhost')
app.config['MYSQL_USER'] = 'db_user'
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', '')
app.config['MYSQL_DB'] = 'employee_db'

@app.route('/')
def index():
    try:
        connection = pymysql.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DB'],
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM employees")
            rows = cursor.fetchall()

        connection.close()

        if not rows:
            return "No employees found."

        return "Employees: " + ", ".join([row['name'] for row in rows])
    except Exception as e:
        return f"Error connecting to database: {str(e)}", 500

if __name__ == '__main__':
    app.debug = True
    app.run()
