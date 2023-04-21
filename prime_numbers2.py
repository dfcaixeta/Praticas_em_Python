''' Programa em python com função que recebe um número inteiro positivo n e retorna uma lista 
    com todos os números primos até n.
    Autor: 
'''

def prime_numbers(n):

    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Cabeçalho (Header)
print('-' * 25)
print('Lista com números primos')
print('-' * 25)

print('')

# Entrada do usuário
n = int(input("Digite um número inteiro positivo: "))

# Chama a função prime_numbers para obter os números primos até n
primes = prime_numbers(n)

# Exibe a lista de números primos encontrados
print('')
print("Números primos até", n, ":", primes)
print('')

# EOF