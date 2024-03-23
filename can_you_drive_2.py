''' Algoritmo em Python com estrutura condicional IF e operador lógico AND que pergunta
sem tem idade para dirigir. (Versão 2). (Em inglês).
autor: Daniel Caixeta @dfcaixeta em 01.jul.2023 '''

age = 15

has_permit = True

if age > 16 and has_permit:
    print('Can drive!', 'You', age, 'years old!')

else:
    print('You cannot drive yet!')

print()

# EOF