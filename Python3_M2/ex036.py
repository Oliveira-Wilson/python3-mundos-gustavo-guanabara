# Programa de empréstimo bancário para compra de imóvel
preço_imovel = float(input('Valor do imóvel: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Anos de financiamento: '))

parcelas_mensais = preço_imovel / (anos * 12)
limite_parcela = salario * 0.3  # 30% do salário

print(f'Para pagar uma casa de R${preço_imovel:.2f}, em {anos} anos, a parcela será de R${parcelas_mensais:.2f} mensais.')

if parcelas_mensais <= limite_parcela:
    print('Seu financiamento foi APROVADO!!!')
else:
    print('Seu financiamento foi NEGADO!!')
