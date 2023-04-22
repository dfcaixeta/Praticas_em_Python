'''Código em Python para a conversão de temperatura Fahreneit em Celsius
autor: Daniel Caixeta @dfcaixeta - 22.abr.2023

Parâmetros de entrada:
temperaturaF = Temperatura em graus Fahrenheit (ºF).
temperaturaC = Temperatura em graus Celsius (ºC). '''

print('')
print('-' * 32)
print(' Converte Fahrenheit -> Celsius ')
print('-' * 32)
print('')

# Parâmetro de entrada (input)
temperaturaF= input('Digite uma temperatura Fahrenheit: ')

# Cálculo de coversão ... (Throughput)
temperaturaC = (float(temperaturaF) - 32) * 5 / 9

# Resultado da conversão (output)
print('')
print(f'A conversão de {temperaturaF} graus Fahrenheit em Celsius é {round(temperaturaC, 2)} graus')
print('')

# EOF