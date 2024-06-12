''' Estudos sobre a função len() para contagem de caracteres em um string ...

Autor: Daniel Caixeta - @dfcaixeta - Data: 15.abr.2024 '''

print()
print('RESULTADOS ...')

# Criando a lista de convidados
convidados = ['Mari', 'Peu', 'Nath', 'Fábio', 'Beth', 'Dan', 'Chica', 'Luiggi', 'Gigio', 'Dácio', 'Eurides', 'Rita', 'Fátima'
               'Clara', 'Duda', 'Eva', 'Michel']

print()
print('Foram convidados', len(convidados), 'pessoas!!!')
print('¬' * 20)

print()

# Contando os caracteres de uma string PARTE 1.
ice_cream = 'Adoro sorvete de morango'
print('A frase "Eu adoro sorvete de morango tem"', len(ice_cream), 'caracteres!')
print('¬' * 20)
print()

# Contando os caracteres de uma string PARTE 2. 
nomeCliente = 'Daniel Caixeta'
print('O nome do cliente tem', len(nomeCliente), 'letras')
print('¬' * 20)
print()

# Contado elementos de uma lista.
lista = ['Beth', 'Dan', 'Peu', 'Mari', 'Clara']
print('A lista contem', len(lista), 'nomes!')
print('¬' * 20)
print()

# Contando e imprimindo uma lista de elementos.
cores = ['a. Vermelho = 1', 'b. Azul = 2', 'c. Amarelo = 3', 'd. Verde = 4', 'e. Branco = 5']

print('A lista de cores é:')
print()
for cor in range(0, len(cores)):
    print(cores[cor])

print('¬' * 20)
print()

# EOF
