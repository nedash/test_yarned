from django.forms import ModelForm, TextInput
from django.forms.models import inlineformset_factory
from django.conf import settings

from test_yarned_app.models import Person, Contact


class CalendarWidget(TextInput):
    class Media:
        js = (
              settings.MEDIA_URL + 'js/jquery-1.5.js',
              settings.MEDIA_URL + 'js/jquery-ui-1.8.10.custom.min.js',
              settings.MEDIA_URL + 'js/ext/jsdate.js',
        )
        css = {
              'all': (
                   settings.MEDIA_URL +
                       'css/jquery-ui/jquery-ui-1.8.10.custom.css',
              )
        }

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(attrs={'class': 'datepicker'})


class RersonInfoForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'bio', 'birthdate']
        widgets = {
            'birthdate': CalendarWidget()
        }


ContactFormSet = inlineformset_factory(Person, Contact)
