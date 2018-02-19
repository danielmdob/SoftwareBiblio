from django.db import models
from django import forms
# Create your models here.
from SoftwareBiblio.models import User

class RegisteredUser(User):
    email =  models.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    enabled = models.BooleanField
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)

    class Meta:
        db_table = 'registeredUser'