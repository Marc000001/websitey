from django.contrib import admin
from .models import Patient, Note
# Register your models here.

admin.site.register(Patient)
admin.site.register(Note)

