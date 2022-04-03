""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.views.generic import TemplateView
from apps.home import views
from apps.home.views import HomeServe
from django.conf import settings



### הגשת URL ראשית
if settings.DEBUG==True:
    urlpatterns = [
        
        url(r'^adminapp/', admin.site.urls),
        # url(r'^$', HomeServe.as_view()),
        path('', include('apps.home.urls')),
        
    ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

else:
    urlpatterns = [
        path('', include('apps.home.urls')),
       
    ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = 'apps.home.views.error_404_view'
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
