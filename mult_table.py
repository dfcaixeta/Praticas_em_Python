''' Tabuada de multiplicação em Python ...
Código de autoria Francisco Chaves  <<https://franciscochaves.com.br/blog/tabuada-em-python>>
Alterado @dfcaixeta em 09.abr.23.
'''

print('')
value = int(input('Enter number to table: '))
aux = 0

print('')
print('-' * 18)
print('Multiplication table for {}' .format(value))
print('-' * 18)

while(aux <= 15):
    print('{0} x {1} = {2}' .format(aux, value, (aux * value)))
    aux = aux + 1
    
print('')
# EOF