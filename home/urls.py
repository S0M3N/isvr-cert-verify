from django.urls import path
from .views import *

urlpatterns = [
    path('',  home, name='home'),
    path('cert/<slug:slug>/', cert_check, name='cert_check'),
    path('search', search_cert, name='search_certs'),
    path('contact', contact, name='contact'),
]
