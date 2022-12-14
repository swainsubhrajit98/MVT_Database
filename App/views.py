from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from django.db.models import Q
from App.models import *
def display_topic(request):
    LTO=Topic.objects.all()
    
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    LWO=Webpage.objects.all()
    LWO = Webpage.objects.filter(topic_name='Cricket')
    LWO = Webpage.objects.exclude(topic_name='Cricket')
    LWO = Webpage.objects.all()[2:5:]
    LWO = Webpage.objects.all().order_by('name')
    LWO = Webpage.objects.filter(topic_name='Cricket').order_by('-name')
    LWO = Webpage.objects.all().order_by(Length('name'))
    LWO = Webpage.objects.all().order_by(Length('name').desc())
    LWO = Webpage.objects.filter(name__startswith='m')
    LWO = Webpage.objects.filter(name__endswith='a')
    LWO = Webpage.objects.filter(name__contains='s')
    LWO = Webpage.objects.filter(name__in=('Sultan', 'ABD'))
    LWO = Webpage.objects.filter(name__regex='^S\w{5}')
    LWO = Webpage.objects.all()
    LWO = Webpage.objects.filter(Q(topic_name='Cricket') & Q(name__startswith='m'))
    LWO = Webpage.objects.all()
    LWO = Webpage.objects.filter(Q(topic_name='Football') | Q(url__endswith='in'))
    LWO=Webpage.objects.all()
    
    d={'LWO':LWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    # LARO=AccessRecords.objects.all()
    LARO = AccessRecords.objects.filter(date='1999-05-25')
    LARO = AccessRecords.objects.filter(date__year='1998')
    LARO = AccessRecords.objects.filter(date__month='06')
    LARO = AccessRecords.objects.filter(date__day='11')
    LARO = AccessRecords.objects.filter(date__gte='1999-05-25')
    LARO = AccessRecords.objects.filter(date__lte='1999-05-25')
    LARO = AccessRecords.objects.filter(date__year__gte='1999')
    LARO=AccessRecords.objects.all()
    
    d={'LARO':LARO}
    return render(request,'display_access.html',d)