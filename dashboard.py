# import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
from flask import Flask, render_template, request,redirect
import time
time.clock=time.time

app = Flask(__name__)

@app.route("/chatbot")
def chatbot():
           return render_template('chatbot.html')

@app.route('/login')
def show_login():
    return render_template('login.html')

@app.route('/register')
def show_register():
    return render_template('register.html')

bot = ChatBot('EduGuide')
trainer = ListTrainer(bot)

# Create a ChatterBotCorpusTrainer and train it with the corpus data
corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english.greetings')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    bot_response = bot.get_response(userText)
    if float(bot_response.confidence) > 0.5:
        return str(bot_response)
    else:
        return "Sorry, I am not sure what you mean.Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Brochure of top colleges in Mumbai</br>4.Cut-Off of Different Colleges</br>"

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')
