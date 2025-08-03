import tensorflow as tf
import pathlib
import os
import shutil

# URL oficial do dataset
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"

# Baixa e extrai
data_dir = tf.keras.utils.get_file(
    origin=dataset_url,
    untar=True
)

# Garante que a pasta 'dataset/flower_photos' exista
destino = pathlib.Path("dataset/flower_photos")
os.makedirs(destino, exist_ok=True)

# Move o conteúdo da pasta baixada para dentro de dataset/flower_photos
origem = pathlib.Path(data_dir)
for item in origem.iterdir():
    shutil.move(str(item), destino)

print("✅ Dataset salvo em:", destino.absolute())
