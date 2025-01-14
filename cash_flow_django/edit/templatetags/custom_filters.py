from django import template

register = template.Library()

# Возвращение атрибута по его имени
@register.filter
def attr(obj, field_name):
    return getattr(obj, field_name, None)