from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CarViewSet
from .views import CommentViewSet
from .views import CountryViewSet
from .views import ManufacturerViewSet

router = DefaultRouter()
router.register(r"countries", CountryViewSet)
router.register(r"manufacturers", ManufacturerViewSet)
router.register(r"cars", CarViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
