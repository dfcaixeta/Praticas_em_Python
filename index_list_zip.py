'''
Algoritmo em Python que cria listas com indices de assuntos usando o metodo zip().
O método Zip é usado para compactar o índice e os valores de uma vez, temos que
passar duas listas uma lista é de elementos de índice e outra lista é de elementos.
Autor: Daniel Caixeta @dfcaixeta 06.jun.2023.
'''

# Criar uma lista de índice que armazena a lista.
indexlist = [0, 1, 2, 3, 4, 5]

# Cria uma lista com os assuntos.
data = ['Java', 'Python', 'HTML', 'PHP', 'C++', 'Mojo']

# Imprime os indices e valores na lista.  
print('Indices e valores na lista: ')
print()

# Obtenha os valores dos índices usando o método zip.

for index, value in zip(indexlist, data):
    print(index, value, sep=' - ')

print()

# EOF