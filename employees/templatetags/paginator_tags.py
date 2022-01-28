from django import template
from django.core.paginator import Paginator
from employees.models import CustomPaginate

register = template.Library()
records = CustomPaginate.objects.all().first()
around = records.around
boundaries = records.boundaries


@register.simple_tag
def get_proper_elided_page_range(p, number, on_each_side=around, on_ends=boundaries):
    paginator = Paginator(p.object_list, p.per_page)
    return paginator.get_elided_page_range(number=number, 
                                           on_each_side=on_each_side,
                                           on_ends=on_ends)