from django.db import models


class Acao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    instituicao = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    endereco = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)

    class Meta:
        db_table = 'acoes'

    def __str__(self):
        return self.nome

    
