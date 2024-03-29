

def menu():

    print('')
    print('Conversão de temperaturas')
    print('')

    var = int(input('''Escolha no menu a temperatura para conversão:'

    ----------------------
    | < 1 > Celsius.     |
    | < 2 > Kelvin       |
    | < 3 > Fahrenheit   |
    ----------------------

    '''))

    if var == 1:
        tempC()

    elif var == 2:
        tempK()

    elif var == 3:
        tempF()

# Celsius

def tempC():

    print("")
    inteiro = float(input("Digite a temperatura em ºC): "))
    print("")

    resultado = (inteiro - 273)

    var = int(input(''' Para calcular novamente tecle: 1
                      Para voltar ao menu principal tecle: 0


    '''))

    if var == 1:
        tempC()

    else:
        menu

# Celsius para Kelvin

tempC = float(input("Digite a temperatura em ºC: "))

tempK = tempC + 273

print("A temperatura em K é: ", tempK)


# Celsius para Fahrenheit

tempC = float(input("Digite a temperatura em ºC: "))

tempF = (tempC - 32) * 5 / 9

print("A temperatura em F é: ", tempF)