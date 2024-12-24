# sistema_carrinho_compras
- Cliente

A tabela Cliente armazena informações sobre os clientes do sistema, como nome e e-mail. Cada cliente pode ter um ou mais carrinhos e pedidos.

Chave primária: id (identificador único do cliente).
- Produto
A tabela Produto armazena os itens disponíveis para compra, com informações como nome, descrição e preço.

Chave primária: id (identificador único do produto).
- Carrinho
O Carrinho representa o carrinho de compras de um cliente antes da finalização da compra. Cada cliente tem um carrinho associado, onde ele pode adicionar produtos. A tabela Carrinhocontém um campo de referência para o cliente ( cliente), que estabelece a relação entre o cliente e o carrinho.

Chave primária: id (identificador único do carrinho).
Chave estrangeira: cliente (relaciona-se ao cliente que possui o carrinho).
- ItemCarrinho
A tabela ItemCarrinho contém os produtos que foram adicionados ao carrinho. Ela registra o produto específico e a quantidade que o cliente deseja comprar. Essa tabela serve para associar produtos ao carrinho e permitir que um carrinho contenha múltiplos produtos.

Chave primária: id (identificador único do item no carrinho).
Chaves estrangeiras:
carrinho: Relacione-se ao carrinho em que o produto foi adicionado.
produto: Relaciona-se ao produto específico que foi adicionado ao carrinho.
- Pedido
O Pedido é criado quando o cliente finaliza uma compra. Ele armazena os dados e o horário da compra e está vinculado a um único cliente. Cada pedido pode conter vários produtos, que estão registrados na tabela ItemPedido. A criação de um pedido implica que o cliente finalizou a compra de todos os itens em seu carrinho.

Chave primária: id (identificador único do pedido).
Chave estrangeira: cliente (relaciona-se ao cliente que fez o pedido).
- ItemPedido
Após o pedido ser finalizado, os produtos do carrinho são transferidos para a tabela ItemPedido. Cada registro ItemPedido representa um item comprado no pedido, incluindo a quantidade do produto adquirido.

Chave primária: id (identificador único do item no pedido).
Chaves estrangeiras:
pedido: Relaciona-se ao pedido finalizado.
produto: Relacione-se ao produto comprado.
Como as Tabelas Estão Relacionadas
Aqui está o fluxo e como as tabelas estão organizadas para garantir que os itens comprados sejam garantidos aos pedidos:

Cliente com Carrinho :

Um cliente pode ter apenas um carrinho ativo . A tabela Carrinho tem uma chave estrangeira para Cliente, garantindo que cada carrinho pertença a um único cliente.
Carrinho com Itens :

O cliente pode adicionar múltiplos produtos ao seu carrinho. Cada item no carrinho é registrado na tabela ItemCarrinho, que tem referências tanto ao Carrinho(indica a qual carrinho o item pertence) quanto ao Produto(indica qual produto foi adicionado).
Carrinho para Pedido :

Quando o cliente finaliza uma compra, um novo Pedido é criado, com referência ao cliente. Este pedido representa a compra do cliente.
Itens de Carrinho para Itens de Pedido :

Após a finalização da compra, os itens no carrinho são transferidos para o pedido. A tabela ItemPedido contém os itens ItemCarrinho que foram comprados, incluindo a quantidade, produto e associando o item ao pedido finalizado. A relação entre ItemPedido e Pedido é imposta pela chave estrangeira pedido, enquanto a relação com o produto é garantida pela chave estrangeira produto.

- Relacionamentos e Chaves
As chaves primárias e estrangeiras são usadas para organizar as tabelas de maneira relacional e garantir que os dados em diferentes tabelas estejam devidamente conectados.

- Chaves Primárias e Estrangeiras
Chave Primária
Uma chave primária é usada para identificar a forma única de cada registro dentro de uma tabela. 

Cliente : A chave primária é o campo id, que é gerado automaticamente pelo Django. Este campo serve para identificar de forma única cada cliente.
Produto : Da mesma forma, o campo id é a chave primária, identificando cada produto de forma única.
Carrinho : Cada carrinho tem um campo id que é a chave primária.
ItemCarrinho : A chave primária é o campo id, que identifica de forma única cada item dentro de um carrinho.
Pedido : O campo id funciona como chave primária para os pedidos.
ItemPedido : A chave primária também é o campo id, identificando de forma única cada item dentro de um pedido.
- Chave Estrangeira (Chave Estrangeira)
Uma chave estrangeira é usada para criar uma relação entre duas tabelas. Ela aponta para a chave primária de outra tabela e garante que o valor no campo de chave estrangeira corresponda a um registro existente na tabela relacionada. No Django, usamos ForeignKeypara definir essas relações.

Cliente e Carrinho :

A classe Carrinho possui uma chave estrangeira chamada cliente, que se refere à tabela Cliente. Isso significa que cada carrinho é atribuído a um único cliente.
Relação: 1 cliente pode ter vários carrinhos (1 para muitos) .
Carrinho e ItemCarrinho :

A classe ItemCarrinho possui uma chave estrangeira chamada carrinho, que se refere à tabela Carrinho. Isso significa que cada item de carrinho pertence a um carrinho específico.
Relação: 1 carrinho pode ter vários itens (1 para muitos) .
Produto e ItemCarrinho :

A classe ItemCarrinho também possui uma chave estrangeira chamada produto, que se refere à tabela Produto. Isso significa que cada item do carrinho corresponde a um produto específico.
Relação: 1 produto pode estar presente em vários itens de carrinho (1 para muitos) .
Cliente e Pedido :

A classe Pedido tem uma chave estrangeira chamada cliente, que se refere à tabela Cliente. Isso significa que cada pedido é feito por um cliente específico.
Relação: 1 cliente pode ter vários pedidos (1 para muitos) .
Pedir e ItemPedido :

A classe ItemPedido tem uma chave estrangeira chamada pedido, que se refere à tabela Pedido. Isso significa que cada item do pedido está associado a um pedido específico.
Relação: 1 pedido pode ter vários itens (1 para muitos) .
Produto e ItemPedido :

A classe ItemPedido tem uma chave estrangeira chamada produto, que se refere à tabela Produto. Isso significa que cada item do pedido corresponde a um produto específico.
Relação: 1 produto pode estar presente em vários itens de pedido (1 para muitos) .
Como As Chaves Primárias e Estrangeiras Modelam as Relações
Cliente e Carrinho : Um cliente pode ter vários carrinhos (por exemplo, em diferentes momentos). Cada carrinho é vinculado a um cliente específico através da chave estrangeira clientena tabela Carrinho.

Carrinho e Itens : Cada carrinho pode ter vários itens. A tabela ItemCarrinho usa a chave estrangeira carrinho para vincular cada item a um carrinho específico.

Pedido e Cliente : Cada pedido é feito por um cliente. A tabela Pedido possui uma chave estrangeira cliente que vincula o pedido ao cliente que o fez.

Pedido e Itens de Pedido : Cada pedido pode ter vários itens. A tabela ItemPedido usa a chave estrangeira pedido para vincular cada item ao pedido.

Produto e Itens : O produto presente em cada item de carrinho ou pedido é condicionado através da chave estrangeira produtonas tabelas ItemCarrinhoe ItemPedido.

Para executar o comidigo da melhor maneira, pode abrir o terminal da ide do usuario que for analisar o codigo e usar o comando 'cd ecommerce' apos isso utilizar o comando 'python manage.py createsuperuser' para decidir qual vai ser o nome, email e senha do adiministrador que vai ser a pessoa que ira usar o sitema, apos usar o comando 'python manage.py createsuperuser' no terminal da ide ira aparecer algo parecido com isto:
Username (leave blank to use ' '): Nome do adimistrador 
Email address: email do adimistrador 
Password: senha 
Password (again): repetir senha
Na parte de colocar a senha, talvez não apareceça nada na tela, mas mesmo assim ainda ira funcionar, por exemplo se uma pessoa decidir usar a senha 12345 ela não ira aparecer na tela do terminal mas quando executar o codigo e ir para a pagina do adiministrador, no momento em que pedir a senha e o usuario digitar 12345 ela ira funcionar. Apos isso basta usar o comando 'python manage.py runserver' no terminal da usa ide onde logo apos isso ira aparecer um link parecido ou igual a este 'http://127.0.0.1:8000/' mas para ficar mais facil de usar a pagina do adiministrador use este 'http://127.0.0.1:8000/admin/'.
Obrigado pelo atenção estarei disponivel para qualquer esclarecimento
tel: (93) 99129-7109
Email: oi17mateus@gmail.com
