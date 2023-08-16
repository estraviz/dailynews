from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.filter()
def firstCap(value):
    return ' '.join(w.capitalize() for w in value.split(' '))


@register.filter()
def display_length(val):
    if len(val) == 0:
        return mark_safe("<p></p>")
    return mark_safe(f"<p>{len(val)} result{'' if len(val) == 1 else 's'}</p>")
