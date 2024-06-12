''' Programa em Python que processa imagens, fotos, etc. Precisa instalar a biblioteca (library) PIL.
E.g.: pip install pillow

O PIL, sigla para Python Imaging Library, é uma biblioteca de processamento de imagens bastante utilizada em Python.
Oferece funcionalidades e recursos para manipulação, edição e processamento de imagens.
Permite que os desenvolvedores Python trabalhem com imagens de forma eficiente e flexível.
Formatos: JPEG, PNG, GIF, BMP, etc. Permite também a aplicação de filtros.

Autor: Daniel Caixeta - @dfcaixeta - 01.abr.2024. '''

# Importando a biblioteca Pillow.
from PIL import Image, ImageFilter

# Carrega uma imagem.
imagem1_original = Image.open('E:/Repo_Codes/Praticas_em_Python/Imagens_processadas/Fotos_processar.jpg')

# Redimensiona a imagem original para uma largura de 600 pixels.
nova_largura = 600
nova_altura = int(imagem1_original.size[1] * (nova_largura / imagem1_original.size[0]))
imagem1_redimensionada = imagem1_original.resize((nova_largura, nova_altura))

# Salvando a imagem final na pasta de interesse.
imagem1_redimensionada.save('E:/Repo_Codes/Praticas_em_Python/Imagens_processadas/imagem1_redimensionada.jpg')
print('Imagem final salva com sucesso!')

# Certifique-se de que as duas imagens tenham o mesmo tamanho usnando operação de comparação.
print()
if imagem1_original.size == imagem1_redimensionada.size:
    raise ValueError("As imagens têm as mesmas dimensões!")
else:
    print('Imagens com as mesmas dimensões diferentes!')
    print()

# Exibe as informações das imagens que serão processadas
print('Informações das Imagens [...]')
print('Imagem 1: Formato:', imagem1_original.format, '- Dimensões:', imagem1_original.size,
       '- Modo:', imagem1_original.mode)
print('Imagem 2: Formato:', imagem1_redimensionada.format, '- Dimensões:', imagem1_redimensionada.size,
       '- Modo:', imagem1_redimensionada.mode)
print()

# Processamento de imagem - Aplicar um filtro de desfoque na imagem redimensionada.
imagem1_desfocada = imagem1_redimensionada.filter(ImageFilter.BLUR)

# Processamento de imagem - Aplicar um filtro de suavização na imagem redimensionada.
imagem1_suavizada = imagem1_redimensionada.filter(ImageFilter.SHARPEN)

# Processamento de imagem - Aplicar um filtro cinza na imagem redimensionada.
imagem1_cinza = Image.open('E:/Repo_Codes/Praticas_em_Python/Imagens_processadas/imagem1_redimensionada.jpg').convert('L')

# Processamento de imagem - Aplicar um filtro sepia na imagem redimensionada.
def apply_sepia(image):
    # Define a matriz de conversão para o efeito sépia
    sepia_matrix = [
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ]

    # Aplica a matriz de conversão à imagem
    sepia_image = image.copy()
    width, height = sepia_image.size

    for y in range(height):
        for x in range(width):
            r, g, b = sepia_image.getpixel((x, y))
            sepia_r = min(255, int(r * sepia_matrix[0][0] + g * sepia_matrix[0][1] + b * sepia_matrix[0][2]))
            sepia_g = min(255, int(r * sepia_matrix[1][0] + g * sepia_matrix[1][1] + b * sepia_matrix[1][2]))
            sepia_b = min(255, int(r * sepia_matrix[2][0] + g * sepia_matrix[2][1] + b * sepia_matrix[2][2]))
            sepia_image.putpixel((x, y), (sepia_r, sepia_g, sepia_b))

    return sepia_image

# Carrega a imagem original
input_image = Image.open('E:/Repo_Codes/Praticas_em_Python/Imagens_processadas/imagem1_redimensionada.jpg')

# Aplica o efeito sépia
imagem1_sepia = apply_sepia(input_image)

# Exibe as imagens
imagem1_original.show()
imagem1_redimensionada.show()
imagem1_desfocada.show()
imagem1_suavizada.show()
imagem1_cinza.show()
imagem1_sepia.show()

# EOC