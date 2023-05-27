
whatsapp chatbot using python django and flask
==================================================
Install necessary modules
==========================
 pip install twilio --user
 
 pip install flask --user
 
 pip install django --user
 
 pip install pyngrok --user
 
 
STEPS:-
=======

-> Set up a Django project and run  database migratopm by running: 
    python manage.py migrate
    
-> Create the necessary Django models

-> Set up the Django views

-> Configure the URL routing


-> Configure Twilio for WhatsApp integration 
============================================
Sign up for a Twilio account (if you don't have one) and obtain your account SID and authentication token.

Set up a new WhatsApp Sandbox in your Twilio account and note the assigned sandbox phone number.

-> Add SSID, auth and number in settings.py 

-> Create a Twilio webhook to receive WhatsApp messages

->  set up ngrox to create a secure tunnel to your localhost

Start the development server
============================
python manage.py runserver

browse this url: http://127.0.0.1:8000/

Start the Twilio webhook server
=============================
python whatsapp_webhook.py
browse this url: https://sami1234.ngrok.io/webhook

