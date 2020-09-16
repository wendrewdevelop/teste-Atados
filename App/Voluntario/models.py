from django.db import models


class Voluntario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)

    class Meta:
        db_table = 'voluntarios'

    def __str__(self):
        return self.nome + ' ' + self.sobrenome