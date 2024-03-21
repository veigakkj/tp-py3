CODIGO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

def morse_para_texto(morse):
    texto = ''
    morse_invertido = {v: k for k, v in CODIGO_MORSE.items()}  # Inverte o dicionário
    for codigo in morse.split(' '):
        if codigo in morse_invertido:
            texto += morse_invertido[codigo]
    return texto

def texto_para_morse(texto):
    morse = ''
    for char in texto.upper():
        if char in CODIGO_MORSE:
            morse += CODIGO_MORSE[char] + ' '
    return morse.strip()

def main():
    while True:
        opcao = input("Escolha uma opção:\n1. Morse para Texto\n2. Texto para Morse\n3. Sair\nOpção: ")
        if opcao == '1':
            morse = input("Digite o código Morse: ")
            texto = morse_para_texto(morse)
            print("Texto traduzido:", texto)
        elif opcao == '2':
            texto = input("Digite o texto: ")
            morse = texto_para_morse(texto)
            print("Código Morse:", morse)
        elif opcao == '3':
            print("até mais!!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()