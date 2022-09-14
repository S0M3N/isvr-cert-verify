from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
from django.template.loader import render_to_string



# Create your views here.
def home(request):
    return render(request, 'index.html')

def cert_check(request, slug):
    try:
        std = Certificate.objects.filter(slug = slug)[0]
        return render(request, 'cert.html', {'std':std})
    except:
        std = {
            "student_name" : "No certificate found",
            "student_id" : "None",
            "cert_number" : None,
            "cert_created" : "Certificate ID is invalid",
            "course" : "-",
            "slug" : "nocertificate",
            "gdrive_id" : "1O0EVKgJOKO_Y4MYlz_eKuufdbcSKFsO7",
        }
        return render(request, 'cert.html', {'std':std})

def search_cert(request):
    query = request.GET['cert_id']
    return cert_check(request=request,slug=query.lower())

def contact(request):
    if request.method == "POST":
        first_name = request.POST['name']
        last_name = request.POST['surname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        val = Message(first_name = first_name, last_name = last_name, email = email, subject = subject, message = message)
        val.save()
    return render(request, 'index.html')
