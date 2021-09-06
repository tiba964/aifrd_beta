from rest_framework import serializers
from .models import CareerDetail, CareerList, CareerDetatilImage


class CareerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CareerDetail
        fields = '__all__'


class CareerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CareerList
        fields = '__all__'


class CareerDetatilImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CareerDetatilImage
        fields = '__all__'
