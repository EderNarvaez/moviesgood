from unicodedata import name
from xml.dom.minidom import Document
import django
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

# Agregamos los path para acceder a las vistas

urlpatterns = [
    path('', views.start, name='start'),
    path('about', views.about, name="about"),
    path('movies', views.movies, name="movies"),
    path('movies/create', views.create, name="create"),
    path('movies/edit', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('movie/edit/<int:id>', views.edit, name="edit")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
