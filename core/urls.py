from django.contrib import admin
from django.urls import path
from django.http import HttpResponse  # Adicione isso

def home(request):  # Função de teste para exibir no navegador
    return HttpResponse("Olá, Django está funcionando!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Rota principal
]
