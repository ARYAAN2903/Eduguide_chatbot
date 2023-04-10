# import files
from flask import Flask, render_template, request
from flask import Flask, redirect, url_for, session, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
from flask import Flask, render_template, request,redirect
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import Flow



time.clock=time.time

client_config = {
    "installed": {
        "client_id": "1032842133365-f30g0qla8r02i1bebddfdam42fv9fk6o.apps.googleusercontent.com",
        "client_secret": "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",
        "redirect_uris": ["http://127.0.0.1:5000/google/auth"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "access_type": "offline",
        "prompt": "consent"
    }
}

CLIENT_ID = '1032842133365-f30g0qla8r02i1bebddfdam42fv9fk6o.apps.googleusercontent.com'
CLIENT_SECRET = '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'
SCOPES = ['https://www.googleapis.com/auth/drive.file']
API_SERVICE_NAME = 'drive'
API_VERSION = 'v3'

app = Flask(__name__)


@app.route("/chatbot")
def chatbot():
           return render_template('chatbot.html')


@app.route('/logout')
def logout():
    # clear the session data
    session.pop('user', None)

    # redirect the user to the login page
    return render_template('login.html')

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


@app.route('/authorize')
def authorize():
    flow = Flow.from_client_config(
        client_config={'1032842133365-f30g0qla8r02i1bebddfdam42fv9fk6o.apps.googleusercontent.com': CLIENT_ID, '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': CLIENT_SECRET, 'https://www.googleapis.com/auth/drive.file': SCOPES},
        scopes=SCOPES,
        redirect_uri=url_for('oauth2callback', _external=True),
        authorization_prompt_message='Please authorize this application to access your Google Drive.',
    )
    authorization_url, state = flow.authorization_url(access_type='offline', prompt='consent')
    session['state'] = state
    return redirect(authorization_url)

@app.route('/oauth2callback')
def oauth2callback():
    state = session['state']
    flow = Flow.from_client_config(
        client_config={'1032842133365-f30g0qla8r02i1bebddfdam42fv9fk6o.apps.googleusercontent.com': CLIENT_ID, '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': CLIENT_SECRET, 'https://www.googleapis.com/auth/drive.file': SCOPES},
        scopes=SCOPES,
        redirect_uri=url_for('oauth2callback', _external=True),
        state=state,
    )
    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials
    session['credentials'] = credentials.to_authorized_user_info()
    return redirect(url_for('index'))

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/api')
def api():
    # Render the HTML template for the login page
    return render_template('index.html')
