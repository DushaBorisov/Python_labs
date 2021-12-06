
from django.contrib import admin
from django.urls import path

from Models_test import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cars),
    path('car/<int:id>/', views.car, name='car_url'),
]
