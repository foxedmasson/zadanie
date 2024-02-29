"""
URL configuration for rev_avto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,  include
from app1 import urlss

# from app1.views import CountryListAPIView, CountryCreateAPIView, CountryUpdateAPIView, CountryDestroyAPIView, \
#     ManufacturerListAPIView, ManufacturerCreateAPIView, ManufacturerUpdateAPIView, ManufacturerDestroyAPIView, \
#     CarListAPIView, CarCreateAPIView, CarUpdateAPIView, CarDestroyAPIView, \
#     CommentListAPIView, CommentCreateAPIView, CommentUpdateAPIView, CommentDestroyAPIView, CountryListView, \
#     ManufacturerListView, \
#     CarListView, ExportData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urlss')),
    # path('export-data/', ExportData, name='export-data'),
    # path('cars-gt/', CarListView.as_view(), name='car-lists'),
    # path('manufacturers-gt/', ManufacturerListView.as_view(), name='manufacturer-lists'),
    # path('countries-gt/', CountryListView.as_view(), name='country-lists'),
    # path('countries/', CountryListAPIView.as_view(), name='country-list'),
    # path('countries-create/', CountryCreateAPIView.as_view(), name='country-create'),
    # path('countries-update/', CountryUpdateAPIView.as_view(), name='country-update'),
    # path('countries-destroy/', CountryDestroyAPIView.as_view(), name='country-destroy'),
    # path('manufacturers/', ManufacturerListAPIView.as_view(), name='manufacturer-list'),
    # path('manufacturers-create/', ManufacturerCreateAPIView.as_view(), name='manufacturer-create'),
    # path('manufacturers-update/', ManufacturerUpdateAPIView.as_view(), name='manufacturer-update'),
    # path('manufacturers-destroy/', ManufacturerDestroyAPIView.as_view(), name='manufacturer-destroy'),
    # path('cars/', CarListAPIView.as_view(), name='car-list'),
    # path('cars-create/', CarCreateAPIView.as_view(), name='car-create'),
    # path('cars-update/', CarUpdateAPIView.as_view(), name='car-update'),
    # path('cars-destroy/', CarDestroyAPIView.as_view(), name='car-destroy'),
    # path('comments/', CommentListAPIView.as_view(), name='comment-list'),
    # path('comments-create/', CommentCreateAPIView.as_view(), name='comment-create'),
    # path('comments-update/', CommentUpdateAPIView.as_view(), name='comment-update'),
    # path('comments-destroy/', CommentDestroyAPIView.as_view(), name='comment-destroy'),
]
