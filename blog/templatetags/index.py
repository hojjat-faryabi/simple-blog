from django import template
register = template.Library()

@register.filter
def index(itrable, i):
    return itrable[i]