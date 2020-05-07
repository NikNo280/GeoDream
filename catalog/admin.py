import datetime
from django.contrib import admin
from django.core.mail import send_mail
from multiprocessing.dummy import Manager
from django.template.loader import render_to_string
from .models import *
from GeoDream.settings import EMAIL_HOST_USER

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

class EmailSending(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        message = render_to_string('mail.html', {
            'text': obj.text,
            'sending_time': obj.sending_time,
        })

        recipients = [
            x.email for x in CustomUser.objects.all() if x.verified
        ]

        def send(email):
            send_mail(obj.heading, message, EMAIL_HOST_USER, [email])

        pool = Manager().Pool(4)
        pool.map(send, recipients)
        obj.heading = ''
        obj.text = None
        super().save_model(request, obj, form, change)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Newsletter, EmailSending)
