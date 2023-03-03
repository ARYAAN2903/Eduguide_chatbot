from flask import Flask,request,render_template
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "27293003@ary",
    database = "app"
)

 
cursor = mydb.cursor()


@app.route('/')
def login():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route("/login_validation",methods=['POST'])
def login_validation():
    name1=request.form.get['username']
    pwd=request.form.get['password']

    #cursor.execute("""SELECT * FROM users WHERE `username` LIKE '{}' AND `password` LIKE '{}'""".format(name1,pwd))
    # cursor.execute(f"SELECT * FROM users WHERE `username` LIKE {name1} AND `password` LIKE {pwd}")
    # users=cursor.fetchall()
    # if len(users)>0:
    #     return render_template('dashboard.html',name=name1)
    # else:
    #     return render_template('index.html')

    if name1 == 'aryaan2903' and pwd == '12345':
        return render_template('dashboard.html')
    else:
        return render_template('index.html')

if __name__ == '__app__':
    app.run(debug=True)