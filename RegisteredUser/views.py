from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from SoftwareBiblio.models import UnregisteredUser, RegisteredUser, Administrator
from django.contrib.auth.views import login


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
    phone = request.GET.get('phone', None)
    # print("%s %s %s %s %s %s" % (fullname, cedula, email, address, city, phone))
    # hacer el registro a la base de datos
    try:
        user = UnregisteredUser.objects.get(email=email)
        dashboard = 1  # admin dashboard
        admin = Administrator(email=email, fullname=fullname, cedula=cedula, address=address, city=city, phone=phone)
        #  admin.save()
    except UnregisteredUser.DoesNotExist:
        dashboard = 0  # reader dashboard
        registered_user = RegisteredUser(email=email, fullname=fullname, cedula=cedula, address=address, city=city,
                                         phone=phone)
        # registered_user.save()
    data = {'dashboard': dashboard}
    return JsonResponse(data)


def reader_dashboard(request):
    return render(request, '../templates/RegisteredUser/reader-book.html')
