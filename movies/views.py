
from django.shortcuts import render, redirect
# Importamos la libreria HttpRespons
from django.http import HttpResponse

from .models import Movie

from .forms import MovieForm

# Aqui creamos nuestras vistas


def start(request):
    return render(request, 'pages/start.html')


def about(request):
    return render(request, 'pages/about.html')


def movies(request):
    movies = Movie.objects.all()
    # print(movies)
    return render(request, 'movies/index.html', {'movies': movies})


def create(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('movies')
    return render(request, 'movies/create.html', {'form': form})


def edit(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None,
                     request.FILES or None, instance=movie)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('movies')
    return render(request, 'movies/edit.html', {'form': form})


def delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('movies')
