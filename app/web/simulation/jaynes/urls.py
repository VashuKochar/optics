from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rabi', views.rabi, name='rabi'),
    path('wigner', views.wigner, name='wigner'),
]