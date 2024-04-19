from django.urls import path
from .views import *

urlpatterns = [
    path('', mainpage),
    path('analyse/', analyse),
    path('story/', story),
    path('arts/', arts),

]

