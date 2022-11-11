from django.shortcuts import render
from .models import Personal
# Create your views here.
from django.views.generic import DetailView


# class PersonalDetailView(DetailView):
#     queryset = Personal.objects.all()
#     print (queryset)
#     template_name = "detail.html"
