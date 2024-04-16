''' Criando um gráfico de barras de produtos A e B com as libs matplotlib e numpy

Autor: Daniel Caixeta - @dfcaixeta - 16.abr.2024 '''

# Importando as bibliotecas
from matplotlib import pyplot as plt
import numpy as np

# Quantidades de vendas para o Produto A
valores_produto_A = [6, 7, 8, 4, 4]

# Quantidades de vendas para o Produto B
valores_produto_B = [3, 12, 3, 4.1, 6]

# Cria eixo x para produto A e produto B couma separação 0.25 entre as barras.
x1 = np.arange(len(valores_produto_A))
x2 = [x + 0.25 for x in x1]

# Plota as barras x1 e x2
plt.bar(x1, valores_produto_A, width=0.25, label = 'Produto A', color = 'deepskyblue')
plt.bar(x2, valores_produto_B, width=0.25, label = 'Produto B', color = 'mediumseagreen')

# Coloca o nome dos meses como label do eixo x
meses = ['Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
plt.xticks([x + 0.25 for x in range(len(valores_produto_A))], meses)

# Coloca labels nos eixos x e y
plt.ylabel('Qtd.')
plt.xlabel('Mês')

# Insere uma legenda no gráfico
plt.legend()

# Insere o título do gráfico
plt.title('Quantidade de vendas no 1º semestre de 2024')

# Mostra p gráfico
plt.show()

