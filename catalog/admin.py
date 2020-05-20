from django.contrib import admin
from django.core.mail import send_mail
import multiprocessing.dummy as multiprocessing
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


class PlacesAdmin(admin.ModelAdmin):
    list_display = ('part_of_the_world', 'country', 'city', 'name')
    fields = ['name', ('part_of_the_world', 'country', 'city'), 'description', 'image', 'tags']
    list_filter = ('part_of_the_world', 'country', 'city', 'tags')
    pass


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'verified']


class EmailSending(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        message = render_to_string('mail.html', {
            'text': obj.text + '\n' + "http://127.0.0.1:8000/catalog/verification",
            'sending_time': obj.sending_time,
        })

        recipients = [
            x.email for x in CustomUser.objects.all() if not x.verified
        ]

        def send(email):
            send_mail(obj.heading, message, EMAIL_HOST_USER, [email])

        pool = multiprocessing.Pool()
        pool.map(send, recipients)
        obj.heading = ''
        obj.text = None
        super().save_model(request, obj, form, change)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Newsletter, EmailSending)
admin.site.register(Places, PlacesAdmin)
