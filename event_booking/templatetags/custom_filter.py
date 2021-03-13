from django import template
register = template.Library()


@register.filter(name ='icon_split')
def icon_split(stri):
    sep = stri.split('</i>')[0]
    sep = sep + '</i>'
    return sep