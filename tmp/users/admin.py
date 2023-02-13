from django.contrib import admin
from .models import User


# Чтобы в админке появились пользователи
admin.site.register(User)
# Register your models here.
