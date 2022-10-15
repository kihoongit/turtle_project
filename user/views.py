from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login1

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       passwordcheck = request.POST.get('passwordcheck')
       if password == passwordcheck:
        print(username,password)
        User.objects.create_user(username=username, password=password)

        return redirect('user:login')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login1(request,user)
            print("로그인성공")
            return redirect('user:index')
        else:
            print("로그인실패")
            return redirect('user:login')

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')



