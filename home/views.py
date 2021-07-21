from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# password for the test user is --> Kunal%%%***000
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")

def loginUser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Check if user has entered the correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, "login.html")

    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")

def signupUser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user_obj = User(username=username, email=email, password=password)
        user_obj.set_password(password)
        user_obj.save()
        login(request, user_obj)
        return redirect('/')
    return render(request, 'signup.html')