from django.db import models

#Create your models here.

class Escola(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.nome


class Serie(models.Model):
    ano_letivo = models.IntegerField(unique=True)
    
    def __str__(self):
        return str(self.ano_letivo)
        

class Turma(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    series = models.ManyToManyField(Serie)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    
class Aluno(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome;


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.aluno} - {self.turma}'
        

class Professor(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.nome;
        

class Lotacao(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.professor} - {self.turma}'