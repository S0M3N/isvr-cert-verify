from django.shortcuts import render
from .models import *
from django.contrib import messages


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
    if request.method =="POST":
        try:
            messages.success(request, 'Message send successfully, we will connect to you soon')
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            contact = request.POST['contact']
            subject = request.POST['subject']
            message = request.POST['message']
            val = Message(first_name = fname, last_name = lname, email = email, phone = contact, subject = subject, message = message)
            val.save()
        except:
            messages.error(request, 'Some error happened, please try again later.')
    return render(request, 'contact.html')
