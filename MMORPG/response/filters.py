from django_filters import FilterSet
from .models import Response


# Фильтрация
class ResponseFilter(FilterSet):
    class Meta:
        model = Response
        fields = [
            'user__username',
            'post__title',
            'post__category',
            'date_create',
        ]
