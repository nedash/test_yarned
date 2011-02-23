from django.http import HttpResponse
from django.shortcuts import render_to_response

from test_yarned_app.models import User
from test_yarned_app.models import Contact

def userInfo(request):
     user = User.objects.get(id=1)
     contacts = list(Contact.objects.filter(userId=1))
     return render_to_response('main.html', {'user' : user, 'contacts' : contacts })
