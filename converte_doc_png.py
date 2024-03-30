import docx2txt

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Converter o arquivo .docx para texto
text = docx2txt.process("arquivo.docx")

# Configurar a fonte e o tamanho
font = ImageFont.truetype("arial.ttf", 14)

# Configurar a largura máxima da imagem (ajuste conforme necessário)
max_width = 800

# Quebrar o texto em várias linhas para caber na largura máxima
lines = []
line = ""
for word in text.split():
    if font.getsize(line + word)[0] <= max_width:
        line += word + " "
    else:
        lines.append(line)
        line = word + " "
lines.append(line)

# Calcular a altura da imagem com base no número de linhas e tamanho da fonte
image_height = len(lines) * font.getsize("Ag")[1]

# Criar uma imagem em branco
image = Image.new("RGB", (max_width, image_height), "white")
draw = ImageDraw.Draw(image)

# Desenhar o texto na imagem
y = 0
for line in lines:
    draw.text((0, y), line, font=font, fill="black")
    y += font.getsize("Ag")[1]

# Salvar a imagem como .png
image.save("output.png")
