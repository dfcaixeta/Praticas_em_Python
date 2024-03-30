''' Algoritmo que recebe uma nota (score) e informa se passou ou não de ano.
Autor: Daniel Caixeta @dfcaixeta em 10.jun.23.'''

print('-' * 15)
print()

# Entrada da nota com a função input ...
score_str = input('The score is: ')

# Coerção de str para int.
score_int = (int(score_str))

# Bloco condicional (if ... else ...).
pass_grade = score_int > 50

if pass_grade:
    print("Passed!")

else:
    print("Not passed!")

print()
print('-' * 15)

# EOF