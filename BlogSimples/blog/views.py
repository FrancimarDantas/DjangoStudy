from django.shortcuts import render
from .models import Postagem
# Create your views here.

def homepage(request):
    postagem = Postagem.objects.all()
    return render(request,'home.html',{"posta":postagem})
