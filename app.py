from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_data():
    conn = mysql.connector.connect(
        host='localhost',
        user='your_user',
        password='your_password',
        database='student_db'
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    students = get_data()
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
