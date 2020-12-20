"""backend URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from EducaUB import views
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register(r'pessoa', views.PessoaView, 'pessoa')
router.register(r'professor', views.ProfessorView, 'professor')
router.register(r'escola', views.EscolaView, 'escola')
router.register(r'estudante', views.EstudanteView, 'estudante')
router.register(r'disciplina', views.DisciplinaView, 'disciplina')
router.register(r'disciplinaestudante', views.DisciplinaEstudanteView, 'disciplinaestudante')
router.register(r'professorescola', views.ProfessorEscolaView, 'professorescola')
router.register(r'enem', views.EnemView, 'enem')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/informacaoclasse/<str:classe_nome>', csrf_exempt(views.InformacaoClasse)),
    path('api/listaclasse/<int:prof_id>', csrf_exempt(views.ListaClasseView)),
    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>URLS ABAIXO É PARA TESTE, NÃO USAR NO PROGRAMA FINAL<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    path('api/like/', csrf_exempt(views.like)),
    path('api/teste/<int:my_id>', csrf_exempt(views.teste))
]