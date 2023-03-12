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
