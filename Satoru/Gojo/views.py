from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

menu = ["Analyse", "Story", "Arts"]

def mainpage(request):
    #posts = MainPage.objects.all()
    #return render(request, 'Gojo/mainpage.html', {'posts' = posts})

def analyse(request):
    return render(request, 'Gojo/analyse.html')

def story(request):
    return render(request, 'Gojo/story.html')

def arts(request):
    return render(request, 'Gojo/arts.html')

