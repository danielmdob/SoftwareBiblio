from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def home(request):
    return render(request, '../templates/Admin/home.html')


def register(request):
    return render(request, '../templates/RegisteredUser/reader-register.html')

def finish_register(request):
    fullname = request.GET.get('fullname', None)
    cedula = request.GET.get('cedula', None)
    email = request.GET.get('email', None)
    address = request.GET.get('address', None)
    city = request.GET.get('city', None)
    print("%s %s %s %s %s" % (fullname, cedula, email, address, city))
    data = {
         'is_taken': "HOLA"
    }
    return JsonResponse(data)
