import django_filters
from django_filters import CharFilter
from .models import *


class ApartmentFilter(django_filters.FilterSet):
    building = CharFilter(field_name='building__address', lookup_expr='icontains')

    class Meta:
        model = Apartment
        fields = ['building', 'tenant', 'floor', 'square_meters']


class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = Expense
        fields = ['total', 'type_expenses', 'month', 'year']


class PaymentFilter(django_filters.FilterSet):
    class Meta:
        model = Payment
        fields = ['month', 'year', 'payment_made']
