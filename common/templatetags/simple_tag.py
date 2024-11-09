from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def simple_tag_example(context, number=23):
    return f"This is a simple tag example {context['username']} {number}"