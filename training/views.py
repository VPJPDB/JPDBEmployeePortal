from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm  # Import RegisterForm correctly

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirects to the login page after logging out

def home(request):
    if request.user.is_authenticated:
        return render(request, 'training/home_logged_in.html')
    else:
        return render(request, 'training/home_logged_out.html')

def handbook(request):
    return render(request, 'training/handbook.html')  # Ensure this template exists

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'training/login.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'training/dashboard.html')
