# Resumo: Laço while que solicita o nome ao usuário, exibe a resposta formatada uma vez e interrompe com 'break'.
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    break
