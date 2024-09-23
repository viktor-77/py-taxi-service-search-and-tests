from django import template

register = template.Library()


@register.simple_tag
def url_update_tag(request, **kwargs):
    updated = request.GET.copy()

    for key, value in kwargs.items():
        if value is not None:
            updated[key] = value
        else:
            updated.pop(key, 0)

    return updated.urlencode()
