from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, template_name="home.html")
def apartment(request):
    return render(request, template_name="apartment.html")