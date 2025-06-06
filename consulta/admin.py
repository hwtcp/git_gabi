from django.contrib import admin
from .models import Paciente, Especialidade, Medico, Especialidade, Consulta, Prontuario

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Especialidade)
admin.site.register(Consulta)
admin.site.register(Prontuario)
