from django import template

register = template.Library()


@register.filter(is_safe=True)
def echo_lower(value):
    return value.lower()
