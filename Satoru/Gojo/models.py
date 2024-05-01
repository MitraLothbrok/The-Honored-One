from django.db import models

class MainPage(models.Model):
    image = models.ImageField()

class Analyse(models.Model):
    image = models.ImageField()

class Story(models.Model):
    image = models.ImageField()

class Arts(models.Model):
    image = models.ImageField()
