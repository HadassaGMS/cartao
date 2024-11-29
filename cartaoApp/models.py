from django.db import models

# Create your models here.
# número do cartão
# CPF do usuário
# nome do usuário igual aparece no cartão
# código de validade
# data de vencimento do cartão
class Validar(models.Model):
    id_validar = models.AutoField(primary_key=True)
    cartao_validar = models.CharField(max_length=255, null=False)
    CPF_validar = models.CharField(max_length=255, null=False)
    nome_validar = models.CharField(max_length=255, null=False)
    codigo_validar = models.CharField(max_length=255, null=False)
    data_validar = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome_validar