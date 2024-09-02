from django.contrib import admin

# Register your models here.
from .models import Produto, Cliente, Estoque

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'criacao', 'atualizacao', 'ativo', 'valor')

@admin.register(Cliente)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criacao', 'atualizacao', 'ativo')

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto','quantidade')
