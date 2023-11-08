from django.urls import path, include
from rest_framework import routers
from .views import ProfileViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile', ProfileViewset)

urlpatterns = [
    path('', include(router.urls)),
]
