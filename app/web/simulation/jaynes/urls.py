from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='jaynes'),
    path('rabi', views.Rabi.as_view(), name='rabi'),
    path('wigner', views.Wigner.as_view(), name='wigner'),
]