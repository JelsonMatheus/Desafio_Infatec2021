from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse


from core.models import *


# Create your views here.

def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')                               
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
        else:
            messages.error(request, "usuário e senha errado.")
    
    return redirect('/')


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')
    
    
@login_required(login_url='/login/')
def cadastro_alunos(request):
    context = {
        'alunos': Aluno.objects.all(),
        'series': Serie.objects.all()
    }
    
    return render(request, 'telas/cadastro-aluno.html', context)
    
    
@login_required(login_url='/login/')
def cadastro_professor(request):
    professores = Professor.objects.all();
    context = {'professores': professores}
    
    return render(request, 'telas/cadastro-professor.html', context)


@login_required(login_url='/login')
def cadastro_turma(request):
    context = {
        'escolas': Escola.objects.all(),
        'series': Serie.objects.all(),
        'turmas': Turma.objects.all()
    }
    
    return render(request, 'telas/cadastro-turma.html', context)


@login_required(login_url='/login')
def matricula_aluno(request):
    context = {
        'alunos': Aluno.objects.all(),
        'turmas': Turma.objects.all(),
        'matriculas': Matricula.objects.all(),
    }
    
    return render(request, 'telas/matricula-aluno.html', context)
    

@login_required(login_url='/login')
def lotacao_professor(request):
    context = {
        'professores': Professor.objects.all(),
        'turmas': Turma.objects.all(),
        'lotacoes': Lotacao.objects.all(),
    }
    
    return render(request, 'telas/lotacao-professor.html', context)


@login_required(login_url='/login')
def relatorio(request):
    context = {
        'total_alunos': Aluno.objects.count(),
        'total_professores': Professor.objects.count(),
        'turmas': Turma.objects.all(),
        'series': Serie.objects.all(),
    }
    
    return render(request, 'relatorio.html', context)


def submit_aluno(request):
    if request.POST:
        nome = request.POST.get('nome')
        serie_id = request.POST.get('serie')
        serie = Serie.objects.get(id=serie_id)
        
        try:
            Aluno.objects.create(nome=nome, serie=serie)
            messages.success(request, f'Aluno: {nome} cadastrado')
        except:
            messages.error(request, "Erro: Aluno já cadastrado.")
            
    return redirect('../cadastro-aluno/')
    
    
def submit_professor(request):
    if request.POST:
        nome = request.POST.get('nome')
        
        try:
           Professor.objects.create(nome=nome)
           messages.success(request, f'Professor: {nome} cadastrado.')
        except:
           messages.error(request, "Erro: professor já cadastrado.")
        
    return redirect('../cadastro-professor/')


def submit_turma(request):
    if request.POST:
        nome = request.POST.get('nome')
        escola_id = request.POST.get('escola')
        serie_ids = request.POST.getlist('series')
        escola = Escola.objects.get(id=escola_id)
        
        try:
            turma = Turma.objects.create(nome=nome, escola=escola)
        
            for i in serie_ids:
                turma.series.add(Serie.objects.get(id=i))
            
            messages.success(request, f'Turma: {nome} cadastrada.')
        except:
            messages.error(request, "Erro ao salvar os dados.")
            
    return redirect('../cadastro-turma/')


def submit_matricula(request):
    if request.POST:
        aluno_id = request.POST.get('aluno')
        turma_id = request.POST.get('turma')
        aluno = Aluno.objects.get(id=aluno_id)
        turma = Turma.objects.get(id=turma_id)
        
        try:
            Matricula.objects.create(aluno=aluno, turma=turma)
            messages.success(request, f'Aluno {aluno} na Turma {turma}.')
        except:
            messages.error(request, "Erro ao salvar os dados.")
            
    return redirect('../matricula-aluno/')


def submit_lotacao(request):
    if request.POST:
        professor = Professor.objects.get(id=request.POST.get('professor'))
        turma = Turma.objects.get(id=request.POST.get('turma'))
        
        try:
           Lotacao.objects.create(professor=professor, turma=turma)
           messages.success(request, 'Professor/turma cadastrada.')
        except:
           messages.error(request, "Erro ao salvar os dados.")
        
    return redirect('../lotacao-professor/')


#******* views para consulta de dados. ******

@login_required(login_url='/login')
def consulta_alunos(request, turma_id):
    turma = Turma.objects.get(id=turma_id);
    matriculas = Matricula.objects.filter(turma=turma)
    lista_alunos = []
    
    for matricula in matriculas:
        aluno = Aluno.objects.get(id=matricula.aluno_id)
        lista_alunos.append({
            'nome': aluno.nome, 
            'serie': str(aluno.serie)
        })
    
    dados = {'alunos': lista_alunos}
    
    return JsonResponse(dados)


@login_required(login_url='/login')
def consulta_professores(request):
    professores = Professor.objects.all()
    lista_prof = []
    
    for prof in professores:
        lista_turmas = []
        lotacoes = Lotacao.objects.filter(professor=prof)
        
        for lotacao in lotacoes:
            lista_turmas.append(lotacao.turma.nome)
        
        lista_prof.append({
            'nome': prof.nome,
            'turmas': lista_turmas
        })
    
    dados = {'professores': lista_prof}
    
    return JsonResponse(dados)


@login_required(login_url='/login')
def consulta_turmas(request, serie_id=None):
    turmas = None
    
    if not serie_id:
        turmas = Turma.objects.all()
    else:
        serie = Serie.objects.get(id=serie_id)
        turmas = Turma.objects.filter(series=serie)
    
    lista_turmas = []
    
    for turma in turmas:
        lista_series = []
        series_ids = turma.series.values('id')
        series = Serie.objects.filter(id__in=series_ids)
        
        for serie in series:
            lista_series.append(str(serie))
        
        lista_turmas.append({
            'nome': turma.nome,
            'series': lista_series,
            'id': turma.id,
        })
        
    dados = {'turmas': lista_turmas}
    
    return JsonResponse(dados);