from django import template


register = template.Library()


@register.filter(name="zip")
def zip_two_lists(first, second):
    return zip(first, second)


@register.filter(name="zip_empty")
def zip_two_lists_allow_empty(first, second):
    zipped = []
    for i in range(max(len(first), len(second))):
        try:
            f = first[i]
        except IndexError:
            f = ""
        try:
            s = second[i]
        except IndexError:
            s = ""
        zipped.append((f, s))
    return zipped
