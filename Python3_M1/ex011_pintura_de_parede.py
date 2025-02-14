lar = float(input('Digite a largura da parede (em metros): '))
alt = float(input('Digite a altura da parede (em metros): '))

# Calcula a área total da parede
area = lar * alt

# Calcula a quantidade de tinta necessária (1 litro para cada 2 metros quadrados)
litros_tinta = area / 2

# Exibe o resultado formatado com 2 casas decimais
print(f'A parede tem a área total de {area:.2f}m².\nPrecisa-se de {litros_tinta:.2f} litros de tinta para pintar essa parede.')
