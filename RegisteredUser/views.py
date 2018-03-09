from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, '../templates/Admin/home.html')


def register(request):
    return render(request, '../templates/RegisteredUser/reader-register.html')
