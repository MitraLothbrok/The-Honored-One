from django.contrib import admin
from django.urls import path, include
from Gojo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Gojo.urls'))
]


