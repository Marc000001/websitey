import django_filters

from staff.models import Patient
from .models import *

class Filter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields =['name','description', 'number', 'time', 'ward', 'symptoms', 'Admitted']

