from django.db import models

# Create your models here.
class tb_pessoa(models.Model):
    nome      = models.TextField(max_length = 255)
    login     = models.TextField(max_length = 255)
    senha     = models.TextField(max_length = 255)

class tb_professor(models.Model):
    id_pessoa = models.ForeignKey(tb_pessoa, on_delete = models.CASCADE)

class tb_escola(models.Model):
    nome_escola = models.TextField(max_length = 255)
    cep = models.IntegerField()
    coordenada = models.TextField(max_length=20)

class tb_estudante(models.Model):
    id_pessoa   = models.ForeignKey(tb_pessoa, on_delete = models.CASCADE)
    id_escola   = models.ForeignKey(tb_escola, on_delete = models.CASCADE)
    serie_atual = models.TextField(max_length = 255)

class tb_administrador(models.Model):
    id_pessoa = models.ForeignKey(tb_pessoa, on_delete = models.CASCADE)

class tb_disciplina(models.Model):
    id_professor = models.ForeignKey(tb_professor, on_delete = models.CASCADE)
    nome_classe  = models.TextField(max_length = 255)
    nome_materia = models.TextField(max_length = 255)

class tb_disciplina_estudante(models.Model):
    id_estudante  = models.ForeignKey(tb_estudante,  on_delete = models.CASCADE)
    id_disciplina = models.ForeignKey(tb_disciplina, on_delete = models.CASCADE)
    notas1        = models.FloatField()
    notas2        = models.FloatField()
    notas3        = models.FloatField()
    notas4        = models.FloatField()
    faltas        = models.IntegerField()

class tb_professor_escola(models.Model):
    id_professor = models.ForeignKey(tb_professor, on_delete = models.CASCADE)
    id_escola    = models.ForeignKey(tb_escola, on_delete = models.CASCADE)

class tb_enem(models.Model):
    media   = models.FloatField()
    ano = models.DateField()
    id_escola = models.ForeignKey(tb_escola, on_delete = models.CASCADE)