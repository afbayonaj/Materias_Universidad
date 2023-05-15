from django.urls import path
from . import views

urlpatterns = [
    path('index', views.home),
    path('registrar_curso/', views.registrar_curso),
    path('edicion_cursos/<codigo>', views.edicion_curso),
    path('editar_curso/', views.editar_curso),
    path('eliminar_curso/<codigo>', views.eliminar_curso),
]
