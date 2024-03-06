from django.shortcuts import render,redirect
from .models import EmergencyAlert
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here
def create_emergency_alert(request):
    if request.method == 'POST':
        user = request.user
        message = request.POST.get('emergency_message')
        EmergencyAlert.objects.create(request,user=user, message=message)
        # Additional logic or redirection as needed

    return render(request,'create_emergency_alert.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')  # Replace 'dashboard' with your desired dashboard page name
        else:
            messages.error(request,'Invalid username or password.')

    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')
