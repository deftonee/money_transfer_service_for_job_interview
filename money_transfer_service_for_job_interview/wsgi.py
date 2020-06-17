import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'money_transfer_service_for_job_interview.settings')

application = get_wsgi_application()
