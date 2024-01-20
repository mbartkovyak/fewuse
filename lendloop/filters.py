import django_filters
from django.forms.widgets import DateInput


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")
    price__gt = django_filters.NumberFilter(
        field_name="price", lookup_expr="gt")
    price__lt = django_filters.NumberFilter(
        field_name="price", lookup_expr="lt")
    date_from = django_filters.DateFilter(
        field_name='date_from',
        label='Available from',
        lookup_expr='gte',
        widget=DateInput(attrs={'type': 'date'})
    )
    date_to = django_filters.DateFilter(
        field_name='date_to',
        label='Available to',
        lookup_expr='lte',
        widget=DateInput(attrs={'type': 'date'})
    )

    description = django_filters.CharFilter(lookup_expr="icontains")

    # Filter by foreign key
    category = django_filters.CharFilter(
        field_name="category__name", lookup_expr="iexact"
    )
