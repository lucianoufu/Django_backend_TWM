from rest_framework import serializers
from .models import tb_pessoa, tb_professor, tb_escola, tb_estudante, tb_disciplina, tb_disciplina_estudante, tb_professor_escola, tb_enem

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_pessoa
        fields = ('id', 'nome', 'login', 'senha')

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tb_professor
        fields = ('id','id_pessoa')

class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_escola
        fields = ('id', 'nome_escola', 'cep', 'coordenada')

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_estudante
        fields = ('id', 'id_pessoa', 'id_escola', 'serie_atual')

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_disciplina
        fields = ('id', 'id_professor', 'nome_classe', 'nome_materia')

class DisciplinaEstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_disciplina_estudante
        fields = ('id', 'id_estudante', 'id_disciplina', 'notas1', 'notas2', 'notas3', 'notas4', 'faltas')

class ProfessorEscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_professor_escola
        fields = ('id', 'id_professor', 'id_escola')

class EnemSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_enem
        fields = ('id', 'media', 'ano')