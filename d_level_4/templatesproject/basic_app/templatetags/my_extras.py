
from django import template

register = template.Library()

# @register.filter(name='cut')
def cut(value,arg):
    # cut out value from string
    return value.replace(arg,' ')

register.filter('cut',cut) 