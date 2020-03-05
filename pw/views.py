# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import Messages
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def skills(request):
    return render(request, 'skills.html')

def contact(request):
    form=Messages()
    respond='Send Message'
    return render(request, 'contact.html',{'form':form,'respond':respond})

def message_sent(request):
    if request.method=="POST":
        data=Messages(request.POST)
        if data.is_valid():
            data.save()
            respond='Your Message has been sent successfully!'
            return render(request,'contact.html',{'data':data,'respond':respond,})
        else:
            data=Messages()
            respond='Your Message has been sent successfully!'
            return render(request,'contact.html',{'data':data,'respond':respond,})
