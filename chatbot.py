from chatterbot import ChatBot
from flask import Flask, request,render_template
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
import logging
time.clock= time.time
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)


bot = ChatBot('EduGuide')
trainer = ListTrainer(bot)

app = Flask(__name__)


trainer.train(
    [
        "Hello",
        "Hi there!",
        "How are you doing?",
        "I am doing great",
        "Can you guide me regarding the admission process?",
        "Yes sure! Here are some important guidlines you need to follow",
        "What are the important documents needed?",
        "Here are the list of important documents you will be needing to complete your admission process.",
        "Can u give me the brochure of some top colleges in Mumbai?",
        "Here are some top colleges in mumbai along with their brochure.",
    ]
)

# Create a ChatterBotCorpusTrainer and train it with the corpus data
corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english.greetings')


while True:
    textInput = input("You : ")
    if(textInput=='quit'):
        break
    print("Bot: ", bot.get_response(textInput))

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))
