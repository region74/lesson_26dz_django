from django.db import models


class StampName(models.Model):
    name = name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Link(StampName):
    pass


class Firma(StampName):
    pass


class Zarplata(StampName):
    pass


class Region(StampName):
    pass


class Position(StampName):
    pass


class Vacancy(models.Model):
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE, default='0')
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, default='0')
    firma_id = models.ForeignKey(Firma, on_delete=models.CASCADE, default='0')
    zarplata_id = models.ForeignKey(Zarplata, on_delete=models.CASCADE, default='0')
    link_id = models.ForeignKey(Link, on_delete=models.CASCADE, default='0')

    def __str__(self):
        return f'Должность: {self.position_id} Город: {self.region_id} Фирма: {self.firma_id} Зарплата: {self.zarplata_id} Ссылка: {self.link_id}'
