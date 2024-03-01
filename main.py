
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

question_data = {
    'java': 'https://imgs.search.brave.com/D6Tct29SgNOuVzHkFM5Wl26LEmYJxvQjqVUNe9xSJPE/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9laS5w/aG5jZG4uY29tL2lz/LXN0YXRpYy9pbWFn/ZXMvY2F0ZWdvcmll/cy8obT1xSVcyNTZU/YmVnWjg4emphZE9m/KShtaD1EbTJUdlM3/bjhKV3BBb21OKTUu/anBn',
    'python': 'https://imgs.search.brave.com/LME7nof0d4-eOXnXgz5JZSZhnDgJphVGAyMZJgcZhWg/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9laS5w/aG5jZG4uY29tL2lz/LXN0YXRpYy9pbWFn/ZXMvY2F0ZWdvcmll/cy8obT1xX0czNTZU/YmVnWjg4emphZE9m/KShtaD00WnRuVkF5/THc4X3RRM3JWKTQu/anBn',
    'cpp': 'https://imgs.search.brave.com/hMTGCMtyqgJetEX8PQ46l86rwa9-d46EnwYOmr2lxyY/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9laS5w/aG5jZG4uY29tL2lz/LXN0YXRpYy9pbWFn/ZXMvY2F0ZWdvcmll/cy8obT1xWTE1NTZU/YmVxTTQ4emphZE9m/KShtaD1DeEppX2Mt/ZnJfTmxiTERMKXJv/a3VfMjIuanBn',
    'A': 'option a',
    'B': 'option b',
    'C': 'option c',
    'D': 'option d'
}
app = Flask(__name__)

# Route for the main page
@app.route("/")
def home():
    return render_template("main.html", question = question_data)

@app.route("/getdata")
def getdata():
    try:
        cursor = connection.cursor()
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
        cursor = connection.cursor()
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

