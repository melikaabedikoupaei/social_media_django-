from django import template
from  core.models import *
register = template.Library()

@register.simple_tag(name='totallike')
def function():
    return 10
