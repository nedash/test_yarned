from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def edit_object(ref):
    return reverse('admin:%s_%s_change' %
        (ref._meta.app_label, ref._meta.module_name), args=(ref.pk,))
