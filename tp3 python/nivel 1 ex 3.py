def calcular_media(numeros):
    total = sum(numeros)
    media = total / len(numeros)
    return media

numeros_input = input("Digite os números separados por espaço: ")


numeros_input = numeros_input.replace(',', '.')


numeros = [float(num) for num in numeros_input.split()]

media = calcular_media(numeros)
print("A média dos números é:", media)