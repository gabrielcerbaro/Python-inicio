# Resumo: Declara variáveis pessoais, calcula ano de nascimento, verifica maioridade e exibe as informações formatadas.
nome = 'Gabriel'
sobrenome = 'Cerbaro'
idade = 23
ano_nasc = 2025 - idade
maior_idade =  idade >= 18 <= 59
idoso = idade >= 60
altura = 1.85

print('Nome completo:', nome, sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nasc)
print('É maior de idade:', maior_idade)
if idade >= 60:
    print('Idoso:', idoso)
print('Altura:', altura)

