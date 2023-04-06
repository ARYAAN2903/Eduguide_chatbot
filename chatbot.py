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
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Scholarship related info</br>4.Top Colleges</br>",

"Great",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Scholarship related info</br>4.Top Colleges</br>",

"good",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Scholarship related info</br>4.Top Colleges</br>",

"fine",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Scholarship related information</br>4.Top Colleges</br>",

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
 
 " Top Colleges cet?",
 "Here are the Top Colleges in Maharashtra through CET EXAMINATION: <br> 1.COEP Pune <br> 2.VJTI Mumbai <br> 3. GHRCE Nagpur <br> 4.SPIT Mumbai <br> 5.RCOEM Nagpur <br> 6.YCCE Nagpur <br> 7.WCE Sangli <br> 8.MIT World Peace University,Pune <br> 9.MKSSS'S Cummins College of Engineering for Women,Pune <br> 10.DJSCE MUMBAI </b>",
 
 " Top Engineering Colleges in Maharashtra ?",  
 "Here are the Top Colleges in Maharashtra through CET EXAMINATION: <br> 1.COEP Pune <br> 2.VJTI Mumbai <br> 3. GHRCE Nagpur <br> 4.SPIT Mumbai <br> 5.RCOEM Nagpur <br> 6.YCCE Nagpur <br> 7.WCE Sangli <br> 8.MIT World Peace University,Pune <br> 9.MKSSS'S Cummins College of Engineering for Women,Pune <br> 10.DJSCE MUMBAI </b>",

 " Top Engineering Colleges in Mumbai??",   
 "Here are the Top Colleges in Mumbai through CET EXAMINATION: <br> 1.VJTI Mumbai <br> 2.SPIT Mumbai <br> 3.DJSCE Mumbai  <br> 4.TSEC Mumbai <br> 5.VIT Mumbai <br> 6.Atharva College of Engineering Mumbai <br> 7.Don Bosco Institue Of Technology, Mumbai <br> 8.VESIT Mumbai <br> 9.RCOE Mumbai <br> 10.CRCE MUMBAI </b>",
 
 " Top Engineering Colleges in Pune?",
 "Here are the Top Colleges in Pune through CET EXAMINATION: <br> 1.COEP Pune <br> 2.MIT World Peace University, Pune <br> 3.MKSSS's Cummins College of Engineering for Women,Pune  <br> 4.Vishwakarma Institue of Technology, Pune  <br> 5.MIT Academy of Engineering, Pune <br> 6.MIT-WPU Faculty of Engineering,Pune <br> 7.PICT Pune <br> 8.JSPM Narhe Technical Campus,Pune <br> 9.IIT Pune <br> 10.DPCOE ,Pune </b>",
  
  "What is CET in engineering?",
  "CET stands for Common Entrance Test for engineering. It is a competitive exam conducted by various state-level and national-level authorities to provide admission to undergraduate engineering courses in various colleges and universities across India. </b>",
  
  "Who is eligible to take the CET exam for engineering?",
  "The eligibility criteria for CET vary from state to state, but in general, candidates who have completed their 10+2 education with Physics, Chemistry, and Mathematics as compulsory subjects are eligible to appear for the exam.</b>",

  "What is the application process for CET?",
  "The application process for CET involves registering online on the official website of the exam conducting authority. Candidates need to provide their personal and educational details, upload their photograph and signature, and pay the application fee. The application process usually starts a few months before the exam date.</b>",
  
  "What is the syllabus for CET?",
  "The syllabus for CET includes topics from Physics, Chemistry, and Mathematics that are covered in the 10+2 education. The level of difficulty and the weightage of each topic may vary depending on the state and the conducting authority.</b>",

  "How is the CET exam conducted?",
  "The CET exam is usually conducted in an online mode (computer based) and has multiple-choice questions. The duration of the exam is typically 3 hours, and there is no negative marking for wrong answers like JEE and NEET entrance exams.</b>",

  "What is the selection process after CET?",
  "The selection process after CET involves counseling rounds based on the candidate's rank in the exam. Candidates need to register for counseling, and seats are allotted based on their preferences and availability.</b>",

  "scholarship?",
  "There are different types of scholarship for Engineering students after CET. For further information Select 3 in the list of queries </b>",

  "government scholarship?",
  "Government Scholarships: Various government departments offer scholarships for engineering students. These scholarships are usually based on academic performance, and other criteria such as financial need, minority status, and disability. Some popular government scholarships for engineering students in India include the INSPIRE Scholarship, Jindal Scholarship, and Sitaram Jindal Scholarship.</b>",

  "Private Scholarships?",
  "Many private companies and organizations offer scholarships for engineering students based on academic merit, financial need, and other criteria. Some of the well-known private scholarships for engineering students include the Tata Scholarship, L&T Build India Scholarship, and Samsung Star Scholarship.</b>",

  "Merit-based Scholarships?",
  "Many colleges and universities offer merit-based scholarships for engineering students who have excelled academically. These scholarships are usually awarded based on the student's CET rank, and they can cover a percentage of tuition fees or the full tuition fees.<b/>",

  "Need-based Scholarships?",
  "Some colleges and universities also offer need-based scholarships for engineering students who come from economically weaker backgrounds. These scholarships are usually awarded based on the student's family income, and they can cover a percentage of tuition fees or the full tuition fees.</b>",

  "Sports Scholarships?",
  "If you are a talented athlete, you may also be eligible for sports scholarships offered by colleges and universities. These scholarships are usually awarded based on your sports performance and can cover a percentage of tuition fees or the full tuition fees.</b>",

  "scholarship site?",
  " Site name is (https://mahadbt.maharashtra.gov.in/login/login) ",
    
    "1",
     "<b> ● Print out of counselling registration form <br> <br> ● MHT CET admit card and Result <br> ● Class 10 and 12 pass certificate and marksheet <br> ● Category certificate (if applicable) <br> ● Character and migration certificate <br> ● School leaving certificate <br> ● Domicile certificate (if applicable) </b>",
    
    "2",
    "<b> Following are the frequently asked questions during admission <br> <br> 2.1 What is Freeze <br> 2.2 What is Slide <br> 2.3 What is Float <br> 2.4 What is Merit List <br> 2.5 What is CET in engineering? <br> 2.6 Who is eligible to take the CET exam for engineering <br> 2.7 What is the application process for CET? <br> 2.8 What is the syllabus for CET? <br> 2.9 How is the CET exam conducted? <br> 2.10 What is the selection process after CET? </b>",
    
    "2.1",
    " <b> What is Freeze : <br> Candidates who are satisfied with their allotted seats and do not want to participate in further have to select this option. <br> By selecting this option candidates will confirm their allotted seats and will not be allowed to participate further </b>",
    
    "2.2",
    " <b> What is Slide : <br> By selecting this option candidates who wish to accept the seat allotted to them but will also be open for upgradation into a higher preferred course in the same institute. <br> If in further round these candidates are allotted in a higher preferred course then their previous seat will be cancelled </b>",
   
    "2.3",
    "<b> What is Float : <br> This option allows candidates to upgrade their seat to a higher preferred choice of course at any institute. <br> However their earlier allotment will be cancelled if their choice of higher course is allotted to them. </b> ",
  
    "2.4",
    "<b>  What is Merit List : <br> After the declaration of result the exam conducting authority releases the provisional merit list in online mode. <br> The merit will be prepared based on the marks secured in the entrance exam. <br> The provisional merit list carries the name of candidates shortlisted for counselling along with their overall ranks. <br> To check the merit list candidates have to login into their account by entering application number and date of birth. <br> What needs to be noted is that separate merit list is prepared and released for JEE Main qualified candidates. <br> MHT CET merit list will be available separately for different groups like all India and Maharashtra candidates. <br> A few days window will be given to the candidates to send the complaint against the merit list if they have any. <br> After the feedback a final merit list will be published. </b> ",
    
    "2.5",
    "<b>  What is CET in engineering? : <br> CET stands for Common Entrance Test for engineering. It is a competitive exam conducted by various state-level and national-level authorities to provide admission to undergraduate engineering courses in various colleges and universities across India. </b>",

    "2.6",
    " <b> Who is eligible to take the CET exam for engineering? : <br> The eligibility criteria for CET vary from state to state, but in general, candidates who have completed their 10+2 education with Physics, Chemistry, and Mathematics as compulsory subjects are eligible to appear for the exam.</b>",

    "2.7",
    " <b>  What is the application process for CET? : <br> The application process for CET involves registering online on the official website of the exam conducting authority. Candidates need to provide their personal and educational details, upload their photograph and signature, and pay the application fee. The application process usually starts a few months before the exam date.</b>",

    "2.8",
    " <b>  What is the syllabus for CET?: <br> The syllabus for CET includes topics from Physics, Chemistry, and Mathematics that are covered in the 10+2 education. The level of difficulty and the weightage of each topic may vary depending on the state and the conducting authority.</b>",

    "2.9",
    " <b>  How is the CET exam conducted?: <br> The CET exam is usually conducted in an online mode (computer based) and has multiple-choice questions. The duration of the exam is typically 3 hours, and there is no negative marking for wrong answers like JEE and NEET entrance exams.</b>",
 
    "2.10",
    "<b>  What is the selection process after CET?:  <br> The selection process after CET involves counseling rounds based on the candidate's rank in the exam. Candidates need to register for counseling, and seats are allotted based on their preferences and availability.</b>",
    
    "3",
    "<b > Scholarship related information <br> <br> 3.1 Government Scholarships? <br> 3.2 Private Scholarships? <br> 3.3 Merit-based Scholarships? <br> 3.4 Need-based Scholarships? <br> 3.5 Sports Scholarships? </b>",
    
    "3.1",
    " <b> Government Scholarships? : <br> Government Scholarships: Various government departments offer scholarships for engineering students. These scholarships are usually based on academic performance, and other criteria such as financial need, minority status, and disability. Some popular government scholarships for engineering students in India include the INSPIRE Scholarship, Jindal Scholarship, and Sitaram Jindal Scholarship.</b>",

    "3.2",
    " <b> Private Scholarships? : <br> Many private companies and organizations offer scholarships for engineering students based on academic merit, financial need, and other criteria. Some of the well-known private scholarships for engineering students include the Tata Scholarship, L&T Build India Scholarship, and Samsung Star Scholarship.</b>",

    "3.3",
    " <b> Merit-based Scholarships? : Many colleges and universities offer merit-based scholarships for engineering students who have excelled academically. These scholarships are usually awarded based on the student's CET rank, and they can cover a percentage of tuition fees or the full tuition fees.<b/>",

    "3.4",
    "<b> Need-based Scholarships? : <br> Some colleges and universities also offer need-based scholarships for engineering students who come from economically weaker backgrounds. These scholarships are usually awarded based on the student's family income, and they can cover a percentage of tuition fees or the full tuition fees.</b>",

    "3.5",
    " <b> Sports Scholarships? : <br> If you are a talented athlete, you may also be eligible for sports scholarships offered by colleges and universities. These scholarships are usually awarded based on your sports performance and can cover a percentage of tuition fees or the full tuition fees.</b>",

    "4",
    "<b> Top Engineering Colleges <br> <br> 4.1 Top Engineering Colleges in Maharashtra? <br> 4.2 Top Engineering Colleges in Mumbai? <br> 4.3 Top Engineering Colleges in Pune? </b> ",
    
    "4.1",
    " <b> Here are the Top Colleges in Maharashtra through CET EXAMINATION: <br> 1.COEP Pune <br> 2.VJTI Mumbai <br> 3. GHRCE Nagpur <br> 4.SPIT Mumbai <br> 5.RCOEM Nagpur <br> 6.YCCE Nagpur <br> 7.WCE Sangli <br> 8.MIT World Peace University,Pune <br> 9.MKSSS'S Cummins College of Engineering for Women,Pune <br> 10.DJSCE MUMBAI </b>",

    "4.2",
    " <b> Here are the Top Colleges in Mumbai through CET EXAMINATION: <br> 1.VJTI Mumbai <br> 2.SPIT Mumbai <br> 3.DJSCE Mumbai  <br> 4.TSEC Mumbai <br> 5.VIT Mumbai <br> 6.Atharva College of Engineering Mumbai <br> 7.Don Bosco Institue Of Technology, Mumbai <br> 8.VESIT Mumbai <br> 9.RCOE Mumbai <br> 10.CRCE MUMBAI </b>",
    
    "4.3",
    " <b> Here are the Top Colleges in Pune through CET EXAMINATION: <br> 1.COEP Pune <br> 2.MIT World Peace University, Pune <br> 3.MKSSS's Cummins College of Engineering for Women,Pune  <br> 4.Vishwakarma Institue of Technology, Pune  <br> 5.MIT Academy of Engineering, Pune <br> 6.MIT-WPU Faculty of Engineering,Pune <br> 7.PICT Pune <br> 8.JSPM Narhe Technical Campus,Pune <br> 9.IIT Pune <br> 10.DPCOE ,Pune </b>",
    
    
    
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
        print("Bot: Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Scholarship related info </br> 4.Top Colleges</br>")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    bot_response = bot.get_response(userText)
    if float(bot_response.confidence) > 0.5:
        return str(bot_response)
    else:
        return "Sorry, I am not sure what you mean.Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Scholarship related info </br> 4.Top Colleges </br>"
