from django.db import models
from RegisteredUser.models import RegisteredUser
from Admin.models import Administrator
# Create your models here.

class User(models.model):

    class Meta:
            db_table = "user"

class Genre(models.model):
    name = models.CharField(max_length=50)

    class Meta:
            db_table = 'genre'

class Serie(models.model):
    name = models.CharField(max_length=50)

    class Meta:
            db_table = 'serie'

class Author(models.model):
    normalizedName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20)

    class Meta:
            db_table = 'author'

class Book(models.model):
    title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20)
    ISSN = models.CharField(max_length=20)
    series = models.ForeignKey(Serie)
    year = models.IntegerField
    signature = models.CharField(max_length=50)
    pages = models.IntegerField
    publisher = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    genres = models.ManyToManyField(Genre)
    authors = models.ManyToManyField(Author)

    class Meta:
            db_table = 'book'

class Review(models.model):
    text = models.CharField(max_length=1000)
    reviewer = models.ForeignKey(RegisteredUser)
    book = models.ForeignKey(Book)

    class Meta:
            db_table = 'review'

class Copy(models.model):
    copyNumber = models.IntegerField
    book = models.ForeignKey(Book)
    loan = models.ForeignKey(Loan)

    class Meta:
            db_table = 'copy'

class Loan(models.model):
    loanDate = models.DateTimeField
    returnDate = models.DateTimeField
    feeTime = models.DateTimeField
    fee = models.FloatField
    admin = models.ForeignKey(Administrator)
    feePerBook = models.FloatField
    reader = models.ForeignKey(RegisteredUser)

    class Meta:
            db_table = 'loan'
