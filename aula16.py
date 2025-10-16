# Resumo: Lê nome e idade, calcula ano de nascimento e faz uma pergunta; responde diferente conforme 'sim' (case-insensitive).
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
ano_nasc = 2025 - idade
amor = input('Você ama a Gabriela? ')

print (f'O seu nome é: {nome} e sua idade é {idade}')
print(f'Seu ano de nascimento é: {ano_nasc}')


if amor.lower () == 'sim':
    print(f'Que amor!, {nome}')

else: 
    print(f'Poxa, que pena!, {nome}')
