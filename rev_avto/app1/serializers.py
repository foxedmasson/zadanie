from rest_framework import serializers

from .models import Country, Manufacturer, Car, Comment

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'




class CountrySerializerForZ(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        manufacturers = Manufacturer.objects.filter(country=instance)
        representation['manufacturers'] = ManufacturerSerializer(manufacturers, many=True).data
        return representation

class ManufacturerSerializerForZ(serializers.ModelSerializer):
    country_id = serializers.PrimaryKeyRelatedField(source='country', queryset=Country.objects.all())
    total_comments = serializers.SerializerMethodField()
    cars = serializers.SerializerMethodField()

    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country_id', 'total_comments', 'cars']

    def get_total_comments(self, obj):
        return Comment.objects.filter(car__manufacturer=obj).count()

    def get_cars(self, obj):
        cars = Car.objects.filter(manufacturer=obj)
        return CarSerializer(cars, many=True).data


class CarSerializerForZ(serializers.ModelSerializer):
    total_comments = serializers.SerializerMethodField()


    class Meta:
        model = Car
        fields = ['id', 'name', 'start_year', 'end_year', 'manufacturer_id', 'total_comments']

    def get_total_comments(self, obj):
        return Comment.objects.filter(car=obj).count()


class CommentSerializerForZ(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    def validate(self, data):
        if len(data['comment']) > 500:
            raise serializers.ValidationError("Комментарий не может содержать более 500 символов.")
        return data