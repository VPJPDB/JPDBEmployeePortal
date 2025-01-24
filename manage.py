#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hr_training_site.settings')

    # Check if running in Render environment
    if 'RENDER' in os.environ:
        port = os.environ.get('PORT', '8000')  # Use the PORT environment variable or default to 8000
        os.system(f"python manage.py runserver 0.0.0.0:{port}")
    else:
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)

    # Run migrations
    os.system("python manage.py migrate")

    # Stop and restart the server after making changes to settings.py
    os.system("python manage.py runserver --noreload")
    os.system("python manage.py runserver")
    

if __name__ == '__main__':
    main()
