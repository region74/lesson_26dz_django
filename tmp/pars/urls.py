from django.urls import path
from pars import views

app_name = 'pars'
urlpatterns = [
    path('', views.main_view, name='main'),
    path('results/', views.result_view, name='results'),
    path('found/', views.found_view, name='found')
]
