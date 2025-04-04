from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.URLField()  # URL da imagem externa
    link_compra = models.URLField()  # Link para a loja externa
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="produtos")
    preço = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
        return self.nome


