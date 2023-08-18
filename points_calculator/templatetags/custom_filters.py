from django import template

register = template.Library()


@register.filter
def get_rounds(points):
    return [attr for attr in points.__dict__ if not attr.startswith('_')]


@register.filter
def get_value(points, round_num):
    return getattr(points, round_num, '')
