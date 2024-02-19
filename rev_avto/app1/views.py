from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Country, Manufacturer, Car, Comment
from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentSerializer


#Логика к выгрузке в форматах
class ExportDataAPIView:
    queryset = None
    serializer_class = None

    def get(self, request, *args, **kwargs):
        export_format = request.Get.get('format')
        if export_format==('csv'):
            return self.export_csv()
        elif export_format==('xlsx'):
            return self.export_xlsx()
        else:
            return HttpResponse("Неверный формат", status=400)

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer(self, queryset):
        return self.serializer_class(queryset, many=True)
    def export_csv(self):
        data = self.get_queryset()
        serializer = self.get_serializer(data)
        csv_data = pd.DataFrame(serializer.data)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        csv_data.to_csv(response, index=False)
        return response

    def export_xlsx(self):
        data = self.get_queryset()
        serializer = self.get_serializer(data)
        xlsx_data = pd.DataFrame(serializer.data)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="export.xlsx"'
        xlsx_data.to_excel(response, index=False)
        return response



#Эндпоинты
class CountryListCreateAPIView(generics.ListCreateAPIView, ExportDataAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CountryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ManufacturerListCreateAPIView(generics.ListCreateAPIView, ExportDataAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ManufacturerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CarListCreateAPIView(generics.ListCreateAPIView, ExportDataAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CommentListCreateAPIView(generics.ListCreateAPIView,ExportDataAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AllowAny]


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]