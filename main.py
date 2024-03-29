from PIL import Image
import math

# CONFIGURACOES

# digite aqui o caminho para a imagem
new_image = Image.open("foguete.png")
new_image = new_image.convert("RGB")

# escala: quanto mais proximo de 1, mais preciso
res = 10

# detalhes das sombras
long_line = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """
short_line = "@%#*+=-:. "
line = short_line




brightness_list = []
for y in reversed(range(0, new_image.height, res)):
    x_line = []
    for x in range(0, new_image.width, res):
        rgb = new_image.getpixel((x, y))
        x_line.append((rgb[0] + rgb[1] + rgb[2]) / 3)
    brightness_list.append(x_line)

line_list = []

for list in brightness_list:
    list_row = []
    for item in list:
        list_row.append(line[math.floor((item / (255 / len(line))) - 1)])
    line_list.append(list_row)

for i in reversed(range(len(line_list))):
    print(' '.join(line_list[i]))

