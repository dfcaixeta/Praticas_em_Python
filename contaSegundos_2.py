''' Código em Python que converte segundos em dias, horas, minutos e segundos restantes.
Autor: Daniel Caixeta @dfcaixeta - 22.abr.2023
'''

# Cabeçalho
print('')
print('-' * 32)
print(' Conversão de tempo em segundos ')
print('-' * 32)

# Parâmetros de entrada

print('')
segundos = int(input('Quantos segundos você deseja converter? '))

total_segundos = int(segundos)

# Cálculos para a conversão ...

dias = segundos // 86400
horas = total_segundos // 3600
segs_restantes = total_segundos % 3600
minutos = segs_restantes //60
segs_restantes_final = segs_restantes % 60

# Imprime o resultado ...

print('')
print(f'{segundos} segs. correspondem a', dias, 'dias', horas, 'hrs', minutos, 
      'min e', segs_restantes_final, 'segs.')
print('')

# EOF