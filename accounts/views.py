from django.shortcuts import redirect, render

def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def dashboard(request):
    return redirect ('index')

def logout(request):
    return render(request, 'accounts/logout.html')

