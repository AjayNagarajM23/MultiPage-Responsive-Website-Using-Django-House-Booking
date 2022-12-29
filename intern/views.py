from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from VivekInternShip import settings
from intern.models import PostHouse


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    return render(request, 'book.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        query = request.POST['query']
        content = request.POST['content']

        subject = "From : " + name + " :" + query
        message = content
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['vnr177@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, "Mail sent Successfully")
        return redirect('index')
    return render(request, 'contact.html')


def postadd(request):
    if request.method == 'POST':
        name = request.POST['name']
        phno = request.POST['phno']
        housename = request.POST['housename']
        houseno = request.POST['houseno']
        housephoto = request.FILES['photo']
        houseadd = request.POST['houseadd']
        aboutHouse = request.POST['abouthouse']

        add_info = PostHouse(name=name, phno=phno, housename=housename,
                           houseno=houseno, houseimg=housephoto, houseaddr=houseadd,
                           description=aboutHouse)
        add_info.save()
        messages.success(request, "New Add Added")
        return redirect('showadd')
    return render(request, 'postadd.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, username + " Successfully Logged In")
            return redirect('index')
        else:
            messages.error(request, "Bad credentials ( Wrong Username Or Password )")
            return redirect('signin')
    return render(request, 'signin.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['mail']
        password = request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request, "Username Already Exists")
            return redirect('signup')
        if User.objects.filter(email=email):
            messages.error(request, "Email Already Exists")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, password)

        myuser.save()
        messages.success(request, "Your account has successfully Created, Please Login To Continue")
        return render(request, 'signin.html')

    return render(request, 'signup.html')


def signout(request):
    logout(request)
    messages.success(request, " Logged out Successfully ")
    return redirect('index')


def showadd(request):
    add = PostHouse.objects.all()
    return render(request, 'showadd.html', {'add': add})
