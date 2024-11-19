from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def home(request):
    # Show login/register links if the user is not logged in, or dashboard/logout if they are.
    if request.user.is_authenticated:
        return HttpResponse("Welcome to the HR Training Portal! <a href='/dashboard/'>Go to Dashboard</a> | <a href='/logout/'>Logout</a>")
    else:
        return HttpResponse("Welcome to the HR Training Portal! <a href='/login/'>Login</a> | <a href='/register/'>Register</a>")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegisterForm()
    return render(request, 'training/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'training/dashboard.html')

