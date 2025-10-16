# Resumo: Calcula o IMC a partir de peso e altura e imprime o resultado formatado com 2 casas decimais usando f-string.
nome = 'Gabriel Cerbaro'
altura = 1.86
peso = 124
imc = peso / altura ** 2

linha_1 = f'Olá {nome} Seu IMC é: {imc:.2f}'

print(linha_1)
