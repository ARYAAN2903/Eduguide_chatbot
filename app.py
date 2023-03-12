from flask import Flask
from flaskext.mysql import MySQL
from flask import request, render_template, redirect, url_for
from flask import session
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
import time
time.clock=time.time


app = Flask(__name__)
app.secret_key = 'my_secret_key'

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '27293003@ary'
app.config['MYSQL_DATABASE_DB'] = 'app'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

@app.route('/')
def show_login():
    return render_template('login.html')

@app.route('/register')
def show_register():
    return render_template('register.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        
        # validate the user's information
        # check if the username or email already exists in the database
        
        # if the information is valid, insert the new user into the database
        cursor = mysql.get_db().cursor()
        cursor.execute("INSERT INTO users (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
        mysql.get_db().commit()
        
        return redirect(url_for('login'))
    
    return render_template('register.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # check if the username and password match any entries in the database
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        
        if user:
            # store the user's information in a session variable
            session['user'] = user
            return redirect(url_for('dashboard'))
        else:
            # display an error message if the login information is invalid
            error = 'Invalid login credentials'
            return render_template('login.html', error=error)
    
    return render_template('login.html')



@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        # display the dashboard for the logged in user
        return render_template('dashboard.html')
    else:
        # redirect the user to the login page if they are not logged in
        return redirect(url_for('login.html'))

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

bot = ChatBot('EduGuide')
trainer = ListTrainer(bot)

# Create a ChatterBotCorpusTrainer and train it with the corpus data
corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english.greetings')


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()

