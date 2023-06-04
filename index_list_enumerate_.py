'''
Algoritmo em Python que cria listas com indices de assuntos usando o método enumerate().
Este método é usado no loop for, que é usado para obter o índice junto com o elemento
correspondente ao longo do intervalo.

Autor: Daniel Caixeta @dfcaixeta 06.jun.2023.
'''

# Cria a lista com os assuntos usando o metodo enumerate().
data = ['Java', 'Python', 'HTML', 'PHP', 'C++', 'Mojo']

# Imprime a lista dos assuntos indexados.  
print('Indices e valores na lista: ')

print()
  
# Obtenha os indices e valores usando o método enumarate.
for i in enumerate(data):
    print(i)

print()

# EOF