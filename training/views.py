from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

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

# Static file debugging view (Optional: For diagnosing static file issues)
def static_debug_view(request):
    """Lists static files for debugging purposes."""
    import os
    from django.conf import settings
    static_dir = settings.STATIC_ROOT
    files = []
    for root, dirs, filenames in os.walk(static_dir):
        for filename in filenames:
            files.append(os.path.relpath(os.path.join(root, filename), static_dir))
    return render(request, 'training/static_debug.html', {'files': files})
