from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria


def lista_produtos(request, categoria_id=None):
    categorias = Categoria.objects.all()
    if categoria_id:
        categoria = get_object_or_404(Categoria, id=categoria_id)
        produtos = Produto.objects.filter(categoria=categoria)
    else:
        produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos, 'categorias': categorias})

