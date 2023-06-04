'''
Algoritmo em Python que cria listas com indices de assuntos usando lista de compreensão.
Este método é usado no loop for, que é usado para obter o índice junto com o elemento
correspondente ao longo do intervalo.
Autor: Daniel Caixeta @dfcaixeta 06.jun.2023.
'''

# Cria a lista com os assunto.
data = ['Java', 'Python', 'HTML', 'PHP', 'C++', 'Mojo']

print()

# Imprime os indices na lista.  
print('Indices e valores na lista: ')

# Obtenha os índices usando o método lista de compressão.
print([i for i in range(len(data))])

# Imprime os valores na lista.
print('Valores na lista: ')

# Obtenha os valores dos índices usando o método de lista de compreensão.
print([data[i] for i in range(len(data))])

print()

# EOF