from django.shortcuts import render_to_response
from django.template import RequestContext

from test_yarned_app.models import Person
from test_yarned_app.models import RequestSnapShot


def person_info(request):
    person = Person.objects.get(id=1)
    return render_to_response('main.html',
        context_instance=RequestContext(request, {'person': person}))


def requests_info(request):
    requests = RequestSnapShot.objects.all().order_by('-id')[0:10]
    return render_to_response('requests_info.html', {'requests': requests})
