"""tmp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from pars.api_views import VacancyViewSet

router = routers.DefaultRouter()
router.register(r'vacancy', VacancyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pars.urls', namespace='pars')),
    path('users/', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/ver1/', include(router.urls)),
    # path('__debug__/', include('debug_toolbar.urls'))
]
if settings.DEBUG:
    import debug_toolbar
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
