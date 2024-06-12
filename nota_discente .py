''' Algoritmo que recebe uma nota e informa se o discente passou ou não de ano.
Autor: Daniel Caixeta @dfcaixeta em 30.mar.24.'''

print('-' * 28)
print(' INFORMAÇÕES DO(A) DISCENTE ')
print('-' * 28)
print(' MÉDIA >= 50 ')
print('-' * 28)
print()

# Entrada nome do(a) discente
discente = input("Digite o nome do(a) discente: ")

print()

# Entrada da nota com a função input ...
nota_str = input('A nota final do(a) discente: ')

# Coerção de str para int.
nota_int = (int(nota_str))

# Bloco condicional (if ... else ...).
aprovado = nota_int > 50

print()

if aprovado:
    print(f"O(a) discente {discente} passou!. Nota = {nota_int}")

else:
    print(f"O(a) discente {discente} não passou!")

print()
print('-' * 28)
print()

# EOF