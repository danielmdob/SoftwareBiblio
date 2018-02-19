from django.db import models
from SoftwareBiblio.models import User
# Create your models here.

class Anonymous(User):
    class Meta:
            db_table = 'Anonymous'

