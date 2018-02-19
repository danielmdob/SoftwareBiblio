from django.db import models
from RegisteredUser.models import RegisteredUser
# Create your models here.

class Administrator(RegisteredUser):
    class Meta:
            db_table = 'Administrator'