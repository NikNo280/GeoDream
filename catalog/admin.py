from django.contrib import admin
from .models import PartOfTheWorld, Countries, Cities, Places, Tags, CustomUser


@admin.register(PartOfTheWorld)
class PartOfTheWorldAdmin(admin.ModelAdmin):
    pass


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    pass


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass


# Define the admin class
class PlacesAdmin(admin.ModelAdmin):
    list_display = ('part_of_the_world', 'country', 'city', 'name')
    fields = ['name', ('part_of_the_world', 'country', 'city'), 'description', 'image', 'tags']
    list_filter = ('part_of_the_world', 'country', 'city', 'tags')
    pass


# Register the admin class with the associated model
admin.site.register(Places, PlacesAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)
