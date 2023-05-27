from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from .models import User
from random import randint

def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        
        user, created = User.objects.get_or_create(phone_number=phone_number)
        user.name = name
        user.is_registered = True
        user.otp_code = str(randint(100000, 999999))
        user.save()
        
        return HttpResponse('User registered successfully!')

def generate_otp(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        
        try:
            user = User.objects.get(phone_number=phone_number)
            if user.is_registered:
                user.otp_code = str(randint(100000, 999999))
                user.save()
                return HttpResponse('OTP code generated successfully!')
            else:
                return HttpResponse('User not registered!')
        except User.DoesNotExist:
            return HttpResponse('User not found!')
