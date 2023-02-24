from .models import Vacancy
from .serializers import VacancySerializer
from rest_framework import viewsets


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
