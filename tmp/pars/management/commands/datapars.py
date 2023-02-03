from django.core.management.base import BaseCommand
from pars.models import Firma, Vacancy, Zarplata, Link, Position, Region
import pprint
import requests


class Command(BaseCommand):

    def handle(self, *args, **options):
        text = 'Учитель'
        result = parser(text)
        for test_add in result:
            Position.objects.get_or_create(name=test_add[0])
            pos_id = Position.objects.get(name=test_add[0])

            Firma.objects.get_or_create(name=test_add[1])
            fir_id = Firma.objects.get(name=test_add[1])

            Region.objects.get_or_create(name=test_add[2])
            reg_id = Region.objects.get(name=test_add[2])

            Zarplata.objects.get_or_create(name=test_add[3])
            zar_id = Zarplata.objects.get(name=test_add[3])

            Link.objects.get_or_create(name=test_add[4])
            lin_id = Link.objects.get(name=test_add[4])

            Vacancy.objects.get_or_create(position_id=pos_id, region_id=reg_id, firma_id=fir_id,
                                          zarplata_id=zar_id,
                                          link_id=lin_id)

def parser(text):
    url = 'https://api.hh.ru/vacancies'
    gorod = '1384'
    params = {
        'text': text,
        'area': gorod
    }

    result = requests.get(url, params=params).json()
    pprint.pprint(result)
    vacancy_list = []
    for item in result['items']:
        city = item['area']['name']
        firma = item['employer']['name']
        vacancy = item['name']
        link = item['alternate_url']
        try:
            zarplata = item['salary']['from']
            if zarplata == None:
                zarplata = 'Не указана'
        except Exception:
            zarplata = 'Не указана'
        data = (vacancy, firma, city, zarplata, link)
        vacancy_list.append(data)
    return vacancy_list
