# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    input("Login: ")
    input('Senha: ')
    print('Você entrou no sistema')

elif entrada == 'sair':
    print('Você saiu do sistema')

else:
    print('Você não digitou nem entrar e nem sair.')

# print('FORA DOS BLOCOS')

condicao1 = False
# Resumo: Demonstra uso de if/elif/else com um prompt de "entrar/sair" e um segundo bloco com múltiplas condições (apenas um deles executa).
condicao2 = True
condicao3 = False
condicao4 = False

if condicao1: 
    print('Código de condição 1')

elif condicao2:
    print('Código de condição 2')
    
elif condicao3:
    print('Código de condição 3')

elif condicao4:
    print('Código de condição 4')

else: 
    print(' ')
