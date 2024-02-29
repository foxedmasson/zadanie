import pandas as pd
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework import viewsets

from .models import Car
from .models import Comment
from .models import Country
from .models import Manufacturer
from .serializers import CarSerializer
from .serializers import CommentSerializer
from .serializers import CountrySerializer
from .serializers import ManufacturerSerializer


# Логика к выгрузке в форматах
def ExportData(request):
    format = request.GET.get(
        "format", "xlsx"
    )  # Получаем параметр format из запроса (по умолчанию xlsx)

    data = Country.objects.all()  # Получаем данные из базы данных

    if format == "xlsx":
        # Создаем DataFrame из данных модели
        df = pd.DataFrame(list(data.values()))

        # Создаем файл XLSX
        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = 'attachment; filename="exported_data.xlsx"'
        df.to_excel(response, index=False)
        return response
    elif format == "csv":
        df = pd.DataFrame(list(data.values()))
        # Создаем файл CSV
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="exported_data.csv"'
        df.to_csv(response, index=False)
        return response
    else:
        return HttpResponse(
            'Invalid format parameter. Please specify "xlsx" or "csv".', status=400
        )


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve", "create"]:
            # Разрешение AllowAny для просмотра и создания
            permission_classes = [permissions.AllowAny]
        else:
            # Для остальных методов использовать IsAuthenticatedOrReadOnly
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
