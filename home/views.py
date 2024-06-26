from django.shortcuts import render

from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required




#homepage

def home(request):

    return render(request, 'index.html')
    

def about(request):

    return render(request, 'about.html')

#Register


def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")

    context = {'form':form}

    return render(request, 'register.html', context=context)


# Log in a user
def user_login(request):
    form = LoginForm()

    if request.method == "POST":
        
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password') 

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")
    
    context = {'form':form}

    return render(request, 'login.html', context=context)


    
# Dashboard
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')



# User Logout 

def logout(request):

    auth.logout(request)

    return redirect ("login")