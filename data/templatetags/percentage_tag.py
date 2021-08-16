from django import template

register = template.Library()

@register.simple_tag
def calcpercent(highPrice, lastPrice):
  percentage = ((highPrice - lastPrice) / highPrice) * 100
  return percentage