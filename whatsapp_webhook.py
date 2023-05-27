from twilio.twiml.messaging_response import MessagingResponse
from django.conf import settings
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application
import os

from twilio.rest import Client
from django.conf import settings


def send_whatsapp_message(to, body):
    client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=body,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=to
    )

    return message.sid



def handle_incoming_message(request):
    msg_body = request.values.get('Body', None)
    sender_number = request.values.get('From', None)

    response = MessagingResponse()

    if msg_body == 'register':
        response.message('Please provide your name and phone number in the format: NAME, PHONE_NUMBER')
    elif ',' in msg_body:
        name, phone_number = msg_body.split(',')
        data = {'name': name.strip(), 'phone_number': phone_number.strip()}
        
        request.POST = data
        response_text = call_command('register_user', verbosity=0)
        
        # Send the response as a WhatsApp message
        response.message(response_text)
    elif msg_body == 'generate otp':
        data = {'phone_number': sender_number}
        
        request.POST = data
        response_text = call_command('generate_otp', verbosity=0)
        
        # Send the response as a WhatsApp message
        response.message(response_text)
    else:
        response.message('Invalid command!')
    
    return HttpResponse(str(response))

if __name__ == '__main__':
    from django.core.wsgi import get_wsgi_application
    from django.conf import settings
    import os

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_project.settings')
    application = get_wsgi_application()