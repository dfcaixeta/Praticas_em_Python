''' Código que apresenta os números primos <= a N (parâmetro de entrada) ...
Obs.: Perdi a autoria ...!!!!!
Modificado @dfcaixeta em 09.abr.23.'''

import math

# Entrada: um inteiro n > 1.
print('Digite um número inteiro n > 1')

print('')

numb = int(input("Digite n: "))

''' Gera uma matriz A de valores booleanos, indexados por inteiros de 2 a n, inicialmente
todos definidos como verdadeiros.'''

A = list(range(2, numb))

# Para i = 2, 3, 4, ..., não superior a :
for i in range(2, int(math.sqrt(numb)+1)):

  # Se a matriz A[i] é verdadeira:
  if i in A:

    # Para j = i2, i2+i, i2+2i, i2+3i, ..., não superior a n:
    for j in range(i**2, numb, i):

      # A[j] := falso.
      if j in A: A.remove(j)

# Saída: todos i na matriz A[i] sendo verdadeiro.        
print('')
print((f"Lista dos números primos <= {numb} ->"), A)
print('')

# EOF