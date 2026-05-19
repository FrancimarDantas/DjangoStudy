from django.shortcuts import render, get_object_or_404
from .models import Postagem
from django.contrib.auth.models import User

# Create your views here.

def homepage(request):
    postagem = Postagem.objects.all()
    return render(request, 'home.html', {"posta": postagem})


def perfil(request, id_user):
    postagem = get_object_or_404(Postagem,autho = id_user)
    return render(request, 'perfil.html', {"post":postagem})


def visualizar(request, id_post):
    postagem = get_object_or_404(Postagem,autho = id_post)
    return render(request, 'visualizar.html', {"post":postagem})
