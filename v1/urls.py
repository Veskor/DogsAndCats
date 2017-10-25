from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'dog',DogViewSet)
router.register(r'cat',CatViewSet)

urlpatterns = [
    url(
            r'^v1/',
                include(
                            router.urls,
                        ),
            ),
        ]
