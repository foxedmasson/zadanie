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
from django.urls import path

from app1.views import CountryListCreateAPIView, CountryDetailAPIView, \
    ManufacturerListCreateAPIView, ManufacturerDetailAPIView, \
    CarListCreateAPIView, CarDetailAPIView, \
    CommentListCreateAPIView, CommentDetailAPIView, ExportDataAPIView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('export-data/', ExportDataAPIView, name='export_data'),
    path('countries/', CountryListCreateAPIView.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryDetailAPIView.as_view(), name='country-detail'),
    path('manufacturers/', ManufacturerListCreateAPIView.as_view(), name='manufacturer-list'),
    path('manufacturers/<int:pk>/', ManufacturerDetailAPIView.as_view(), name='manufacturer-detail'),
    path('cars/', CarListCreateAPIView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailAPIView.as_view(), name='car-detail'),
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
]