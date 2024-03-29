# Utilizando operador de módulo (%) para apresentar números pares
numero = 10

print("Vendo se o número é par com operador mod (%)")

if numero % 2 == 0:
    print(f"O número {numero} é par!")

else:
    print("O número é impar!")

print()
print('-' * 15)
print()

# Utilizando bitwise AND (&)
numero = 11

print("Vendo se o número é par ou impar utilizando bitwise AND (&)")

if numero & 1 == 0:
    print("O número é par!")

else:
    print("O número é impar!")

print()

# EOF