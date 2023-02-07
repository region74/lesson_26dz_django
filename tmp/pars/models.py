from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class Firma(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Zarplata(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    position_id = models.ForeignKey(Position,on_delete=models.CASCADE,default='0')
    region_id = models.ForeignKey(Region,on_delete=models.CASCADE,default='0')
    firma_id = models.ForeignKey(Firma,on_delete=models.CASCADE,default='0')
    zarplata_id = models.ForeignKey(Zarplata,on_delete=models.CASCADE,default='0')
    link_id = models.ForeignKey(Link,on_delete=models.CASCADE,default='0')

    def __str__(self):
        return f'Должность: {self.position_id} Город: {self.region_id} Фирма: {self.firma_id} Зарплата: {self.zarplata_id} Ссылка: {self.link_id}'
