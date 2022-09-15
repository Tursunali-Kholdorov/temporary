web: gunicorn --workers 16 --threads 32 --worker-class=gevent --max-requests 5000 --max-requests-jitter 700 --timeout 140 config.wsgi:application
release: python manage.py migrate --noinput
