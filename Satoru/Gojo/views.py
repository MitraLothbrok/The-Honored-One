from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def mainpage(request):
    return render(request, 'Gojo/mainpage.html')

def analyse(request):
    return render(request, 'Gojo/analyse.html')

def story(request):
    return render(request, 'Gojo/story.html')

def arts(request):
    return render(request, 'Gojo/arts.html')

def abilities(request):
    return render(request, 'Gojo/abilities.html')

