# Solicita o preço do produto
preco_produto = float(input('Digite o preço do produto (Em R$): '))

# Calcula o valor do desconto de 5%
valor_desconto = preco_produto * 5 / 100

# Exibe o preço original e o preço com o desconto aplicado
print(f'O produto de preço R${preco_produto:.2f}, com 5% de desconto, tem o novo preço de R${preco_produto - valor_desconto:.2f}')
