from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Produto(Base):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=12, decimal_places=6)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['id']

    def __str__(self):
        return self.descricao
    
class Cliente(Base):
    nome = models.CharField(max_length=255)    

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return self.nome
    
class Estoque(models.Model):
    produto = models.ForeignKey(Produto, related_name="produto_estoque", on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'
        unique_together = ['produto']
        ordering = ['id']

    def __str__(self):
        return f'Estoque de produto {self.produto} com um total de {self.quantidade}'
        
     
