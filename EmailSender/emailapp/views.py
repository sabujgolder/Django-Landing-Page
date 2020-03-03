from django.shortcuts import render
from EmailSender.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from . import forms

def form_process_view(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        name = request.POST.get('Name')
        subject = request.POST.get('Email')
        body = request.POST.get('Description')
        recepient = str('recipient mail')
        send_mail(subject,body,name,  [recepient], fail_silently = False)
        return render(request, 'emailapp/success.html', {'recepient': recepient})
    return render(request, 'emailapp/contact.html', {'form':sub})

def home(request):
        return render(request, 'emailapp/index.html')

def map(request):
        return render(request, 'emailapp/map.html')
