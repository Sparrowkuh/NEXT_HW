from django.shortcuts import render, redirect
from .models import Article
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def income(request):
    return render(request, 'income.html')

def SNS(request):
    return render(request, 'SNS.html')

