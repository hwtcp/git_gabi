from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=255, null=True)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Especialidade(models.Model):
    nome = models.CharField(max_length=255, null=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=255, null=True)
    crm = models.CharField(max_length=20, null=True)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # Relação many-to-many sem modelo explícito
    especialidades = models.ManyToManyField(Especialidade)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    data_hora = models.DateTimeField(null=True)
    motivo = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consulta - {self.paciente.nome} com Dr(a). {self.medico.nome}"

class Prontuario(models.Model):
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE, null=True)
    diagnostico = models.TextField()
    prescricao = models.TextField()
    observacoes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prontuário - {self.consulta.paciente.nome}"

