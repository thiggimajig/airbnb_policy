web: gunicorn --max-requests 1000 --max-requests-jitter 50 airbnb_project.wsgi
release: python manage.py migrate