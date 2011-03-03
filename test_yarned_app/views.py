from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from test_yarned_app.models import Person, RequestSnapShot
from test_yarned_app.forms import RersonInfoForm

from test_yarned_app.forms import ContactFormSet


def person_info(request):
    person = Person.objects.get(id=1)
    return render_to_response('main.html',
        context_instance=RequestContext(request, {'person': person}))


def requests_info(request):
    requests = RequestSnapShot.objects.all().order_by('-id')[0:10]
    return render_to_response('requests_info.html', {'requests': requests})


@login_required
def person_info_edit(request):
    person = Person.objects.get(id=1)

    if request.method == 'POST':
        form = RersonInfoForm(request.POST, instance=person)
        contacts = ContactFormSet(request.POST, instance=person)
        if form.is_valid():
            form.save()
            if contacts.is_valid():
                contacts.save()
    else:
        form = RersonInfoForm(instance=person, label_suffix=':')
        contacts = ContactFormSet(instance=person)
    return render_to_response("person_info_edit.html", locals(),
        context_instance=RequestContext(request))
