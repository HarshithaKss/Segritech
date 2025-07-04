"""
This module contains custom template filters for the first app.
Currently includes:
- multiply: Multiplies a number by another number
"""

from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies the value by the argument"""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return value 