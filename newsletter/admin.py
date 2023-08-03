# app_name/admin.py

from django.contrib import admin
from .models import EmailSubscriber

# Register the EmailSubscriber model with the admin site
admin.site.register(EmailSubscriber)
