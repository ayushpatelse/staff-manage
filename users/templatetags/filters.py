from django import template

register = template.Library()

@register.filter
def phone_format(value):
    value_str = str(value)
    if len(value_str) == 10:
        return f"({value_str[:3]}) {value_str[3:6]}-{value_str[6:]}"    
    return f'Required Format : XXX-XXX-XXXX'  