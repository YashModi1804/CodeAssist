
from flask import Flask, render_template, request

# database
import pymysql

timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="codeassist-codeassist.a.aivencloud.com",
    password="AVNS_dIB72iujYgE0YglUFSo",
    read_timeout=timeout,
    port=24991,
    user="avnadmin",
    write_timeout=timeout,
)

# try:
#     cursor = connection.cursor()
#     # cursor.execute("create table student_data (name varchar(30), enroll varchar(11) primary key, answer varchar(500));")
#     # cursor.execute("set autocommit = 1;")
#     # cursor.execute("insert into student_data values('Deepak Yadav', '2022BCSE036', 'galat ans');")
#     # cursor.execute("delete from student_data where name = 'Deepak Yadav';")
#     cursor.execute("select * from student_data;")
    
#     print(cursor.fetchall())
# finally:
#     # print("closed")
#     connection.close()

app = Flask(__name__)

# Route for the main page
@app.route("/")
def home():
    return render_template("main.html")

@app.route("/write", methods=["POST"])
def write():
    data = request.json

    try:
        cursor = connection.cursor()
        # cursor.execute("create table student_data (name varchar(30), enroll varchar(11) primary key, answer varchar(500));")
        cursor.execute("set autocommit = 1;")
        cursor.execute(f"insert into student_data values('{data['name']}', '{data['enroll']}', '{data['ans']}');")
        # cursor.execute("delete from student_data where name = 'Deepak Yadav';")
        cursor.execute("select * from student_data;")
        
        result = cursor.fetchall()
        print(result)
    except Exception as e:
        print("Error occurred:", e)
        # Optionally, you can raise the exception to halt the program
        raise

    return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)

