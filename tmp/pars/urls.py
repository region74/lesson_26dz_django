from django.urls import path
from pars import views

app_name = 'pars'
urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('results/', views.ParsResultView.as_view(), name='results'),
    path('found/', views.ParsFoundView.as_view(), name='found'),
    path('psih/', views.PsihView.as_view(), name='psih')
]
