from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.http import HttpResponse

from test_yarned_app.models import Person, RequestSnapShot, OperationLog
from test_yarned_app.forms import RersonInfoForm, ContactFormSet


def person_info(request):
    person = Person.objects.get(id=1)
    return render_to_response('main.html',
        context_instance=RequestContext(request, {'person': person}))


def requests_info(request):
    requests = RequestSnapShot.objects.all().order_by('-id')[0:10]
    return render_to_response('requests_info.html', {'requests': requests})


def operation_log(request):
    log = OperationLog.objects.all().order_by('-id')[0:10]
    return render_to_response('operation_log.html',
        context_instance=RequestContext(request, {'log': log}))


@login_required
def person_info_edit(request):
    person = Person.objects.get(id=1)

    if request.method == 'POST':
        form = RersonInfoForm(request.POST, instance=person)
        contacts = ContactFormSet(request.POST, instance=person)
        status = 'ERROR'
        errors = []

        if form.is_valid():
            form.save()
            if contacts.is_valid():
                contacts.save()
                status = 'OK'
            else:
                errors = contacts.errors.items()
        else:
            errors = form.errors.items()
        return HttpResponse(simplejson.dumps(
            {'status': status, 'errors': errors, }),
            mimetype='application/javascript')
    else:
        form = RersonInfoForm(instance=person)
        form.fields.keyOrder.reverse()
        contacts = ContactFormSet(instance=person)
    return render_to_response("person_info_edit.html", locals(),
        context_instance=RequestContext(request))
