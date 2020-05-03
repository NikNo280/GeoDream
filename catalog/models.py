from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class PartOfTheWorld(models.Model):
    name = models.CharField(max_length=255, help_text="Название части света")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('PartOfTheWorld-detail', args=[str(self.id)])


class Countries(models.Model):
    name = models.CharField(max_length=255, help_text="Название страны")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Countries-detail', args=[str(self.id)])


class Cities(models.Model):
    name = models.CharField(max_length=255, help_text="Название города")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Cities-detail', args=[str(self.id)])

class Tags(models.Model):
    name = models.CharField(max_length=255, help_text="Тег")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('place-detail', args=[str(self.id)])

class Places(models.Model):
    part_of_the_world = models.ForeignKey('PartOfTheWorld', on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey('Countries', on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey('Cities', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, help_text="Название места")
    description = models.CharField(max_length=1255, help_text="Описание")
    image = models.ImageField(upload_to='images')
    tags = models.ManyToManyField('Tags',  help_text="Теги")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('place-detail', args=[str(self.id)])

class CustomUser(AbstractUser):
    verified = models.NullBooleanField(default=False, help_text="Подписаться на рассылку сообщений?")
    pass

