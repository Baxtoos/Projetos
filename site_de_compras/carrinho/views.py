from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from produtos.models import Produto
from .models import Carrinho, ItemCarrinho

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)

    item, criado = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
    if not criado:
        item.quantidade += 1
        item.save()

    return redirect('ver_carrinho')


@login_required
def remover_do_carrinho(request, produto_id):
    carrinho = get_object_or_404(Carrinho, usuario=request.user)
    item = ItemCarrinho.objects.filter(carrinho=carrinho, produto_id=produto_id).first()
    if item:
        item.delete()
    return redirect('ver_carrinho')


@login_required
def alterar_quantidade(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario=request.user)
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade', 1))
        if quantidade > 0:
            item.quantidade = quantidade
            item.save()
        else:
            item.delete()
    return redirect('ver_carrinho')


from collections import defaultdict

@login_required
def ver_carrinho(request):
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
    itens = ItemCarrinho.objects.filter(carrinho=carrinho).select_related('produto__vendedor')

    itens_por_vendedor = defaultdict(list)
    total_geral = 0

    for item in itens:
        vendedor = item.produto.vendedor
        subtotal = item.quantidade * item.produto.preco
        total_geral += subtotal
        itens_por_vendedor[vendedor].append({
            "item": item,
            "produto": item.produto,
            "quantidade": item.quantidade,
            "subtotal": subtotal
        })

    return render(request, "carrinho.html", {
        "itens_por_vendedor": dict(itens_por_vendedor),
        "total_geral": total_geral
    })

