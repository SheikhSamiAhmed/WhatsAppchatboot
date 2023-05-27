from django.urls import path
from chatbot_app import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('generate_otp/', views.generate_otp, name='generate_otp'),
    
]
