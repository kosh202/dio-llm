import os
import numpy as np
from pathlib import Path
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from visualizar_padronizar import carregar_e_preprocessar  # usa a função do script anterior

# Caminho do dataset
data_dir = Path("dataset/flower_photos")

# Lista de categorias
classes = [d.name for d in data_dir.iterdir() if d.is_dir()]

# Carrega modelo ResNet50 pré-treinado, sem a última camada
base_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Função para extrair características
def extrair_caracteristicas(img_path):
    img_array = carregar_e_preprocessar(img_path)
    features = base_model.predict(img_array, verbose=0)
    return features.flatten()

vetores = []
caminhos = []

# Extrai embeddings para todas as imagens
for categoria in classes:
    pasta = data_dir / categoria
    for img_name in os.listdir(pasta):
        caminho_img = pasta / img_name
        vetor = extrair_caracteristicas(caminho_img)
        vetores.append(vetor)
        caminhos.append(str(caminho_img))

vetores = np.array(vetores)
caminhos = np.array(caminhos)

print("Formato dos vetores:", vetores.shape)
print("Exemplo de vetor:", vetores[0][:5])  # primeiros 5 valores

# Salva para usar depois na busca
np.save("vetores.npy", vetores)
np.save("caminhos.npy", caminhos)

print("Embeddings salvos!")
