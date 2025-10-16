# Resumo: Demonstra formatação com f-strings: alinhamento (direita e centro), casas decimais e formatação hexadecimal com preenchimento.
variavel = 'ABC'

print (f'{variavel}')
print (f'{variavel: >10}')
print (f'{variavel: ^10}')
print (f'{1220093.010029102010:.2f}')
print (f'O hexadecimal de 1500 é {1500:08x}')
