from random import choice

# Recebendo os nomes dos alunos
aluno_1 = input('Digite o nome do primeiro aluno: ')
aluno_2 = input('Digite o nome do segundo aluno: ')
aluno_3 = input('Digite o nome do terceiro aluno: ')
aluno_4 = input('Digite o nome do quarto aluno: ')

# Criando a lista de alunos
lista = [aluno_1, aluno_2, aluno_3, aluno_4]

# Escolhendo aleatoriamente um aluno
escolhido = choice(lista)

# Exibindo o nome do aluno escolhido
print(f'Quem vai limpar o quadro é {escolhido}')
