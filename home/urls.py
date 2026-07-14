from django.urls import path
from . import views

urlpatterns = [
    path('', views.obtener_clima, name='obtener_clima'),
    path('ciudad/', views.ciudad, name='ciudad')
]
