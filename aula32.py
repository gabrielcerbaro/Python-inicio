frase = 'O corinthians é o maior time do brasil' \
        'Ele foi campeão mundial em 2012'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    
    if letra_atual == ' ':
        
        i += 1

        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f"A letra que apareceu mais vezes é '{letra_apareceu_mais_vezes}' ({qtd_apareceu_mais_vezes}x)")
