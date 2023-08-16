from django import template

register = template.Library()


@register.filter()
def firstCap(value):
    return " ".join(w.capitalize() for w in value.split(" "))
