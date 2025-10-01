nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade == '':
    print('Desculpe, você deixou campos vazios')
else:
    print(f'Seu nome é {nome}, você tem {idade} anos.')
    print(f'Seu nome invertido é:', nome[::-1])
    print('Seu nome tem ', len(nome), 'caracteres')
    print(f'A primeira letra do seu nome é:', nome[0])
    print(f'A última letra do seu nome é:', nome[-1])
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')



