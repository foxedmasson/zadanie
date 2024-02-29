from rest_framework import serializers
from django.utils import timezone
from .models import Country, Manufacturer, Car, Comment


class CountrySerializer(serializers.ModelSerializer):
    # manufacturers = serializers.SerializerMethodField()
    #manufacturers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Country
        fields = '__all__'

    # def get_manufacturers(self, obj):
    #     manufacturers = Manufacturer.objects.filter(country=obj)
    #     return ManufacturerSerializer(manufacturers, many=True).data



class ManufacturerSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    cars = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()
    class Meta:
        model = Manufacturer
        fields = '__all__'

    def get_cars(self, obj):
        cars = Car.objects.filter(manufacturer=obj)
        return CarSerializer(cars, many=True).data

    def get_total_comments(self, obj):
        return Comment.objects.filter(car__manufacturer=obj).count()


class CarSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    total_comments = serializers.SerializerMethodField()
    class Meta:
        model = Car
        fields = '__all__'

    def get_total_comments(self, obj):
        return Comment.objects.filter(car=obj).count()

    def validate(self, data):
        start_year = data.get('start_year')
        end_year = data.get('end_year')

        # Проверка, что начальный год не превышает конечный
        if start_year and end_year and start_year > end_year:
            raise serializers.ValidationError("Начальный год не может быть позже конечного года")

        # Проверка, что конечный год не превышает текущий год
        if end_year and end_year > timezone.now().year:
            raise serializers.ValidationError("Конечный год не может быть в будущем")

        return data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def validate(self, data):
        if len(data['comment']) > 500:
            raise serializers.ValidationError('Комментарий не может содержать более 500 символов.')
        return data


# class CountrySerializerForZ(serializers.ModelSerializer):
#     class Meta:
#         model = Country
#         fields = ['id', 'name']
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         manufacturers = Manufacturer.objects.filter(country=instance)
#         representation['manufacturers'] = ManufacturerSerializer(manufacturers, many=True).data
#         return representation
#
#
# class ManufacturerSerializerForZ(serializers.ModelSerializer):
#     country_id = serializers.PrimaryKeyRelatedField(source='country', queryset=Country.objects.all())
#     total_comments = serializers.SerializerMethodField()
#     cars = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Manufacturer
#         fields = ['id', 'name', 'country_id', 'total_comments', 'cars']
#
#     def get_total_comments(self, obj):
#         return Comment.objects.filter(car__manufacturer=obj).count()
#
#     def get_cars(self, obj):
#         cars = Car.objects.filter(manufacturer=obj)
#         return CarSerializer(cars, many=True).data
#
#
# class CarSerializerForZ(serializers.ModelSerializer):
#     total_comments = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Car
#         fields = ['id', 'name', 'start_year', 'end_year', 'manufacturer_id', 'total_comments']
#
#     def get_total_comments(self, obj):
#         return Comment.objects.filter(car=obj).count()
#
#
# class CommentSerializerForZ(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
#     def validate(self, data):
#         if len(data['comment']) > 500:
#             raise serializers.ValidationError('Комментарий не может содержать более 500 символов.')
#         return data
#
