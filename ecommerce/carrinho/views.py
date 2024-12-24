from .models import Cliente, Carrinho, Pedido, ItemCarrinho, ItemPedido

def finalizar_compra(cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    carrinho = Carrinho.objects.get(cliente=cliente)

    # Cria um novo pedido
    pedido = Pedido.objects.create(cliente=cliente)

    # Transfere os itens do carrinho para o pedido
    itens_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho)
    for item in itens_carrinho:
        ItemPedido.objects.create(
            pedido=pedido,
            produto=item.produto,
            quantidade=item.quantidade
        )

    # Limpa o carrinho
    itens_carrinho.delete()
    carrinho.delete()

    return pedido

