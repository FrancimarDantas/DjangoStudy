from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("profile/<int:id_user>/", views.perfil,name="perfil_user"),
    path("content/<int:id_post>/", views.visualizar,name="visualizar_conteudo"),
]
