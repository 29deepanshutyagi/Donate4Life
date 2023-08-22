from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from patient.models import Patient
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import Group, User

# Get all groups in the Django admin



def first(request):
    return render(request,'first.html')

def patient(request):
    if request.method == "POST":
        name = request.POST['name']
        birthofdate = request.POST['birthofdate']
        email = request.POST['email']
        mobilenumber = request.POST['mobilenumber']
        gender = request.POST['gender']
        occupation = request.POST['occupation']
        IDtype = request.POST['IDtype']
        IDnumber = request.POST['IDnumber']
        expirydate = request.POST['expirydate']
        PermanentorTemporary = request.POST['PermanentorTemporary']
        state=request.POST['state']
        district = request.POST['district']
        father = request.POST['father']
        mother = request.POST['mother']
        grandfather = request.POST['grandfather']
        bloodgroup = request.POST['bloodgroup']

        patient = Patient(
            name=name,
            birthofdate=birthofdate,
            email=email,
            mobilenumber=mobilenumber,
            gender=gender,
            occupation=occupation,
            IDtype=IDtype,
            IDnumber=IDnumber,
            expirydate=expirydate,
            PermanentorTemporary=PermanentorTemporary,
            state=state,
            district=district,
            father=father,
            mother=mother,
            grandfather=grandfather,
            bloodgroup=bloodgroup,
        )
        patient.save()
        messages.success(request, "your detail has bent sent!")
        plaintext = get_template('emailpatient.txt')
        htmly     = get_template('emailpatient.html')

        d = { 'name': name,'birthofdate':birthofdate,'email':email,'mobilenumber':mobilenumber,'gender':gender}
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives('Application', text_content, settings.EMAIL_HOST_USER, [email])
        # send_mail(
        #     'Application',
        #     f'Application from {name}',
        #     settings.EMAIL_HOST_USER,
        #     [email],
        # )
        
        msg.attach_alternative(html_content, "text/html")
        msg.send()
                   
    return render(request, 'patient.html')