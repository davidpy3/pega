# coding=utf-8
# templatetags/paginator.py

from django import template


register = template.Library()


@register.inclusion_tag('templatetags/paginator.html', takes_context=True)
def paginator(context, adjacent_pages=3):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    """
    paginator = context['paginator']
    page_obj = context['page_obj']
    page_numbers = [n for n in range(page_obj.number - adjacent_pages, page_obj.number + adjacent_pages + 1)
                    if n > 0 and n <= paginator.num_pages]
    return {
        'page_numbers': page_numbers,
        'page_obj': page_obj,
        'paginator': paginator,
        'show_first': 1 not in page_numbers,
        'show_last': paginator.num_pages not in page_numbers,
    }
