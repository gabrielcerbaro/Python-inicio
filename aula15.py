# Resumo: Exemplo de formatação de strings com str.format usando chaves nomeadas e formatando float com 2 casas.
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato) 
