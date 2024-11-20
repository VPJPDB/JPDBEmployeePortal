from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def home(request):
    if request.user.is_authenticated:
        return render(request, 'training/home_logged_in.html')
    else:
        return render(request, 'training/home_logged_out.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegisterForm()
    return render(request, 'training/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'training/dashboard.html')

