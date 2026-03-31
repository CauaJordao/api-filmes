from django.contrib import admin
from .models import Filme

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'diretor', 'ano_lancamento', 'nota_imdb')
    search_fields = ('titulo', 'diretor')

admin.site.register(Filme, FilmeAdmin)