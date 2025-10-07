"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero1 = input('Coloque um número inteiro: ')

try:
    numero1_conversao = int(numero1)
except ValueError:
    print('Você não digitou um número inteiro.')
else:
    if numero1_conversao % 2 == 0:
        print(f'O número {numero1} é par')
    else:
        print(f'O número {numero1} é ímpar')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input("Que horas são agora em seu local: ")

try:
    horario_conversao = int(horario)
except ValueError:
    print("Digite apenas a hora")

if horario_conversao <= 11:
    print(f'Bom dia, no seu local são {horario}h')
elif horario_conversao >= 11 <= 17:
    print(f'Boa tarde, no seu local são {horario}h')
elif horario_conversao >= 18 <= 23:
    print(f'Boa noite, no seu local são {horario}h')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Coloque seu primeiro nome: ')

if len(nome) < 4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')