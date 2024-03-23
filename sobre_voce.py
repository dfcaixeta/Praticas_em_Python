''' Algoritmo em Python. Fale sobre você?
Desenvolvendo um minicurriculo (bio) para apresentação.

Autor: Daniel Caixeta @dfcaixeta - 22.mar.2024
'''

# Entrada das informações.
print('-' * 13)
print('Sobre você ...')
print('-' * 13)

print()

nome = input('Qual o seu nome? ')
idade = input('A sua idade é? ')
grad = input("Qual a sua graduação? ")
posgrad = input("Qual a sua posgraduação? ")
exp = input("Qual a sua experiência profissional? (breve texto) ")

print()

# Imprime o texto com a saída das variáveis de entrada.
print("Descrição da Bio ...")
print(f"Meu nome é {nome},", f"tenho {idade} anos e sou formado(a) em {grad} "
      f"e pós-graduado(a) em {posgrad}." f" {exp}.")

print()

# EOF