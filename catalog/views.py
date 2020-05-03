from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm
from .models import PartOfTheWorld, Countries, Cities, Places


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_PartOfTheWorld = PartOfTheWorld.objects.all().count()
    num_Countries = Countries.objects.all().count()
    num_Cities = Cities.objects.all().count()
    num_Places = Places.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_PartOfTheWorld': num_PartOfTheWorld, 'num_Countries': num_Countries,
                 'num_Cities': num_Cities, 'num_Places': num_Places},
    )

from django.views import generic

class PlacesListView(generic.ListView):
    model = Places

class PlacesDetailView(generic.DetailView):
    model = Places


##############################################

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Places
from .forms import PlacesForm
from django.urls import reverse_lazy


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