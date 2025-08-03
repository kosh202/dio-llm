import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from pathlib import Path
import tensorflow as tf

# Caminho do dataset
data_dir = Path("dataset/flower_photos")

# Lista de categorias
classes = [d.name for d in data_dir.iterdir() if d.is_dir()]
print("Categorias encontradas:", classes)

# Mostrar 1 imagem de cada categoria
for categoria in classes:
    pasta = data_dir / categoria
    img_path = next(pasta.iterdir())  # primeira imagem
    img = mpimg.imread(img_path)
    plt.imshow(img)
    plt.title(categoria)
    plt.axis('off')
    plt.show()

# Tamanho padrão para ResNet50
IMG_SIZE = (224, 224)

def carregar_e_preprocessar(img_path):
    img = tf.keras.utils.load_img(img_path, target_size=IMG_SIZE)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, axis=0)  # batch
    img_array = tf.keras.applications.resnet50.preprocess_input(img_array)
    return img_array
