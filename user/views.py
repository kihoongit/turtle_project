from django.shortcuts import render
from .models import User

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

        return render(request, 'signup.html')


