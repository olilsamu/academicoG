from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages


class indexView(View):
    def get (self, request, *args, **kwargs):
        return render (request, 'index.html')
    def post(self, request):
        pass

from django.views import View
from django.contrib import messages  

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = PessoasView.objects.all()
        return render(request, 'pessoas.html', {'pessoas': pessoas})

class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = CidadesView.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})

class AreaSaberView(View):
    def get(self, request, *args, **kwargs):
        areas = AreaSaberView.objects.all()
        return render(request, 'areas.html', {'areas': areas})

class PeriodoCursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = PeriodoCursosView.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos})

class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = DisciplinasView.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicoesView.objects.all()
        return render(request, 'instituicoes.html', {'instituicoes': instituicoes})

class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        frequencias = FrequenciasView.objects.all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})

class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = MatriculasView.objects.all()
        return render(request, 'matriculas.html', {'matriculas': matriculas})

class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = OcorrenciasView.objects.all()  
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})

class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = AvaliacoesView.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})

class TurmasView(View):
    def get(self, request, *args, **kwargs):
        turmas = TurmasView.objects.all()
        return render(request, 'turmas.html', {'turmas': turmas})

class TiposAvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        tipos = TiposAvaliacaoView.objects.all() 
        return render(request, 'tipos.html', {'tipos': tipos})

class CursosView(View):
    def get(self, request, *args, **kwargs):
        disci_cur = CursosView.objects.all()  
        return render(request, 'disci_cur.html', {'disci_cur': disci_cur})

    
    


