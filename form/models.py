from django.db import models
import os
from uuid import uuid4

def get_default_passport():
    return os.path.join('passports', 'default.jpg')  # or whatever default path makes sense

class Member(models.Model):
    full_name = models.CharField(max_length=200)
    state_of_origin = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    membership_no = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20, blank=False, null=True, verbose_name="Phone Number")  # Added verbose_name
    passport_photo = models.ImageField(
        upload_to='passports/',
        default=get_default_passport
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} ({self.membership_no})"