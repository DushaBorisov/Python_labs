
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from student import views as student_views

router = routers.DefaultRouter()
router.register('students', student_views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]
