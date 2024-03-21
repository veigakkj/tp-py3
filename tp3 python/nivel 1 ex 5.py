def romano_para_decimal(romano):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    for i in range(len(romano)):
        if i > 0 and romanos[romano[i]] > romanos[romano[i - 1]]:
            decimal += romanos[romano[i]] - 2 * romanos[romano[i - 1]]
        else:
            decimal += romanos[romano[i]]
    return decimal

def decimal_para_romano(decimal):
    valores = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
               (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
               (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    romano = ''
    for valor, letra in valores:
        while decimal >= valor:
            romano += letra
            decimal -= valor
    return romano

# Teste do conversor de número romano para decimal
numero_romano = input("Digite um número romano: ").upper()
decimal = romano_para_decimal(numero_romano)
print("Número decimal correspondente:", decimal)

# Teste do conversor de número decimal para romano
numero_decimal = int(input("Digite um número decimal: "))
romano = decimal_para_romano(numero_decimal)
print("Número romano correspondente:", romano)