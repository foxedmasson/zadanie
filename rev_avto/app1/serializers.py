from rest_framework import serializers
from .models import Country, Manufacturer, Car, Comment

class CountrySerializer(serializers.ModelSerializer):
    manufacturers = serializers.SerializerMethodField()

    def get_manufacturers(self,obj):
        manufacturers = Manufacturer.objects.filter(country=obj)
        return ManufacturerSerializer(manufacturers, many=True).data

    class Meta:
        model = Country
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):
    counry = CountrySerializer
    cars = serializers.SerializerMethodField()
    coment_count = serializers.SerializerMethodField()

    def get_cars(self,obj):
        cars = Car.objects.filter(manufacturer = obj)
        return CarSerializer(cars, many=True).data

    def get_coment_count(self,obj):
        return obj.coment_set.count()

    class Meta:
        model = Country
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    manufacturers = serializers.SerializerMethodField()
    coment_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        return obj.comment_set.count()

    class Meta:
        model = Car
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def validate_car(self, value):
        # Проверяем существование автомобиля в базе данных
        if not Car.objects.filter(name=value).exists():
            raise serializers.ValidationError("Автомобиль с таким именем не существует")
        return value
    def validate(self, data):
        if len(data['comment']) > 500:
            raise serializers.ValidationError("Комментарий не может содержать более 500 символов.")
        return data