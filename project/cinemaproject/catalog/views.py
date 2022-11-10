
from django.shortcuts import render
from .models import Film, Genre, FilmInstance, Director


# Create your views here.


def index(request):
    num_films = Film.objects.all().count()
    num_instances = FilmInstance.objects.all().count()
    num_directors = Director.objects.all().count()

    status = FilmInstance.objects.filter(status__exact='b').count()

    return render(
        request,
        'index.html',
        context={
            'num_films': num_films,
            'num_instances': num_instances,
            'num_directors': num_directors,
            'billboard': status
        }
    )
