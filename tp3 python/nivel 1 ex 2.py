def histograma_frequencia_letras(texto):
    frequencia = {}
    for char in texto:
        if char.isalpha():
            char = char.lower()  
            frequencia[char] = frequencia.get(char, 0) + 1
    return frequencia

def exibir_histograma(frequencia):
    print("Histograma de Frequência de Letras:")
    for letra, freq in sorted(frequencia.items()):
        print(f"{letra}: {freq}")

texto = input("Digite um texto: ")
frequencia_letras = histograma_frequencia_letras(texto)
exibir_histograma(frequencia_letras)