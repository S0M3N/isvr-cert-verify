import re
from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def course(request, slug):
    std = Course.objects.filter(slug = slug)[0]
    return render(request, 'course/course.html', {'std':std})