from django.db import models

class MainPage(models.Model):
    text = models.TextField(blank=True)
    image = models.ImageField()

class Analyse(models.Model):
    text = models.TextField(blank=True)
    image = models.ImageField()

class Story(models.Model):
    text = models.TextField(blank=True)
    image = models.ImageField()

class Arts(models.Model):
    text = models.TextField(blank=True)
    image = models.ImageField()
