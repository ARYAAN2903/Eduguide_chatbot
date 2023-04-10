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
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Scholarship related info</br>4.Top Colleges</br>5.Engineering Colleges as per your CET Percentile</br>",

"Great",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Scholarship related info</br>4.Top Colleges</br>5.Engineering Colleges as per your CET Percentile</br>",

"good",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Scholarship related info</br>4.Top Colleges</br>5.Engineering Colleges as per your CET Percentile</br>",

"fine",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Scholarship related info</br>4.Top Colleges</br>5.Engineering Colleges as per your CET Percentile</br>",

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

"Freeze",
"Candidates who are satisfied with their allotted seats and do not want to participate in further have to select this option. <br> By selecting this option candidates will confirm their allotted seats and will not be allowed to participate further",

"What is Freeze?",
"Candidates who are satisfied with their allotted seats and do not want to participate in further have to select this option. <br> By selecting this option candidates will confirm their allotted seats and will not be allowed to participate further",

"Slide",
"By selecting this option candidates who wish to accept the seat allotted to them but will also be open for upgradation into a higher preferred course in the same institute. <br> If in further round these candidates are allotted in a higher preferred course then their previous seat will be cancelled </b>",

"What is Slide?",
"By selecting this option candidates who wish to accept the seat allotted to them but will also be open for upgradation into a higher preferred course in the same institute. <br> If in further round these candidates are allotted in a higher preferred course then their previous seat will be cancelled </b>",

"Float",
"This option allows candidates to upgrade their seat to a higher preferred choice of course at any institute. <br> However their earlier allotment will be cancelled if their choice of higher course is allotted to them. </b>",   


"What is Float?",
"This option allows candidates to upgrade their seat to a higher preferred choice of course at any institute. <br> However their earlier allotment will be cancelled if their choice of higher course is allotted to them. </b>",   

 "Merit List",
 " After the declaration of result the exam conducting authority releases the provisional merit list in online mode. <br> The merit will be prepared based on the marks secured in the entrance exam. <br> The provisional merit list carries the name of candidates shortlisted for counselling along with their overall ranks. <br> To check the merit list candidates have to login into their account by entering application number and date of birth. <br> What needs to be noted is that separate merit list is prepared and released for JEE Main qualified candidates. <br> MHT CET merit list will be available separately for different groups like all India and Maharashtra candidates. <br> A few days window will be given to the candidates to send the complaint against the merit list if they have any. <br> After the feedback a final merit list will be published. </b> ",

 "What is Merit List?",
 " After the declaration of result the exam conducting authority releases the provisional merit list in online mode. <br> The merit will be prepared based on the marks secured in the entrance exam. <br> The provisional merit list carries the name of candidates shortlisted for counselling along with their overall ranks. <br> To check the merit list candidates have to login into their account by entering application number and date of birth. <br> What needs to be noted is that separate merit list is prepared and released for JEE Main qualified candidates. <br> MHT CET merit list will be available separately for different groups like all India and Maharashtra candidates. <br> A few days window will be given to the candidates to send the complaint against the merit list if they have any. <br> After the feedback a final merit list will be published. </b> ",   

"What is merit List?",
" After the declaration of result the exam conducting authority releases the provisional merit list in online mode. <br> The merit will be prepared based on the marks secured in the entrance exam. <br> The provisional merit list carries the name of candidates shortlisted for counselling along with their overall ranks. <br> To check the merit list candidates have to login into their account by entering application number and date of birth. <br> What needs to be noted is that separate merit list is prepared and released for JEE Main qualified candidates. <br> MHT CET merit list will be available separately for different groups like all India and Maharashtra candidates. <br> A few days window will be given to the candidates to send the complaint against the merit list if they have any. <br> After the feedback a final merit list will be published. </b> ",   

"documents",   
 "Here are the list of important documents you will be needing:<b> ● Print out of counselling registration form <br> <br> ● MHT CET admit card and Result <br> ● Class 10 and 12 pass certificate and marksheet <br> ● Category certificate (if applicable) <br> ● Character and migration certificate <br> ● School leaving certificate <br> ● Domicile certificate (if applicable) </b>",

 "documents needed?",   
 "Here are the list of important documents you will be needing:<b> ● Print out of counselling registration form <br> <br> ● MHT CET admit card and Result <br> ● Class 10 and 12 pass certificate and marksheet <br> ● Category certificate (if applicable) <br> ● Character and migration certificate <br> ● School leaving certificate <br> ● Domicile certificate (if applicable) </b>",

" list of important documents needed?",   
"Here are the list of important documents you will be needing:<b> ● Print out of counselling registration form <br> <br> ● MHT CET admit card and Result <br> ● Class 10 and 12 pass certificate and marksheet <br> ● Category certificate (if applicable) <br> ● Character and migration certificate <br> ● School leaving certificate <br> ● Domicile certificate (if applicable) </b>",
 
 " Top Colleges Maharashtra?",
 "Here are the Top Colleges in Maharashtra through CET EXAMINATION: <br> 1.COEP Pune <br> 2.VJTI Mumbai <br> 3. GHRCE Nagpur <br> 4.SPIT Mumbai <br> 5.RCOEM Nagpur <br> 6.YCCE Nagpur <br> 7.WCE Sangli <br> 8.MIT World Peace University,Pune <br> 9.MKSSS'S Cummins College of Engineering for Women,Pune <br> 10.DJSCE MUMBAI </b>",
 
 " Top Engineering Colleges in Maharashtra ?",  
 "Here are the Top Colleges in Maharashtra through CET EXAMINATION: <br> 1.COEP Pune <br> 2.VJTI Mumbai <br> 3. GHRCE Nagpur <br> 4.SPIT Mumbai <br> 5.RCOEM Nagpur <br> 6.YCCE Nagpur <br> 7.WCE Sangli <br> 8.MIT World Peace University,Pune <br> 9.MKSSS'S Cummins College of Engineering for Women,Pune <br> 10.DJSCE MUMBAI </b>",

 " Top Engineering Colleges in Mumbai??",   
 "Here are the Top Colleges in Mumbai through CET EXAMINATION: <br> 1.VJTI Mumbai <br> 2.SPIT Mumbai <br> 3.DJSCE Mumbai  <br> 4.TSEC Mumbai <br> 5.VIT Mumbai <br> 6.Atharva College of Engineering Mumbai <br> 7.Don Bosco Institue Of Technology, Mumbai <br> 8.VESIT Mumbai <br> 9.RCOE Mumbai <br> 10.CRCE MUMBAI </b>",
 
 " Top Engineering Colleges in Pune?",
 "Here are the Top Colleges in Pune through CET EXAMINATION: <br> 1.COEP Pune <br> 2.MIT World Peace University, Pune <br> 3.MKSSS's Cummins College of Engineering for Women,Pune  <br> 4.Vishwakarma Institue of Technology, Pune  <br> 5.MIT Academy of Engineering, Pune <br> 6.MIT-WPU Faculty of Engineering,Pune <br> 7.PICT Pune <br> 8.JSPM Narhe Technical Campus,Pune <br> 9.IIT Pune <br> 10.DPCOE ,Pune </b>",
  
  "Top Colleges in Mumbai??",   
  "Here are the Top Colleges in Mumbai through CET EXAMINATION: <br> 1.VJTI Mumbai <br> 2.SPIT Mumbai <br> 3.DJSCE Mumbai  <br> 4.TSEC Mumbai <br> 5.VIT Mumbai <br> 6.Atharva College of Engineering Mumbai <br> 7.Don Bosco Institue Of Technology, Mumbai <br> 8.VESIT Mumbai <br> 9.RCOE Mumbai <br> 10.CRCE MUMBAI </b>",
  
  "Top Colleges in Pune?",
  "Here are the Top Colleges in Pune through CET EXAMINATION: <br> 1.COEP Pune <br> 2.MIT World Peace University, Pune <br> 3.MKSSS's Cummins College of Engineering for Women,Pune  <br> 4.Vishwakarma Institue of Technology, Pune  <br> 5.MIT Academy of Engineering, Pune <br> 6.MIT-WPU Faculty of Engineering,Pune <br> 7.PICT Pune <br> 8.JSPM Narhe Technical Campus,Pune <br> 9.IIT Pune <br> 10.DPCOE ,Pune </b>",
  
 "CET",
  "CET stands for Common Entrance Test for engineering. It is a competitive exam conducted by various state-level and national-level authorities to provide admission to undergraduate engineering courses in various colleges and universities across India. </b>",
  
  "What is CET in engineering?",
  "CET stands for Common Entrance Test for engineering. It is a competitive exam conducted by various state-level and national-level authorities to provide admission to undergraduate engineering courses in various colleges and universities across India. </b>",
  
  "Eligiblity",
  "The eligibility criteria for CET vary from state to state, but in general, candidates who have completed their 10+2 education with Physics, Chemistry, and Mathematics as compulsory subjects are eligible to appear for the exam.</b>",

  "Who is eligible to take the CET exam for engineering?",
  "The eligibility criteria for CET vary from state to state, but in general, candidates who have completed their 10+2 education with Physics, Chemistry, and Mathematics as compulsory subjects are eligible to appear for the exam.</b>",

    "application process",
  "The application process for CET involves registering online on the official website of the exam conducting authority. Candidates need to provide their personal and educational details, upload their photograph and signature, and pay the application fee. The application process usually starts a few months before the exam date.</b>",

  "What is the application process for CET?",
  "The application process for CET involves registering online on the official website of the exam conducting authority. Candidates need to provide their personal and educational details, upload their photograph and signature, and pay the application fee. The application process usually starts a few months before the exam date.</b>",
  
  "application process for CET?",
  "The application process for CET involves registering online on the official website of the exam conducting authority. Candidates need to provide their personal and educational details, upload their photograph and signature, and pay the application fee. The application process usually starts a few months before the exam date.</b>",
  
"syllabus",
  "The syllabus for CET includes topics from Physics, Chemistry, and Mathematics that are covered in the 10+2 education. The level of difficulty and the weightage of each topic may vary depending on the state and the conducting authority.</b>",

  "What is the syllabus for CET?",
  "The syllabus for CET includes topics from Physics, Chemistry, and Mathematics that are covered in the 10+2 education. The level of difficulty and the weightage of each topic may vary depending on the state and the conducting authority.</b>",

  "syllabus for CET?",
  "The syllabus for CET includes topics from Physics, Chemistry, and Mathematics that are covered in the 10+2 education. The level of difficulty and the weightage of each topic may vary depending on the state and the conducting authority.</b>",
  
  "How is the CET exam conducted?",
  "The CET exam is usually conducted in an online mode (computer based) and has multiple-choice questions. The duration of the exam is typically 3 hours, and there is no negative marking for wrong answers like JEE and NEET entrance exams.</b>",

  "CET exam conducted?",
  "The CET exam is usually conducted in an online mode (computer based) and has multiple-choice questions. The duration of the exam is typically 3 hours, and there is no negative marking for wrong answers like JEE and NEET entrance exams.</b>",
  
  "selection process",
  "The selection process after CET involves counseling rounds based on the candidate's rank in the exam. Candidates need to register for counseling, and seats are allotted based on their preferences and availability.</b>",

  "What is the selection process after CET?",
  "The selection process after CET involves counseling rounds based on the candidate's rank in the exam. Candidates need to register for counseling, and seats are allotted based on their preferences and availability.</b>",

  "selection process after CET?",
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

  "Scholarship Site?",
  "Here is a link to the website: <a href='https://mahadbt.maharashtra.gov.in/login/login'>https://mahadbt.maharashtra.gov.in/login/login</a>"

  "list of minorities in maharashtra?",
  "In Maharashtra, the following communities are considered as minorities for the purpose of admission to engineering colleges through CET (Common Entrance Test): <br>Muslim <br>Christian <br>Sikh <br>Buddhist <br>Jain <br>Parsi <br>Other notified minorities (such as Jews) <br>These communities are eligible for minority quota seats in engineering colleges in Maharashtra. However, the exact number of seats and the admission criteria may vary from college to college.It's important to note that to be eligible for the minority quota, candidates must belong to the specific community and should provide valid proof of the same. Candidates can check with the individual colleges for more information on the admission process and the availability of minority quota seats.</b>", 
    
   "minorities in maharashtra cet?",
   "In Maharashtra, the following communities are considered as minorities for the purpose of admission to engineering colleges through CET (Common Entrance Test): <br>Muslim <br>Christian <br>Sikh <br>Buddhist <br>Jain <br>Parsi <br>Other notified minorities (such as Jews) <br>These communities are eligible for minority quota seats in engineering colleges in Maharashtra. However, the exact number of seats and the admission criteria may vary from college to college.It's important to note that to be eligible for the minority quota, candidates must belong to the specific community and should provide valid proof of the same. Candidates can check with the individual colleges for more information on the admission process and the availability of minority quota seats.</b>", 

   "list of engineering colleges in maharashtra through cet and their  cut off?",
   "The cut-off scores for engineering colleges in Maharashtra through CET (Common Entrance Test) vary from year to year depending on a variety of factors such as the number of applicants, the difficulty level of the exam, and the number of seats available. Here are the cut-off scores for some of the top engineering colleges in Maharashtra through CET in the previous year: <br> <br>1.College of Engineering, Pune (COEP) - 95.9 percentile <br>2.Veermata Jijabai Technological Institute (VJTI), Mumbai - 94.3 percentile <br>3.Sardar Patel College of Engineering (SPCE), Mumbai - 91.9 percentile <br>4.Institute of Chemical Technology (ICT), Mumbai - 89.7 percentile <br>4.Dwarkadas J. Sanghvi College of Engineering (DJ Sanghvi), Mumbai - 87.2 percentile <br>5.Thadomal Shahani Engineering College (TSEC), Mumbai - 85.6 percentile <br>6.Fr. Conceicao Rodrigues College of Engineering (CRCE), Mumbai - 83.7 percentile <br>7.Vishwakarma Institute of Technology (VIT), Pune - 82.6 percentile <br>8.Pimpri Chinchwad College of Engineering (PCCOE), Pune - 78.2 percentile <br>9.KJ Somaiya College of Engineering (KJSCE), Mumbai - 77.2 percentile <br> <br> Please note that these cut-off scores are for the previous year, and the actual cut-off scores may vary for the current year. Also, it's important to note that the cut-off scores may vary depending on the category of the candidate, such as General, SC, ST, OBC, etc. </b>",
   
    "Percentile Between 0 to 10?",
    " <b> Percentile Between 0 to 10: <br> If you have scored between 0 and 10 percentile in CET (Common Entrance Test) in Maharashtra, it may be very challenging to secure admission in most of the engineering colleges. However, there are still some engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> <br>1.Smt. Kashibai Navale Sinhgad College of Engineering, Pune <br>2.G. H. Raisoni College of Engineering, Nagpur <br>3.MIT Academy of Engineering, Pune <br>4.Saraswati Education Society's Group of Institutions, Nashik <br>5.JSPM's Rajarshi Shahu College of Engineering, Pune <br>6.Dr. J. J. Magdum College of Engineering, Kolhapur <br>7.MET's Institute of Engineering, Mumbai <br>8.Dr. DY Patil Institute of Technology, Pune <br>9.Pimpri Chinchwad College of Engineering, Pune <br>10.KIT's College of Engineering, Kolhapur <br> <br>It's important to note that admission to these colleges may be challenging as the competition may be high due to the limited number of seats available. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. Additionally, it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. </b>",
    
    "Percentile Between 11 to 20?",
    " <b> Percentile Between 11 to 20: <br> If you have scored between 11 and 20 percentile in CET (Common Entrance Test) in Maharashtra, it may be very challenging to secure admission in most of the engineering colleges. However, there are still some engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> <br>1.Shreeyash College of Engineering and Technology, Aurangabad <br>2.Genba Sopanrao Moze College of Engineering, Pune,  <br>3.MAEER's M.I.T. College of Engineering, Pune <br>4.All India Shri Shivaji Memorial Society's Institute of Information Technology, Pune <br>5.Kavikulguru Institute of Technology and Science, Nagpur <br>6.K. K. Wagh Institute of Engineering Education and Research, Nashik <br>7.Jaihind College of Engineering, Kuran <br>8.JSPM's RSCOE School of Engineering, Pune <br>9.RMD Sinhgad School of Engineering, Pune <br>10.Bharatiya Jain Sanghatana's Institute of Technology, Pune <br ><br>It's important to note that admission to these colleges may be challenging as the competition may be high due to the limited number of seats available. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. Additionally, it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. </b>",

    "Percentile Between 21 to 30?",
    " <b> Percentile Between 21 to 30: <br> If you have scored between 21 and 30 percentile in CET (Common Entrance Test) in Maharashtra, it may be very challenging to secure admission in most of the engineering colleges. However, there are still some engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> <br>1.KJEI's Trinity Academy of Engineering, Pune <br>2.N B Navale Sinhgad College of Engineering, Solapur  <br>3.Vidya Pratishthan's College of Engineering, Baramati <br>4.Jaihind College of Engineering, Kuran <br>5.JSPM's Imperial College of Engineering and Research, Pune <br>6.Bharatratna Indira Gandhi College of Engineering, Solapur <br>7.G H Raisoni Institute of Business Management, Jalgaon <br>8.Smt. Kashibai Navale Sinhgad School of Engineering, Pune <br>9.Dr. J.J. Magdum College of Engineering, Kolhapur <br>10.Priyadarshini Institute of Engineering and Technology, Nagpur <br> <br>It's important to note that admission to these colleges may be challenging as the competition may be high due to the limited number of seats available. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. Additionally, it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. </b>",

    "Percentile Between 31 to 40?",
    " <b> Percentile Between 31 to 40: <br> If you have scored between 31 and 40 percentile in CET (Common Entrance Test) in Maharashtra, it may be very challenging to secure admission in most of the engineering colleges. However, there are still some engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> <br>KJEI's Trinity Academy of Engineering, Pune <br>N B Navale Sinhgad College of Engineering, Solapur  <br>Vidya Pratishthan's College of Engineering, Baramati <br>Jaihind College of Engineering, Kuran <br>JSPM's Imperial College of Engineering and Research, Pune <br>Bharatratna Indira Gandhi College of Engineering, Solapur <br>G H Raisoni Institute of Business Management, Jalgaon <br>Smt. Kashibai Navale Sinhgad School of Engineering, Pune <br>Dr. J.J. Magdum College of Engineering, Kolhapur <br>Priyadarshini Institute of Engineering and Technology, Nagpur <br> <br>It's important to note that admission to these colleges may be challenging as the competition may be high due to the limited number of seats available. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. Additionally, it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. </b>",

    "Percentile Between 41 to 50?",
    " <b> Percentile Between 41 to 50: <br> If you have scored between 41 and 50 percentile in CET (Common Entrance Test) in Maharashtra, it may be very challenging to secure admission in most of the engineering colleges. However, there are still some engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> <br>Shri Ramdeobaba College of Engineering and Management, Nagpur <br>GH Raisoni College of Engineering, Nagpur <brPune Institute of Computer Technology (PICT), Pune<br>Pimpri Chinchwad College of Engineering (PCCOE), Pune <br>Dr DY Patil Institute of Engineering, Management and Research (DYPIEMR), Pune <br>D Y Patil College of Engineering and Technology, Kolhapur <br>Annasaheb Dange College of Engineering and Technology, Sangli <br>Sharad Institute of Technology, College of Engineering, Yadrav <br>Shreeyash College of Engineering and Technology, Aurangabad <br>Jaihind College of Engineering, Pune <br> <br>These colleges offer decent education and infrastructure, and have a good track record in terms of placements. However, the admission process and cut-off scores may vary for each college, and it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. </b>",

    "Percentile Between 51 to 60?",
    " <b> Percentile Between 51 to 60: <br> If you have scored between 51 and 60 percentile in CET (Common Entrance Test) in Maharashtra,there are still several engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> <br> Vidyalankar Institute of Technology (VIT), Mumbai <br>Maharashtra Academy of Engineering, Pune <br>Smt. Indira Gandhi College of Engineering, Navi Mumbai<br>Atharva College of Engineering, Mumbai <br>Saraswati College of Engineering, Mumbai <br>Bharatiya Vidya Bhavan's Sardar Patel Institute of Technology, Mumbai<br>K. J. Somaiya Polytechnic, Mumbai <br>K.C. College of Engineering and Management Studies and Research, Thane <br>Maharashtra Institute of Technology- Art Design and Technology University (MIT-ADT), Pune<br>Dhole Patil College of Engineering, Pune<br> <br>These colleges offer decent education and infrastructure, and have a good track record in terms of placements. However, the admission process and cut-off scores may vary for each college, and it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. </b>",

    "Percentile Between 61 to 70?",
    " <b> Percentile Between 61 to 70: <br> If you have scored between 61 and 70 percentile in CET (Common Entrance Test) in Maharashtra,there are still several engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> <br> Datta Meghe College of Engineering, Mumbai <br>All India Shri Shivaji Memorial Society's College of Engineering (AISSMS), Pune<br>Sinhgad College of Engineering, Pune<br>Marathwada Institute of Technology, Aurangabad<br>K. J. Somaiya College of Engineering and Information Technology, Mumbai <br>Bharati Vidyapeeth Deemed University College of Engineering, Pune<br>Jayawantrao Sawant College of Engineering, Pune <br>Rizvi College of Engineering, Mumbai<br>Vishwakarma Institute of Information Technology (VIIT), Pune<br>Sandip Institute of Technology and Research Centre, Nashik<br> <br>These colleges offer decent education and infrastructure, and have a good track record in terms of placements. However, the admission process and cut-off scores may vary for each college, and it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. </b>",

    "Percentile Between 71 to 80?",
    " <b> Percentile Between 71 to 80: <br> If you have scored between 71 and 80 percentile in CET (Common Entrance Test) in Maharashtra, there are still several engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> <br>Walchand College of Engineering, Sangli <br>Government College of Engineering, Amravati<br>Pune Institute of Computer Technology (PICT), Pune<br>Dr. D.Y. Patil Institute of Technology, Pune<br>Shri Ramdeobaba College of Engineering and Management (RCOEM), Nagpur<br>Cummins College of Engineering for Women, Pune<br>Sardar Patel Institute of Technology (SPIT), Mumbai<br>Terna Engineering College, Mumbai<br>Pillai College of Engineering, Mumbai<br>K. J. Somaiya Institute of Engineering and Information Technology, Mumbai<br> <br>These colleges have a good track record in terms of placements and research, and offer a wide range of courses and specializations. However, the admission process and cut-off scores may vary for each college, and it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. </b>",

    "Percentile Between 81 to 90?",
    " <b> Percentile Between 81 to 90: <br> If you have scored between 81 and 90 percentile in CET (Common Entrance Test) in Maharashtra, you have a good chance of getting admission to some of the well-known engineering colleges in the state. Here are some engineering colleges in Maharashtra that you may consider applying to: <br> <br>Maharashtra Institute of Technology (MIT), Pune <br>Vishwakarma Institute of Technology (VIT), Pune<br>Fr. Conceicao Rodrigues College of Engineering (CRCE), Mumbai<br>Don Bosco Institue of Technology, Mumbai<br>Dwarkadas J. Sanghvi College of Engineering (DJ Sanghvi), Mumbai<br>KJ Somaiya College of Engineering (KJSCE), Mumbai<br>Sardar Patel Institute of Technology (SPIT), Mumbai<br>Terna Engineering College, Mumbai<br>Thadomal Shahani Engineering College (TSEC), Mumbai<br>Army Institute of Technology, Pune<br> <br>These colleges have a good reputation, experienced faculty, and excellent campus facilities. However, the admission process and cut-off scores may vary for each college, and it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. </b>",

    "Percentile Between 91 to 100?",
    " <b> Percentile Between 91 to 100: <br> Congratulations on scoring more than 90 percentile in CET (Common Entrance Test) in Maharashtra! With such a high score, you have a good chance of getting admission to some of the top engineering colleges in Maharashtra. Here are some of the top engineering colleges in Maharashtra that you may consider applying to: <br> <br>College of Engineering, Pune (COEP) <br>Veermata Jijabai Technological Institute (VJTI), Mumbai<br>Sardar Patel College of Engineering (SPCE), Mumbai<br>Institute of Chemical Technology (ICT), Mumbai<br>Maharashtra Institute of Technology (MIT), Pune<br>Vishwakarma Institute of Technology (VIT), Pune<br>KJ Somaiya College of Engineering (KJSCE), Mumbai<br>Dwarkadas J. Sanghvi College of Engineering (DJ Sanghvi), Mumbai<br>Don Bosco College, Mumbai<br>Fr. Conceicao Rodrigues College of Engineering (CRCE), Mumbai<br> <br>These colleges have a good reputation, experienced faculty, and excellent campus facilities. However, the admission process and cut-off scores may vary for each college, and it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. </b>",


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
    
    "5",
    " <b> Engineering Colleges as per your CET Percentile: <br> <br> 5.1 Percentile Between 0 to 10  <br> <br> 5.2 Percentile Between 11 to 20 <br> <br> 5.3 Percentile Between 21 to 30  <br> <br> 5.4 Percentile Between 31 to 40 <br> <br> 5.5 Percentile Between 41 to 50 <br> <br> 5.6 Percentile Between 51 to 60 <br> <br>  5.7 Percentile Between 61 to 70 <br> <br>  5.8  Percentile Between 71 to 80 Percentile <br> <br>  5.9  Percentile Between 81 to 90 Percentile <br> <br>  5.10  Percentile Between 91 to 100 Percentile </b>",
    
    "5.1",
    " <b> Percentile Between 0 to 10: <br> If you have scored between 0 and 10 percentile in CET (Common Entrance Test) in Maharashtra, it may be very challenging to secure admission in most of the engineering colleges. However, there are still some engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> Smt. Kashibai Navale Sinhgad College of Engineering, Pune <br>G. H. Raisoni College of Engineering, Nagpur <br>MIT Academy of Engineering, Pune <br>Saraswati Education Society's Group of Institutions, Nashik <br>JSPM's Rajarshi Shahu College of Engineering, Pune <br>Dr. J. J. Magdum College of Engineering, Kolhapur <br>MET's Institute of Engineering, Mumbai <br>Dr. DY Patil Institute of Technology, Pune <br>Pimpri Chinchwad College of Engineering, Pune <br>KIT's College of Engineering, Kolhapur <br> <br>It's important to note that admission to these colleges may be challenging as the competition may be high due to the limited number of seats available. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. Additionally, it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. </b>",

    "5.2",
    " <b> Percentile Between 11 to 20: <br> If you have scored between 11 and 20 percentile in CET (Common Entrance Test) in Maharashtra, it may be very challenging to secure admission in most of the engineering colleges. However, there are still some engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> Shreeyash College of Engineering and Technology, Aurangabad <br>Genba Sopanrao Moze College of Engineering, Pune,  <br>MAEER's M.I.T. College of Engineering, Pune <br>All India Shri Shivaji Memorial Society's Institute of Information Technology, Pune <br>Kavikulguru Institute of Technology and Science, Nagpur <br>K. K. Wagh Institute of Engineering Education and Research, Nashik <br>Jaihind College of Engineering, Kuran <br>JSPM's RSCOE School of Engineering, Pune <br>RMD Sinhgad School of Engineering, Pune <br>Bharatiya Jain Sanghatana's Institute of Technology, Pune <br ><br>It's important to note that admission to these colleges may be challenging as the competition may be high due to the limited number of seats available. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. Additionally, it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. </b>",
    
    "5.3",
    " <b> Percentile Between 21 to 30: <br> If you have scored between 21 and 30 percentile in CET (Common Entrance Test) in Maharashtra, it may be very challenging to secure admission in most of the engineering colleges. However, there are still some engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> KJEI's Trinity Academy of Engineering, Pune <br>N B Navale Sinhgad College of Engineering, Solapur  <br>Vidya Pratishthan's College of Engineering, Baramati <br>Jaihind College of Engineering, Kuran <br>JSPM's Imperial College of Engineering and Research, Pune <br>Bharatratna Indira Gandhi College of Engineering, Solapur <br>G H Raisoni Institute of Business Management, Jalgaon <br>Smt. Kashibai Navale Sinhgad School of Engineering, Pune <br>Dr. J.J. Magdum College of Engineering, Kolhapur <br>Priyadarshini Institute of Engineering and Technology, Nagpur <br> <br>It's important to note that admission to these colleges may be challenging as the competition may be high due to the limited number of seats available. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. Additionally, it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. </b>",
    
    "5.4",
    " <b> Percentile Between 31 to 40: <br> If you have scored between 31 and 40 percentile in CET (Common Entrance Test) in Maharashtra, it may be very challenging to secure admission in most of the engineering colleges. However, there are still some engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> KJEI's Trinity Academy of Engineering, Pune <br>N B Navale Sinhgad College of Engineering, Solapur  <br>Vidya Pratishthan's College of Engineering, Baramati <br>Jaihind College of Engineering, Kuran <br>JSPM's Imperial College of Engineering and Research, Pune <br>Bharatratna Indira Gandhi College of Engineering, Solapur <br>G H Raisoni Institute of Business Management, Jalgaon <br>Smt. Kashibai Navale Sinhgad School of Engineering, Pune <br>Dr. J.J. Magdum College of Engineering, Kolhapur <br>Priyadarshini Institute of Engineering and Technology, Nagpur <br> <br>It's important to note that admission to these colleges may be challenging as the competition may be high due to the limited number of seats available. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. Additionally, it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. </b>",
    
    "5.5",
    " <b> Percentile Between 41 to 50: <br> If you have scored between 41 and 50 percentile in CET (Common Entrance Test) in Maharashtra, it may be very challenging to secure admission in most of the engineering colleges. However, there are still some engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> Shri Ramdeobaba College of Engineering and Management, Nagpur <br>GH Raisoni College of Engineering, Nagpur <brPune Institute of Computer Technology (PICT), Pune<br>Pimpri Chinchwad College of Engineering (PCCOE), Pune <br>Dr DY Patil Institute of Engineering, Management and Research (DYPIEMR), Pune <br>D Y Patil College of Engineering and Technology, Kolhapur <br>Annasaheb Dange College of Engineering and Technology, Sangli <br>Sharad Institute of Technology, College of Engineering, Yadrav <br>Shreeyash College of Engineering and Technology, Aurangabad <br>Jaihind College of Engineering, Pune <br> <br>These colleges offer decent education and infrastructure, and have a good track record in terms of placements. However, the admission process and cut-off scores may vary for each college, and it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. </b>",
    
    "5.6",
    " <b> Percentile Between 51 to 60: <br> If you have scored between 51 and 60 percentile in CET (Common Entrance Test) in Maharashtra,there are still several engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> Vidyalankar Institute of Technology (VIT), Mumbai <br>Maharashtra Academy of Engineering, Pune <br>Smt. Indira Gandhi College of Engineering, Navi Mumbai<br>Atharva College of Engineering, Mumbai <br>Saraswati College of Engineering, Mumbai <br>Bharatiya Vidya Bhavan's Sardar Patel Institute of Technology, Mumbai<br>K. J. Somaiya Polytechnic, Mumbai <br>K.C. College of Engineering and Management Studies and Research, Thane <br>Maharashtra Institute of Technology- Art Design and Technology University (MIT-ADT), Pune<br>Dhole Patil College of Engineering, Pune<br> <br>These colleges offer decent education and infrastructure, and have a good track record in terms of placements. However, the admission process and cut-off scores may vary for each college, and it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. </b>",

    "5.7",
    " <b> Percentile Between 61 to 70: <br> If you have scored between 61 and 70 percentile in CET (Common Entrance Test) in Maharashtra,there are still several engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br> Datta Meghe College of Engineering, Mumbai <br>All India Shri Shivaji Memorial Society's College of Engineering (AISSMS), Pune<br>Sinhgad College of Engineering, Pune<br>Marathwada Institute of Technology, Aurangabad<br>K. J. Somaiya College of Engineering and Information Technology, Mumbai <br>Bharati Vidyapeeth Deemed University College of Engineering, Pune<br>Jayawantrao Sawant College of Engineering, Pune <br>Rizvi College of Engineering, Mumbai<br>Vishwakarma Institute of Information Technology (VIIT), Pune<br>Sandip Institute of Technology and Research Centre, Nashik<br> <br>These colleges offer decent education and infrastructure, and have a good track record in terms of placements. However, the admission process and cut-off scores may vary for each college, and it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. </b>",

    "5.8",
    " <b> Percentile Between 71 to 80: <br> If you have scored between 71 and 80 percentile in CET (Common Entrance Test) in Maharashtra, there are still several engineering colleges that you can consider applying to. Here are some of the engineering colleges in Maharashtra that you may consider: <br>Walchand College of Engineering, Sangli <br>Government College of Engineering, Amravati<br>Pune Institute of Computer Technology (PICT), Pune<br>Dr. D.Y. Patil Institute of Technology, Pune<br>Shri Ramdeobaba College of Engineering and Management (RCOEM), Nagpur<br>Cummins College of Engineering for Women, Pune<br>Sardar Patel Institute of Technology (SPIT), Mumbai<br>Terna Engineering College, Mumbai<br>Pillai College of Engineering, Mumbai<br>K. J. Somaiya Institute of Engineering and Information Technology, Mumbai<br> <br>These colleges have a good track record in terms of placements and research, and offer a wide range of courses and specializations. However, the admission process and cut-off scores may vary for each college, and it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. </b>",

    "5.9",
    " <b> Percentile Between 81 to 90: <br> If you have scored between 81 and 90 percentile in CET (Common Entrance Test) in Maharashtra, you have a good chance of getting admission to some of the well-known engineering colleges in the state. Here are some engineering colleges in Maharashtra that you may consider applying to: <br>Maharashtra Institute of Technology (MIT), Pune <br>Vishwakarma Institute of Technology (VIT), Pune<br>Fr. Conceicao Rodrigues College of Engineering (CRCE), Mumbai<br>Don Bosco Institue of Technology, Mumbai<br>Dwarkadas J. Sanghvi College of Engineering (DJ Sanghvi), Mumbai<br>KJ Somaiya College of Engineering (KJSCE), Mumbai<br>Sardar Patel Institute of Technology (SPIT), Mumbai<br>Terna Engineering College, Mumbai<br>Thadomal Shahani Engineering College (TSEC), Mumbai<br>Army Institute of Technology, Pune<br> <br>These colleges have a good reputation, experienced faculty, and excellent campus facilities. However, the admission process and cut-off scores may vary for each college, and it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. </b>",

    "5.10",
    " <b> Percentile Between 91 to 100: <br> Congratulations on scoring more than 90 percentile in CET (Common Entrance Test) in Maharashtra! With such a high score, you have a good chance of getting admission to some of the top engineering colleges in Maharashtra. Here are some of the top engineering colleges in Maharashtra that you may consider applying to: <br>College of Engineering, Pune (COEP) <br>Veermata Jijabai Technological Institute (VJTI), Mumbai<br>Sardar Patel College of Engineering (SPCE), Mumbai<br>Institute of Chemical Technology (ICT), Mumbai<br>Maharashtra Institute of Technology (MIT), Pune<br>Vishwakarma Institute of Technology (VIT), Pune<br>KJ Somaiya College of Engineering (KJSCE), Mumbai<br>Dwarkadas J. Sanghvi College of Engineering (DJ Sanghvi), Mumbai<br>Don Bosco College, Mumbai<br>Fr. Conceicao Rodrigues College of Engineering (CRCE), Mumbai<br> <br>These colleges have a good reputation, experienced faculty, and excellent campus facilities. However, the admission process and cut-off scores may vary for each college, and it's important to check the individual college websites for more information on their admission criteria, eligibility, and cut-off scores. You should also consider factors such as location, cost, campus facilities, and placement opportunities before making your final decision. </b>",

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
        print("Bot: Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Scholarship related info </br> 4.Top Colleges</br> </br> 5.Engineering Colleges as per your CET Percentile </br>")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    bot_response = bot.get_response(userText)
    if float(bot_response.confidence) > 0.5:
        return str(bot_response)
    else:
        return "Sorry, I am not sure what you mean.Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Scholarship related info </br> 4.Top Colleges </br>  5.Engineering Colleges as per your CET Percentile </br>"
