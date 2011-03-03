from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.contrib.admin.widgets import AdminDateWidget
from django.conf import settings

from test_yarned_app.models import Person, Contact


class RersonInfoForm(ModelForm):
    class Media:
        css = {
            'all': (
                settings.ADMIN_MEDIA_PREFIX + 'css/widgets.css',
                )
        }
        js = (
              settings.ADMIN_MEDIA_PREFIX + "js/calendar.js",
              settings.ADMIN_MEDIA_PREFIX + "js/admin/DateTimeShortcuts.js",
        )

    class Meta:
        model = Person
        fields = ['name', 'surname', 'bio', 'birthdate']
        widgets = {
            'birthdate': AdminDateWidget()
        }


ContactFormSet = inlineformset_factory(Person, Contact)
