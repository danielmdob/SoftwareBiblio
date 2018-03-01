from django.db import models
from django import forms


# Create your models here.

class User(models.Model):
    class Meta:
        db_table = "user"


class Anonymous(User):
    class Meta:
        db_table = 'anonymous'


class Image(models.Model):
    image = models.ImageField(upload_to='../images/ProfilePictures', blank=True)
    url = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "image"


class ProfilePicture(Image):
    class Meta:
        db_table = "profilePicture"


class BookCover(Image):
    class Meta:
        db_table = "bookCover"


class RegisteredUser(User):
    email = models.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    enabled = models.BooleanField
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    profilePicture = models.OneToOneField(ProfilePicture, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'registeredUser'


class Administrator(RegisteredUser):
    class Meta:
        db_table = 'administrator'


class Genre(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'genre'


class Serie(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'serie'


class Author(models.Model):
    normalizedName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20)

    class Meta:
        db_table = 'author'


class Book(models.Model):
    title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20)
    ISSN = models.CharField(max_length=20)
    series = models.ForeignKey(Serie, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField
    signature = models.CharField(max_length=50)
    pages = models.IntegerField
    publisher = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    genres = models.ManyToManyField(Genre)
    authors = models.ManyToManyField(Author)
    cover = models.OneToOneField(BookCover, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'book'


class Review(models.Model):
    text = models.CharField(max_length=1000)
    reviewer = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'


class Loan(models.Model):
    loanDate = models.DateTimeField
    returnDate = models.DateTimeField
    feeTime = models.DateTimeField
    fee = models.FloatField
    admin = models.ForeignKey(Administrator, on_delete=models.SET_NULL, null=True, related_name='admin')
    feePerBook = models.FloatField
    reader = models.ForeignKey(RegisteredUser, on_delete=models.SET_NULL, null=True, related_name='reader')

    class Meta:
        db_table = 'loan'


class Copy(models.Model):
    copyNumber = models.IntegerField
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'copy'
