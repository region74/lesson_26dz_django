from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView

app_name = 'users'
urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', views.UserCreate.as_view(), name='registr'),
]
