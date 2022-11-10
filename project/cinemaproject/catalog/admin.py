from django.contrib import admin

# Register your models here.

from .models import Director, Genre, Film, FilmInstance, UploadImage

admin.site.register(Director)
admin.site.register(Film)
admin.site.register(FilmInstance)
admin.site.register(Genre)
admin.site.register(UploadImage)