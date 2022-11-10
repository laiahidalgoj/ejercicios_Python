import uuid

from django.db import models
from django.urls import reverse
import datetime


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=66)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100, help_text='Put the director\'s name')
    surname = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s (%s)' % (self.name, self.surname)


class UploadImage(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.caption


class Film(models.Model):
    title = models.CharField(max_length=66)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    synopsis = models.CharField(max_length=160)
    genre = models.ManyToManyField(Genre)
    image = models.ForeignKey('UploadImage', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])


class FilmInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    film = models.ForeignKey('Film', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('p', 'Premieres'),
        ('c', 'Coming soon'),
        ('b', 'Billboard')
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='b')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return '%s (%s)' % (self.id, self.film.title)



