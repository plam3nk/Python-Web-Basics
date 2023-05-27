from django import template

register = template.Library()


@register.filter(name='odd')
def show_only_odd(nums):

    # can do additional logic in custom filters

    return [x for x in nums if x % 2 == 1]
