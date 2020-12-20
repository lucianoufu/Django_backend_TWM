from django.contrib import admin

# Register your models here.

from .models import tb_pessoa, tb_professor, tb_escola, tb_estudante, tb_administrador, tb_disciplina, tb_disciplina_estudante, tb_professor_escola, tb_enem

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'login', 'senha')

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id','id_pessoa')
 
class EscolaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_escola', 'cep', 'coordenada')

class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('id','id_pessoa', 'id_escola', 'serie_atual')

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('id','id_professor', 'nome_classe', 'nome_materia')

class DisciplinaEstudanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_estudante', 'id_disciplina', 'notas1', 'notas2', 'notas3', 'notas4', 'faltas')

class ProfessorEscolaAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_professor', 'id_escola')

class EnemAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_escola', 'media', 'ano')

admin.site.register(tb_pessoa, PessoaAdmin)
admin.site.register(tb_professor, ProfessorAdmin)
admin.site.register(tb_escola, EscolaAdmin)
admin.site.register(tb_estudante, EstudanteAdmin)
admin.site.register(tb_disciplina, DisciplinaAdmin)
admin.site.register(tb_disciplina_estudante, DisciplinaEstudanteAdmin)
admin.site.register(tb_professor_escola, ProfessorEscolaAdmin)
admin.site.register(tb_enem, EnemAdmin)