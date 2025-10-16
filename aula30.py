# Resumo: Loop de 1 a 100 imprimindo números; pula o 6 e o intervalo 10–27 com 'continue' e interrompe no 40 com 'break'.
# Ao final, exibe "Acabou".
contador = 0

while contador <=100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6')
        continue


    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

print("Acabou")
