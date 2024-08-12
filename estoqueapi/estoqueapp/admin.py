from django.contrib import admin

# Register your models here.
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'criacao', 'atualizacao', 'ativo')
