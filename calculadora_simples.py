''' Programa em Python que cria uma calculadora simples.
Autor: unknow - Data: 30.mar.24 '''

# Importando as bibliotecas necessárias.
from os import system
from formulas import *

# Função que limpa a tela para a impressão dos elementos gráficos do print.
system('cls')


print('''
____ ____ _    ____ _  _ _    ____ ___  ____ ____ ____ 
|    |__| |    |    |  | |    |__| |  \ |  | |__/ |__| 
|___ |  | |___ |___ |__| |___ |  | |__/ |__| |  \ |  |                                                    

 _____________________
|  _________________  |
| |    calculadora  | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | * | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |   
|_____________________|

''')

print('Use quit() e Enter/Return para sair')
print()

while True:
    conta = input('[conta]==-> ')
    print(eval(conta))

# EOF