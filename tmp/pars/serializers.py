from django.urls import path, include
from .models import Vacancy, Zarplata, Region, Firma, Position, Link
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class VacancySerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    position_id = serializers.SlugRelatedField(slug_field='name', queryset=Position.objects)
    region_id = serializers.SlugRelatedField(slug_field='name', queryset=Region.objects)
    firma_id = serializers.SlugRelatedField(slug_field='name', queryset=Firma.objects)
    zarplata_id = serializers.SlugRelatedField(slug_field='name', queryset=Zarplata.objects)
    link_id = serializers.SlugRelatedField(slug_field='name', queryset=Link.objects)
