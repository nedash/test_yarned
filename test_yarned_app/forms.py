from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from test_yarned_app.models import Person, Contact


class RersonInfoForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'bio', 'birthdate']


ContactFormSet = inlineformset_factory(Person, Contact)
