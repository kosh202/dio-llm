from PIL import Image

# 1. Carregar imagem colorida
imagem_colorida = Image.open("img.png")  # Substitua pelo caminho da sua imagem

# 2. Converter para tons de cinza (grayscale)
imagem_cinza = imagem_colorida.convert("L")  # 'L' = luminância (0-255)

# 3. Converter para binarizada (preto e branco)
limiar = 128
imagem_binaria = imagem_cinza.point(lambda x: 255 if x > limiar else 0, mode='1')  # '1' = 1 bit por pixel (PB)

# 4. Mostrar as imagens
imagem_colorida.show(title="Colorida")
imagem_cinza.show(title="Cinza")
imagem_binaria.show(title="Binária")

# 5. Salvar as imagens
imagem_cinza.save("img_cinza.png")
imagem_binaria.save("img_bin.png")
