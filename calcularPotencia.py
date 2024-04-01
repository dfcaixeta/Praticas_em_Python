''' Programa em Python para calcular a potência de números inteiros (base e expoente)
através de uma função personalizada.

Autor: Daniel Caixeta - @dfcaixeta - 01.abr.2024 '''

# Definindo a função personalizada no Python.
def potencia(base, expoente):
    resultado = (base ** expoente)
    return (resultado)

# Recebendo os dados de entrada.
base = int(input("Entre com o valor da base: "))
expoente = int(input("Entre com o valor do expoente: "))

# Cálculo da potência.
resultado = potencia(base, expoente)

# Imprime o resultado
print()
print(f'O resultado da potência é de base {base} e expoente {expoente}:', resultado)
print()

# EOC
