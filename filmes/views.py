from django.http import JsonResponse
from .models import Filme

def listar_filmes(request):
    filmes = Filme.objects.all()
    dados = []
    for f in filmes:
        dados.append({
            'id': f.id,
            'titulo': f.titulo,
            'diretor': f.diretor,
            'categoria': f.get_categoria_display(),
            'nota': f.nota_imdb
        })
    return JsonResponse(dados, safe=False)

def filmes_por_genero(request, genero):
    filmes = Filme.objects.filter(genero__icontains=genero)
    dados = [{'titulo': f.titulo, 'genero': f.genero} for f in filmes]
    return JsonResponse(dados, safe=False)