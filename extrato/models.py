from django.db import models
from perfil.models import Categoria, Conta
class Valores(models.Model):
    choice_tipo = (
        ('E', 'Entrada'),
        ('S', 'Saída')
    )
    
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField()
    data = models.DateField()
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=choice_tipo)

    def __str__(self):
        return self.descricao