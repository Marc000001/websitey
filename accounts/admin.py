from django.contrib import admin
from django.contrib.auth import get_user_model

# from .models import Patient

User = get_user_model()
admin.site.register(User)
# admin.site.register(Patient)
# Register your models here.
