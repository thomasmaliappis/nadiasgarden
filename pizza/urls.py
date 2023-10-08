from django.urls import path

from pizza import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ored', views.order, name='order'),
]
