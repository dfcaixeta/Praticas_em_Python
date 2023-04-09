''' Desenvolvido por Python.org ...
Série Fibonacci ...
Alterado @dfcaixeta em 09.abr.23.
'''

# Série Fibonacci (n)
def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n

print('Imprime sequência de fibonacci ...')
for i in range(12):
    print(rec_fib(i), end = ' ')

# EOF