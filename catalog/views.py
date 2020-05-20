from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .forms import CustomUserCreationForm, PlacesForm
from .models import *


def index(request):
    num_partoftheworld = PartOfTheWorld.objects.all().count()
    num_countries = Countries.objects.all().count()
    num_cities = Cities.objects.all().count()
    num_places = Places.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_PartOfTheWorld': num_partoftheworld, 'num_Countries': num_countries,
                 'num_Cities': num_cities, 'num_Places': num_places},
    )

def verification(request):
    user = CustomUser.objects.get(username=request.user.username)
    user.verified = True
    user.save()
    return render(
        request,
        'registration/user_verification.html',
    )


class PlacesListView(generic.ListView):
    model = Places


class PlacesDetailView(generic.DetailView):
    model = Places


class PlacesCreate(CreateView):
    model = Places
    form_class = PlacesForm
    template_name = 'catalog/places_update.html'

    def form_valid(self, form):
        return super(PlacesCreate, self).form_valid(form)


class PlacesUpdate(UpdateView):
    model = Places
    fields = '__all__'
    template_name = 'catalog/places_update.html'


class PlacesDelete(DeleteView):
    model = Places
    success_url = reverse_lazy('places')
    template_name = 'catalog/places_delete.html'


class RegisterFormView(FormView):
    form_class = CustomUserCreationForm
    fields = ['username', 'password', 'email', 'verified']
    success_url = reverse_lazy('login')
    template_name = "registration/user_create.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
