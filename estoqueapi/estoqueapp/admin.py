from django.contrib import admin

# Register your models here.
from .models import Produto, Cliente

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'criacao', 'atualizacao', 'ativo', 'valor')

@admin.register(Cliente)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criacao', 'atualizacao', 'ativo')
