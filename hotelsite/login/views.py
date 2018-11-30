from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm

# def log_in(request):
#     return render(request, 'sign_in/index.html')

def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('/staff/')
        else:
            return render(request, 'sign_in/index.html')
    else:
        form = LoginForm()
        return render(request, 'sign_in/index.html', {'form':form})
            