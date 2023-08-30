from rest_framework import serializers
from .models import Company, Type, City, Country, Contact, Position, Subscribe


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'title']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'title']


class CityGetSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = ['id', 'title', 'country']
        extra_fields = {
            "country": {"read_only": True}
        }


class CityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'title', 'country']
        extra_fields = {
            "country": {"read_only": True}
        }


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'subject', 'created_date']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'title']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'title', 'location']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['id', 'email']


