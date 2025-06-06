from django.shortcuts import render
# fazer import de consulta
from .models import Consulta


# Create your views here.
def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas/consulta_list.html', {'consultas': consultas})

