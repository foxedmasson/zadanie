from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .models import Country, Manufacturer, Car, Comment
from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentSerializer, \
    CountrySerializerForZ, ManufacturerSerializerForZ, CarSerializerForZ, CommentSerializerForZ


# Логика к выгрузке в форматах
def ExportData(request):
    format = request.GET.get('format', 'xlsx')  # Получаем параметр format из запроса (по умолчанию xlsx)

    data = Country.objects.all()  # Получаем данные из базы данных

    if format == 'xlsx':
        # Создаем DataFrame из данных модели
        df = pd.DataFrame(list(data.values()))

        # Создаем файл XLSX
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'
        df.to_excel(response, index=False)
        return response
    elif format == 'csv':
        df = pd.DataFrame(list(data.values()))
        # Создаем файл CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
        df.to_csv(response, index=False)
        return response
    else:
        return HttpResponse('Invalid format parameter. Please specify "xlsx" or "csv".', status=400)


# Эндпоинты для 4рех конкретных гет запросов.
class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializerForZ
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ManufacturerListView(generics.ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializerForZ
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializerForZ
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# Эндпоинты страны
class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CountryCreateAPIView(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CountryUpdateAPIView(generics.UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CountryDestroyAPIView(generics.DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# Эндпоинты производителя
class ManufacturerListAPIView(generics.ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ManufacturerCreateAPIView(generics.CreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ManufacturerUpdateAPIView(generics.UpdateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ManufacturerDestroyAPIView(generics.DestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# Эндпоинты машины
class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CarCreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CarUpdateAPIView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CarDestroyAPIView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# Эндпоинты коментария
class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AllowAny]


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerForZ
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AllowAny]


class CommentUpdateAPIView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CommentDestroyAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
