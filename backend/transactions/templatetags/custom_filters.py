from django import template

register = template.Library()

@register.filter(name='filter_by')
def filter_by(queryset, args):
    """
    Queryset ni filter qilish
    Ishlatish: queryset|filter_by:'field,value'
    """
    try:
        field, value = args.split(',')
        return queryset.filter(**{field: value})
    except:
        return queryset

@register.filter(name='sum_amount')
def sum_amount(queryset):
    """
    Tranzaksiyalar summasini hisoblash
    """
    try:
        from django.db.models import Sum
        result = queryset.aggregate(total=Sum('amount'))['total']
        return result if result else 0
    except:
        return 0
