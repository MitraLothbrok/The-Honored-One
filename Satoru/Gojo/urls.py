from django.urls import path
from .views import *

urlpatterns = [
    path('', mainpage, name='home'),
    path('analyse/', analyse, name='analyse'),
    path('story/', story, name='story'),
    path('arts/', arts, name='arts'),

]

