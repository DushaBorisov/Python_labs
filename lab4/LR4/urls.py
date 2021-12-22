
from django.contrib import admin
from django.urls import path

from bmstu_lab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cars),
    path('car/<int:id>/', views.car, name='car_url'),
]
