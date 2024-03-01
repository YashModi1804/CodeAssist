
from flask import Flask, render_template, request, jsonify

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
cursor = connection.cursor()


app = Flask(__name__)

# Route for the main page
@app.route("/")
def home():
    cursor.execute("select * from question")
    result = cursor.fetchall()
    
    question_data = {
    'java': result[0]['java'],
    'python': result[0]['python'],
    'cpp': result[0]['cpp'],
    'A': result[0]['a'],
    'B': result[0]['b'],
    'C': result[0]['c'],
    'D': result[0]['d']
    }
    return render_template("main.html", question = question_data)
@app.route("/push")
def push():
    return render_template("push.html")

@app.route("/pushdata",methods = ["POST", "GET"])
def pushData():
    data = request.json
    result = ""
    try:
        cursor.execute("set autocommit = 1")
        # cursor.execute(f"insert into student_data values('{data['name']}', '{data['enroll']}', '{data['ans']}');")
        # cursor.execute("create table question (java varchar(200), python varchar(200), cpp varchar(200) primary key, a varchar(100), b varchar(100), c varchar(100), d varchar(100))")
        cursor.execute(f"insert into question values('{data['java']}', '{data['python']}', '{data['cpp']}','{data['a']}','{data['b']}','{data['c']}','{data['d']}');")
        # cursor.execute("delete from question;")
        # cursor.execute("select * from question;")
        # result = cursor.fetchall()
        # print(result)
        return jsonify("data pushed successfully")
    except Exception as e:
        print(e)
    return jsonify("post unsuccessfull")

@app.route("/getdata", methods=["POST", "GET"])
def getdata():
    try:
        # cursor.execute("create table student_data (name varchar(30), enroll varchar(11) primary key, answer varchar(500));")
        cursor.execute("set autocommit = 1;")
        # cursor.execute(f"insert into student_data values('{data['name']}', '{data['enroll']}', '{data['ans']}');")
        # cursor.execute("delete from student_data where name = 'Deepak Yadav';")
        cursor.execute(f"select * from student_data;")
        result = cursor.fetchall()
        return jsonify(result)
    except Exception as e:
        print("Error occurred:", e)
        # Optionally, you can raise the exception to halt the program
        raise

@app.route("/write", methods=["POST","GET"])
def write():
    data = request.json
    res = {
        'msg': "",
        'val':0
    }

    try:
        # cursor.execute("create table student_data (name varchar(30), enroll varchar(11) primary key, answer varchar(500));")
        cursor.execute("set autocommit = 1;")
        cursor.execute(f"select * from student_data where enroll='{data['enroll']}';")
        # cursor.execute("delete from student_data where name = 'Deepak Yadav';")
        
        result = cursor.fetchall()
        print(result)
        if(result != ()):
            res['msg'] = "you have already answered today"
            res['val'] = 0
            return jsonify(res)
    except Exception as e:
        print("Error occurred:", e)
        # Optionally, you can raise the exception to halt the program
        raise

    cursor.execute(f"insert into student_data values('{data['name']}', '{data['enroll']}', '{data['ans']}');")

    res['msg'] = "answer submitted successfully"
    res['val'] = 1
    return jsonify(res)



if __name__ == "__main__":
    app.run(debug=True)

