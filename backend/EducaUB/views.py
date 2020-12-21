from django.shortcuts import render
from django.http import JsonResponse
import psycopg2
from django.views.decorators.http import require_http_methods

# Create your views here.
from rest_framework import viewsets
from .serializers import PessoaSerializer, ProfessorSerializer, EscolaSerializer, EstudanteSerializer, DisciplinaSerializer, DisciplinaEstudanteSerializer, ProfessorEscolaSerializer, EnemSerializer
from .models import tb_pessoa, tb_professor, tb_escola, tb_estudante, tb_disciplina, tb_disciplina_estudante, tb_professor_escola, tb_enem

class PessoaView(viewsets.ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = tb_pessoa.objects.all() #SELECT * FROM tb_pessoa -> json

class ProfessorView(viewsets.ModelViewSet):
    queryset = tb_professor.objects.all()
    serializer_class = ProfessorSerializer

class EscolaView(viewsets.ModelViewSet):
    serializer_class = EscolaSerializer
    queryset = tb_escola.objects.all()

class EstudanteView(viewsets.ModelViewSet):
    serializer_class = EstudanteSerializer
    queryset = tb_estudante.objects.all()

class DisciplinaView(viewsets.ModelViewSet):
    serializer_class = DisciplinaSerializer
    queryset = tb_disciplina.objects.all()

class DisciplinaEstudanteView(viewsets.ModelViewSet):
    serializer_class = DisciplinaEstudanteSerializer
    queryset = tb_disciplina_estudante.objects.all()

class ProfessorEscolaView(viewsets.ModelViewSet):
    serializer_class = ProfessorEscolaSerializer
    queryset = tb_professor_escola.objects.all()

class EnemView(viewsets.ModelViewSet):
    serializer_class = EnemSerializer
    queryset = tb_enem.objects.all()

def ListaClasseView(request, prof_id):
    json_ret = []
    try:
        connection = psycopg2.connect(user = "postgres",
                                      host = "127.0.0.1",
                                      password = 'banco',
                                      database = 'Teste3',
                                      port = '5432')
        cursor = connection.cursor()
        postgresSQL_select_Query = 'SELECT nome_classe, id FROM "EducaUB_tb_disciplina" WHERE id_professor_id = ' + str(prof_id)
        print(postgresSQL_select_Query)
        cursor.execute(postgresSQL_select_Query)
        print('Selecting rows from mobile table using cursor')
        mobile_records = cursor.fetchall()
        print("Pint each row and it's columns values")
        for row in mobile_records:
            json_ret.append({'nome_classe': row[0], 'Id': row[1]})
            print('nome_classe' +  str(row[0]))
            print('Id' +  str(row[1]))
    except(Exception, psycopg2.Error) as error:
        print("Error while fecthing data from Postgres: ", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Postgres connection is clossed")
    return(JsonResponse(json_ret, safe=False))

def InformacaoClasse(request, classe_nome):
    json_ret = []
    

    try:
        connection = psycopg2.connect(user = 'postgres',
                                      host = '127.0.0.1',
                                      password = 'banco',
                                      database = 'Teste3',
                                      port = '5432')
        cursor = connection.cursor()
        postgresSQL_select_Query = '''SELECT de.id
                                      	  ,pe.nome
                                      	  ,de.notas1
										  ,de.notas2
										  ,de.notas3
										  ,de.notas4
                                      	  ,de.faltas
                                      FROM "EducaUB_tb_pessoa" as pe INNER JOIN
                                      (
                                      	  "EducaUB_tb_estudante" as es INNER JOIN
                                      	  (
                                      	  	  "EducaUB_tb_disciplina_estudante" as de INNER JOIN
                                      	  	  "EducaUB_tb_disciplina" as d ON 
                                      	  	  d.id = de.id_disciplina_id
                                      	  )
                                      	  ON de.id_estudante_id = es.id
                                      )
                                      ON pe.id = es.id_pessoa_id
                                      WHERE d.nome_classe = ''' "'" +  str(classe_nome) + "'" +  'ORDER BY nome;'
        print(postgresSQL_select_Query)                                      
        cursor.execute(postgresSQL_select_Query)
        data_records = cursor.fetchall()
        for row in data_records:
            print('\n\nNome da url: ' + classe_nome)
            json_ret.append({'Id': row[0], 'Nome': row[1], 'Notas1': row[2], 'Notas2': row[3], 'Notas3': row[4], 'Notas4': row[5], 'Faltas': row[6]})
    except(Exception, psycopg2.Error) as error:
        print(postgresSQL_select_Query)
        print("Error while fecthing data from Postgres: ", error)

    finally:
        if(connection):
            cursor.close()
            connection.close()
            print('Postgres connection is closed')
    return(JsonResponse(json_ret, safe=False))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>VIEWS PARA TESTE, NÃO USAR NO PROGRAMA FINAL<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
""" @require_http_methods(["GET", "POST"]) """
def like(request):
    json_ret = []
    """ if request.method == 'GET': """
        
    try:
        connection = psycopg2.connect(user="postgres",
                                      host="127.0.0.1",
                                      password='banco',
                                      database='EducaUB',
                                      port="5432")
        cursor = connection.cursor()
        postgreSQL_select_Query = '''SELECT e.id
                                    	,p.nome
                                    	,de.notas
                                        ,de.faltas

                                    FROM "EducaUB_tb_pessoa" as p
                                    INNER JOIN 
                                    ("EducaUB_tb_estudante" as e
                                     INNER JOIN "EducaUB_tb_disciplina_estudante" as de
                                     ON e.id = de.id_estudante_id)
                                    ON e.id_pessoa_id = p.id;
                                    '''
        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall() 

        print("Print each row and it's columns values")
        for row in mobile_records:
            json_ret.append({"id": row[0], 'nome': row[1], 'notas': row[2], 'faltas': row[3]})
            """ print(json_ret) """
            """ print("Id = ", row[0], ) """
            """ print("nome = ", row[1]) """
            """ print("notas = ", row[2]) """
            """ print("Faltas = ", row[3], "\n") """

        print(json_ret)
    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    return(JsonResponse(json_ret, safe=False))

def teste(request, my_id):
    json_ret = []
    """ if request.method == 'GET': """
        
    try:
        connection = psycopg2.connect(user="postgres",
                                      host="127.0.0.1",
                                      password='banco',
                                      database='EducaUB',
                                      port="5432")
        cursor = connection.cursor()
        postgreSQL_select_Query = 'SELECT * FROM "EducaUB_tb_pessoa" WHERE id = ' + str(my_id)
        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall() 

        print("Print each row and it's columns values")
        for row in mobile_records:
            json_ret.append({"id": row[0], 'nome': row[1], 'login': row[2], 'senha': row[3]})
            """ print(json_ret) """
            """ print("Id = ", row[0], ) """
            """ print("nome = ", row[1]) """
            """ print("Login = ", row[2]) """
            """ print("Senha = ", row[3], "\n") """

        print(json_ret)
    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    return(JsonResponse(json_ret, safe=False))


