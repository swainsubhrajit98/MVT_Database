from django.shortcuts import render

# Create your views here.
from App.models import *
def display_topics(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)

def display_access(request):
    LARO=AccessRecords.objects.all()
    d={'LARO':LARO}
    return render(request,'display_access.html',d)