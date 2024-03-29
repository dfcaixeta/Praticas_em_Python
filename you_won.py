''' Algoritmo em Python que informa se com a pontuação alcançada o atleta
venceu ou não.
Autor: Daniel Caixeta @dfcaixeta 01.jul.2023 '''

# Input data
highest_score = 100
score = 70
level = 5

print()

# Condictional structure and Operational logic
# if score > highest_score and level == 5: # Teste com AND
if score > highest_score or level == 5: # Teste com OR
    print('You won!')

else:
    print("You don't won!")

print()

# EOF