from django.db import models
from django.contrib.auth.models import User

class Flor(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='flores/', blank=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    flor = models.ForeignKey(Flor, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    observacao = models.TextField(blank=True)
    data_pedido = models.DateTimeField(auto_now_add=True)


class Carrinho(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    flor = models.ForeignKey(Flor, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data_adicao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.cliente.username} - {self.flor.nome}"