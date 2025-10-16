# Resumo: Usa o operador "in" para verificar se um texto digitado está presente no nome informado e exibe a mensagem correspondente.
# nome = 'Gabriel'
# # print(nome[2])
# # print(nome[-4])
# print('r' in nome)
# print('r' not in nome)

nome = input('Digire seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
