from django.urls import path, include
from rest_framework.routers import DefaultRouter

from testapp import views

app_name = 'testapp'

router = DefaultRouter()

router.register('license', views.LicenseViewSet, basename='license')
router.register('', views.CarViewSet, 'cars')

urlpatterns = [
    path('api/', include(router.urls)),
]
