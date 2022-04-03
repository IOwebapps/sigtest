
from django.urls import path, include,re_path
from django.views.generic import TemplateView
from . import views
from apps.home.views import *
# from django.urls import path, include,re_path


# ניתוב פונקציות לקישור.
urlpatterns = [
    path('',HomeServe.as_view(),name="myhub"),
    re_path(r'^mypath/',views.pathme, name='mypath'),
    re_path(r'^mybot/', views.mybot, name='mybot'),
    re_path(r'^mypen/', views.myposttest, name='mypen'),
    re_path(r'^serverstat/', views.Dropletuse, name='serverstat'),
    re_path(r'^canibals/', views.canibals, name='canibals'),

    # re_path(r'^formget/', views.formgetter, name='formgetter'),

]