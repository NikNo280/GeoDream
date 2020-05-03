from django.urls import path
from . import views
from django.conf.urls import url, include
from .views import PlacesUpdate, PlacesCreate, PlacesDelete, RegisterFormView

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^places/$', views.PlacesListView.as_view(), name='places'),
    url(r'^places/(?P<pk>\d+)$', views.PlacesDetailView.as_view(), name='place-detail'),
]

urlpatterns += [
    url(r'^places/(?P<pk>[-\w]+)/update/$', PlacesUpdate.as_view(), name='place-update'),
    url(r'^places/add/$', PlacesCreate.as_view(), name='place-add'),
    url(r'^places/(?P<pk>[-\w]+)/delete/$', PlacesDelete.as_view(), name='place-delete'),
    url(r'^places/registration/$', RegisterFormView.as_view(), name='user-registration'),
]
