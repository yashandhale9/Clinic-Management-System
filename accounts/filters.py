import django_filters
from .models import User


class UserFilter(django_filters.FilterSet):
    """Filter for User model"""
    user_type = django_filters.ChoiceFilter(choices=User.USER_TYPE_CHOICES)
    created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')
    
    class Meta:
        model = User
        fields = ['user_type', 'is_active']

