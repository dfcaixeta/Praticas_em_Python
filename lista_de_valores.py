# Definindo uma lista de valores

valores = [1, 2, 3, 4, 5]

# Criando um dicionário
# Compreensão de dicionário e lambda

dicionario = {x: (lambda y: y * 2)(x) \
              for x in valores}

print()
print("Imprime lista de valores do dicionário")
print(dicionario)

print()

# EOF
