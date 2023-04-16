''' Códigos para conversão de um número inteiro para binário, usando funções bin(),
format() e str.format() em Python.
Referência: https://www.delftstack.com/pt/howto/python/python-int-to-binary/
Modificado/alterado: Daniel Caixeta @dfcaixeta em 16.abr.23 '''

# Header to code
print('')
print('-' * 38)
print(' Binary conversion using some methods')
print('-' * 38)

# Utilizando bin(). Função para converter int para binário.

''' Em Python, podemos utilizar uma função integrada, bin() para converter um número
inteiro em binário. A função bin() toma um inteiro como parâmetro e devolve a sua
string binária equivalente prefixada com 0b.'''

binary = bin(10)
print("Print using bin() function:", binary)

# Utilizando a função format() para converter int para binário.

''' Como mostrado no exemplo anterior, o binário de um número inteiro pode ser
simplesmente obtido com o método bin(x). Mas se quiser remover o prefixo 0b da
sua saída, pode utilizar a função format e formatar a saída.

A função format(value, format_spec) tem dois parâmetros - value e format_spec, e irá retornar
uma saída formatada de acordo com a função format_spec.
Abaixo estão alguns exemplos de tipos de formatação que podem ser utilizados dentro
dos espaços reservados:

Tipo de formatação	Papel
        =           Coloca o sinal na posição mais à esquerda.
        b           Converte o valor em binário equivalente.
        o           Converte o valor para o formato octal.
        x           Converte o valor para o formato Hex.
        d           Converte o valor dado em decimal.
        E           Formato científico, com um E em maiúsculas.
        X           Converte o valor para o formato Hex em maiúsculas.
'''

print('')
bin = format(10, "b")
oct = format(10, "o")
hex_one = format(10, "x")
hex_two = format(10, "X")
sci = format(10, "E")

print('Print values using format function ...')
print('Binary =', bin, '| ' 'Octal =', oct, '| ' 'Hexa (lower) =', hex_one, '| '
       'Hexa (upper) =', hex_two)
print('Scientic format =', sci)
print('')

# Utilizando a função str.format(). Método de conversão de int para binário.

''' O método str.format() é semelhante à função format() acima e partilham o mesmo format_spec.'''

bin = "{0:b}".format(10)
oct = "{0:o}".format(10)
hex_one = "{0:x}".format(10)
hex_two = "{0:X}".format(10)
sci = format(10, "E")

print("Print values using str.format")
print('Binary =', bin, '| ' 'Octal =', oct, '| ' 'Hexa (lower) =', hex_one, '| '
       'Hexa (upper) =', hex_two)
print('Scientic format =', sci)

print('')

# EOF