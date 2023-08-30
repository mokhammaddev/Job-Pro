from django.contrib import admin
from .models import City, Country, Contact, Type, Position, Company, Subscribe


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'location']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'country']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']




