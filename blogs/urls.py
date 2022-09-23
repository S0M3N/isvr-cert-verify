from django.urls import path
from .views import *
from home.views import *

urlpatterns = [
    path('', home, name='home'),
    path('apply/', apply, name='home'),
    path('<slug:slug>/', course, name='course'),
]