''' Desenvolvido por Python.org ...
Alterado @dfcaixeta em 09.abr.23.
'''

# Descrição das variável fruits ...
fruits = ['Banana', 'Apple', 'Lime']

# Imprime lista original ...
loud_fruits = [fruits for fruits in fruits]
print('Imprime lista original ...')
print(loud_fruits)
print('')

# Imprime lista fruits em minúsculo ...
loud_fruits_lower = [fruits.lower() for fruits in fruits]
print('Imprime caracteres minúsculos ...')
print(loud_fruits_lower)
print('')

# Imprime lista fruits em MAIÚSCULO ...
loud_fruits_upper = [fruits.upper() for fruits in fruits]
print('Imprime caracteres MAÍSCULOS ...')
print(loud_fruits_upper)
print('')

# Imprime uma lista ennumerada de fruits.
print('Imprime lista enumerada ...')
print (list(enumerate(fruits)), " => " "Lista enumerada ...") 
print('')

# EOF