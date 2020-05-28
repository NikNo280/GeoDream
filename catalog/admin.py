from django.contrib import admin
from django.core.mail import send_mail
import multiprocessing.dummy as multiprocessing
from .models import *
from GeoDream.settings import EMAIL_HOST_USER
from jinja2 import FileSystemLoader
from GeoDream.jinja2 import environment

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

        recipients_email = [
            [x.email, x.username] for x in CustomUser.objects.all() if not x.verified
        ]

        def send(user):
            env = environment(loader=FileSystemLoader('templates/'))
            template = env.get_template('mail.html')
            message = template.render(username=user[1], email=user[0], sending_time=obj.sending_time)
            send_mail("Подтверждение регистрации", message, EMAIL_HOST_USER, [user[0]])

        pool = multiprocessing.Pool()
        pool.map(send, recipients_email)
        super().save_model(request, obj, form, change)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Newsletter, EmailSending)
admin.site.register(Places, PlacesAdmin)
