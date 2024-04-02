
from django.contrib import admin
from django.urls import include, path
from app.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('Pessoa/', PessoasView.as_view(), name='Pessoa'),
    path('ocupacao/', OcupacoesView.as_view(),
    name='ocupacao'),
    path('cidade/', CidadesView.as_view(),
    name='cidade'),
    path('InstituicaoEnsino/', InstituicoesView.as_view(), name='InstituicaoEnsino'),
    path('AreaSaber/', AreaSaberView.as_view(),
    name='AreaSaber'),
    path('Curso/', CursosView.as_view(),
    name='Curso'),
    path('PeriodoCurso/', PeriodoCursosView.as_view(),
    name='PeriodoCurso'),
    path('Disciplinas/', DisciplinasView.as_view(),
    name='Disciplinas'),
    path('Matricula/', MatriculasView.as_view(),
    name='Matricula'),
    path('Avaliacao/', AvaliacoesView.as_view(),
    name='Avaliacao'),
    path('Frequencia/', FrequenciasView.as_view(),
    name='Frequencia'),
    path('Turma/', TurmasView.as_view(),
    name='Turma'),
]


