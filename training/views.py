from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.http import HttpResponse
from .forms import HRReportForm, SafetySurveyForm, CheckInForm, TrainingFollowUpForm

# Logout view
def logout_view(request):
    """Logs the user out and redirects to the login page."""
    logout(request)
    return redirect('login')

# Home view (conditionally renders based on authentication)
def home(request):
    """Renders the home page based on user authentication status."""
    if request.user.is_authenticated:
        return render(request, 'training/home_logged_in.html')
    else:
        return render(request, 'training/home_logged_out.html')

# Handbook view
def handbook(request):
    """Renders the employee handbook page."""
    return render(request, 'training/handbook.html')

# Login view
def login_view(request):
    """Handles user login and redirects to the dashboard upon success."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after login
    else:
        form = AuthenticationForm()
    return render(request, 'training/login.html', {'form': form})

# Dashboard view
@login_required
def dashboard_view(request):
    """Renders the dashboard page, accessible only to logged-in users."""
    return render(request, 'training/dashboard.html')

# Static file debugging view
def static_debug_view(request):
    """Lists all collected static files for debugging purposes."""
    static_dir = settings.STATIC_ROOT
    if not os.path.exists(static_dir):
        return HttpResponse("Static files directory does not exist. Run collectstatic first.")
    
    files = []
    for root, dirs, filenames in os.walk(static_dir):
        for filename in filenames:
            files.append(os.path.relpath(os.path.join(root, filename), static_dir))
    return HttpResponse('<br>'.join(files))

# HR Report view
@login_required
def hr_report_view(request):
    """Handles HR report form submission."""
    if request.method == 'POST':
        form = HRReportForm(request.POST)
        if form.is_valid():
            # Process the form data
            return redirect('dashboard')
    else:
        form = HRReportForm()
    return render(request, 'training/hr_report.html', {'form': form})

# Safety Survey view
@login_required
def safety_survey_view(request):
    """Handles safety survey form submission."""
    if request.method == 'POST':
        form = SafetySurveyForm(request.POST)
        if form.is_valid():
            # Process the form data
            return redirect('dashboard')
    else:
        form = SafetySurveyForm()
    return render(request, 'training/safety_survey.html', {'form': form})

# Check-In view
@login_required
def check_in_view(request):
    """Handles check-in form submission."""
    if request.method == 'POST':
        form = CheckInForm(request.POST)
        if form.is_valid():
            # Process the form data
            return redirect('dashboard')
    else:
        form = CheckInForm()
    return render(request, 'training/check_in.html', {'form': form})

# Training Follow-Up view
@login_required
def training_follow_up_view(request):
    """Handles training follow-up form submission."""
    if request.method == 'POST':
        form = TrainingFollowUpForm(request.POST)
        if form.is_valid():
            # Process the form data
            return redirect('dashboard')
    else:
        form = TrainingFollowUpForm()
    return render(request, 'training/training_follow_up.html', {'form': form})
