from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import logging
time.clock= time.time
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('EduGuide')
trainer = ListTrainer(chatbot)

trainer.train(
    [
        "Hello",
        "Hi there!",
        "How are you doing?",
        "I am doing great",
        "Can you guide me regarding the admission process?",
        "Yes sure! Here are some important guidlines you need to follow",
        "What are the important documents needed?",
        "Here are the list of important documents you will be needing to complete your admission process."
    ]
)

while True:
    textInput = input("You : ")
    if(textInput=='quit'):
        break
    print("Bot: ", chatbot.get_response(textInput))