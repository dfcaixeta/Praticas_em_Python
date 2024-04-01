''' Programa que calcula áreas de figuras geométricas apresentando fórmulas matemática.
É necessário importar a biblioteca math e usar a função def para selecionar a fórmula de interesse.

Passo a passo:
1. Definir quais figuras geométricas terão as áreas cálculas.
2. Importar a biblioteca math do Python (para o valor de Pi) para o cálculo do círculo.
3. Definir as funções (e.g. def função(entrada de dados):)
                                 return fórmula
4. Imprimir MENU de OPÇÕES:
    1. Quadrado
    2. Retângulo
    3. Triângulo
    4. Círculo

5. Escolher uma das opções no MENU.
6. Fazer estrutura condicional IF ...ELIF ... ELSE para atender as opções acima.
7. Arrendondar os resultados em duas casas decimais. E.g. round(area, 2).

Autor: Daniel Caixeta - @dfcaixeta - 01.abr.2024
 '''

# Importando a biblioteca para termos o valor de Pi.
import math

# Função calcular a área de um Quadrado.
def calcular_area_quadrado(lado):
    return (lado ** 2)

# Função calcular a área de um Retângulo.
def calcular_area_retangulo(base, altura):
    return (base * altura)

# Função calcular a área de um Triângulo.
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Função calcular a área de um Círculo.
def calcular_area_circulo(raio):
    return math.pi * (raio ** 2)

# Função calcular o Volume de um Cubo.
def calcular_volume_cubo(aresta):
    return (aresta ** 3)

# Função sair do programa.
def sair_do_programa():
    return (None)

def escolher_formula_e_calcular_area():
    print("Escolha a forma geométrica para calcular a área:")
    print()
    print("1. Quadrado")
    print("2. Retângulo")
    print("3. Triângulo")
    print("4. Círculo")
    print("5. Volume Cubo")
    print("0. Sair")
    print()
    
    escolher = input("Digite o número que corresponde com a fórmula de interesse: ")
    print()

    # Calcular a área de Quadrado.  
    if escolher == "1":
        lado = float(input("Digite a medida do lado (cm): "))
        area = calcular_area_quadrado(lado)
        print()
        print(f"A área do quadrado é: {round(area, 2)} cm²")
        print()

    # Calcular a área do Retângulo. 
    elif escolher == "2":
        base = float(input("Digite a medida da base (cm): "))
        altura = float(input("Digite a medida da altura (cm): "))
        area = calcular_area_retangulo(base, altura)
        print()
        print(f"A área do retângulo é: {round(area, 2)} cm².")
        print()

    # Calcular a área do Triângulo. 
    elif escolher == "3":
        base = float(input("Digite a medida da base (cm): "))
        altura = float(input("Digite a medida da altura (cm): "))
        area = calcular_area_triangulo(base, altura)
        print()
        print(f"A área do triângulo é: {round(area, 2)} cm².")
        print()

     # Calcular a área do Círculo.
    elif escolher == "4":
        raio = float(input("Digite o raio do círculo: "))
        area = calcular_area_circulo(raio)
        print()
        print(f"A área do círculo é: {round(area, 2)} cm².")
        print()

    # Calcular o Volume de um Cubo.
    elif escolher == '5':
        aresta = float(input("Digite a aresta do cubo: "))
        volume = calcular_volume_cubo(aresta)
        print()
        print(f'O volume do cubo é: {round(volume, 2)} cm².')
        print()

    # Sair do programa.
    elif escolher == '0':
        print(f'Saída do programa!')
        print()

    # Sair do programa quando a escolha da opção é inválida.
    else:
        print("Escolha inválida.")
        print()

escolher_formula_e_calcular_area()

# EOC