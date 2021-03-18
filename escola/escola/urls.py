"""escola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('cadastro-aluno/', views.cadastro_alunos),
    path('cadastro-aluno/submit', views.submit_aluno),
    path('cadastro-professor/', views.cadastro_professor),
    path('cadastro-professor/submit', views.submit_professor),
    path('cadastro-turma/',views.cadastro_turma),
    path('cadastro-turma/submit', views.submit_turma),
    path('matricula-aluno/', views.matricula_aluno),
    path('matricula-aluno/submit', views.submit_matricula),
    path('lotacao-professor/', views.lotacao_professor),
    path('lotacao-professor/submit', views.submit_lotacao),
    path('relatorio/', views.relatorio),
    path('relatorio/consulta-alunos/<turma_id>/', views.consulta_alunos),
    path('relatorio/consulta-professores/', views.consulta_professores),
    path('relatorio/consulta-turmas/', views.consulta_turmas),
    path('relatorio/consulta-turmas/<serie_id>/', views.consulta_turmas),
]
