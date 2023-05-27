from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    is_registered = models.BooleanField(default=False)
    otp_code = models.CharField(max_length=6, blank=True, null=True)