from django.http import HttpResponse
from django.shortcuts import render_to_response

from test_yarned_app.models import *

def personInfo(request):
     person = Person.objects.get(id=1)
     contacts = list(Contact.objects.filter(person=person))
     return render_to_response('main.html', {'person' : person, 'contacts' : contacts })

def requestsInfo(request):
     requests = RequestSnapShot.objects.all().order_by('-id')[0:10]
     return render_to_response('requests_info.html', {'requests': requests})
