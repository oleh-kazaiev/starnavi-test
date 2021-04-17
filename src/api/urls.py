from django.urls import path, include
from rest_framework import routers

from .auth import views as auth_views


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
