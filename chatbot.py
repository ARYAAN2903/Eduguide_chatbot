from chatterbot import ChatBot
from flask import Flask, request,render_template
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from textblob import TextBlob

import time
import logging
import nltk

nltk.download('averaged_perceptron_tagger')
time.clock= time.time()

logger = logging.getLogger() 
logger.setLevel(logging.INFO)


bot = ChatBot('EduGuide', 
              logic_adapters=[
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response': 'Sorry, I could not understand your question. Please try again.',
                      'maximum_similarity_threshold': 0.90
                  }
              ]
             )

trainer = ListTrainer(bot)

app = Flask(__name__)


trainer.train(
    [
     "Hi",
"Helloo!",
"Hey",

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Brochure of top colleges in Mumbai</br>4.Cut-Off of Different Colleges</br>",

"Great",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Brochure of top colleges in Mumbai</br>4.Cut-Off of Different Colleges</br>",

"good",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Brochure of top colleges in Mumbai</br>4.Cut-Off of Different Colleges</br>",

"fine",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Brochure of top colleges in Mumbai</br>4.Cut-Off of Different Colleges</br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to guide and give you Information about The Admission process",

"What else can you do?",
"I can help you find colleges and help ypu filling application form",

"What is Freeze?",
"Candidates who are satisfied with their allotted seats and do not want to participate in further have to select this option. <br> By selecting this option candidates will confirm their allotted seats and will not be allowed to participate further",

"What is Slide?",
"By selecting this option candidates who wish to accept the seat allotted to them but will also be open for upgradation into a higher preferred course in the same institute. <br> If in further round these candidates are allotted in a higher preferred course then their previous seat will be cancelled </b>",

"What is Float?",
"This option allows candidates to upgrade their seat to a higher preferred choice of course at any institute. <br> However their earlier allotment will be cancelled if their choice of higher course is allotted to them. </b>",   

 "What is Merit List?",
 " After the declaration of result the exam conducting authority releases the provisional merit list in online mode. <br> The merit will be prepared based on the marks secured in the entrance exam. <br> The provisional merit list carries the name of candidates shortlisted for counselling along with their overall ranks. <br> To check the merit list candidates have to login into their account by entering application number and date of birth. <br> What needs to be noted is that separate merit list is prepared and released for JEE Main qualified candidates. <br> MHT CET merit list will be available separately for different groups like all India and Maharashtra candidates. <br> A few days window will be given to the candidates to send the complaint against the merit list if they have any. <br> After the feedback a final merit list will be published. </b> ",   

"What is merit List?",
" After the declaration of result the exam conducting authority releases the provisional merit list in online mode. <br> The merit will be prepared based on the marks secured in the entrance exam. <br> The provisional merit list carries the name of candidates shortlisted for counselling along with their overall ranks. <br> To check the merit list candidates have to login into their account by entering application number and date of birth. <br> What needs to be noted is that separate merit list is prepared and released for JEE Main qualified candidates. <br> MHT CET merit list will be available separately for different groups like all India and Maharashtra candidates. <br> A few days window will be given to the candidates to send the complaint against the merit list if they have any. <br> After the feedback a final merit list will be published. </b> ",   

 "documents needed?",   
 "Here are the list of important documents you will be needing:<b> ● Print out of counselling registration form <br> <br> ● MHT CET admit card and Result <br> ● Class 10 and 12 pass certificate and marksheet <br> ● Category certificate (if applicable) <br> ● Character and migration certificate <br> ● School leaving certificate <br> ● Domicile certificate (if applicable) </b>",

" list of importantdocuments needed?",   
"Here are the list of important documents you will be needing:<b> ● Print out of counselling registration form <br> <br> ● MHT CET admit card and Result <br> ● Class 10 and 12 pass certificate and marksheet <br> ● Category certificate (if applicable) <br> ● Character and migration certificate <br> ● School leaving certificate <br> ● Domicile certificate (if applicable) </b>",
 
    "1",
     "<b> ● Print out of counselling registration form <br> <br> ● MHT CET admit card and Result <br> ● Class 10 and 12 pass certificate and marksheet <br> ● Category certificate (if applicable) <br> ● Character and migration certificate <br> ● School leaving certificate <br> ● Domicile certificate (if applicable) </b>",
    
    "2",
    "<b> Following are the frequently asked questions during admission <br> <br> 2.1 What is Freeze <br> 2.2 What is Slide <br> 2.3 What is Float <br> 2.4 What is Merit List </b>",
    
    "2.1",
    " <b> What is Freeze : <br> Candidates who are satisfied with their allotted seats and do not want to participate in further have to select this option. <br> By selecting this option candidates will confirm their allotted seats and will not be allowed to participate further </b>",
    
    "2.2",
    " <b> What is Slide : <br> By selecting this option candidates who wish to accept the seat allotted to them but will also be open for upgradation into a higher preferred course in the same institute. <br> If in further round these candidates are allotted in a higher preferred course then their previous seat will be cancelled </b>",
   
    "2.3",
    "<b> What is Float : <br> This option allows candidates to upgrade their seat to a higher preferred choice of course at any institute. <br> However their earlier allotment will be cancelled if their choice of higher course is allotted to them. </b> ",
  
    "2.4",
    "<b>  What is Merit List : <br> After the declaration of result the exam conducting authority releases the provisional merit list in online mode. <br> The merit will be prepared based on the marks secured in the entrance exam. <br> The provisional merit list carries the name of candidates shortlisted for counselling along with their overall ranks. <br> To check the merit list candidates have to login into their account by entering application number and date of birth. <br> What needs to be noted is that separate merit list is prepared and released for JEE Main qualified candidates. <br> MHT CET merit list will be available separately for different groups like all India and Maharashtra candidates. <br> A few days window will be given to the candidates to send the complaint against the merit list if they have any. <br> After the feedback a final merit list will be published. </b> ",
   
    ]
)
while True:
    textInput = input("You : ")
    if(textInput=='quit'):
        break
    bot_response = bot.get_response(textInput)
    if float(bot_response.confidence) > 0.5:
        print("Bot: ", bot_response)
    else:
        print("Bot: Sorry, I am not sure what you mean.")
        print("Bot: Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Brochure of top colleges in Mumbai</br>4.Cut-Off of Different Colleges</br>")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    bot_response = bot.get_response(userText)
    if float(bot_response.confidence) > 0.5:
        return str(bot_response)
    else:
        return "Sorry, I am not sure what you mean.Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Brochure of top colleges in Mumbai</br>4.Cut-Off of Different Colleges</br>"




