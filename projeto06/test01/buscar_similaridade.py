# buscar_similares.py
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os
from sklearn.metrics.pairwise import cosine_similarity

# Caminho para os embeddings salvos
VETORES_PATH = "vetores.npy"
CAMINHOS_PATH = "caminhos.npy"

# Carregar os vetores e os caminhos das imagens
vetores = np.load(VETORES_PATH)
caminhos = np.load(CAMINHOS_PATH)

print(f"Embeddings carregados: {vetores.shape}")
print(f"Total de imagens: {len(caminhos)}")

# Função para extrair vetor de uma imagem de consulta
def extrair_vetor_imagem(img_path):
    from visualizar_padronizar import carregar_e_preprocessar
    from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

    IMG_SIZE = (224, 224)
    modelo = ResNet50(weights="imagenet", include_top=False, pooling="avg")

    img_array = np.array(carregar_e_preprocessar(img_path).numpy(), copy=True)  # força conversão + cópia
    # Não faz expand_dims se já tiver 4 dimensões
    if img_array.ndim == 3:  
        img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)


    vetor = modelo.predict(img_array)
    return vetor

# Função para buscar imagens similares
def buscar_similares(img_path, top_k=5):
    vetor_consulta = extrair_vetor_imagem(img_path)
    similaridades = cosine_similarity(vetor_consulta, vetores)[0]
    indices_ordenados = np.argsort(similaridades)[::-1]

    print(f"\nImagens mais parecidas com: {img_path}")
    plt.figure(figsize=(10, 5))

    # Mostrar imagem de consulta
    plt.subplot(1, top_k + 1, 1)
    plt.imshow(plt.imread(img_path))
    plt.title("Consulta")
    plt.axis("off")

    # Mostrar top_k resultados
    for i, idx in enumerate(indices_ordenados[:top_k]):
        plt.subplot(1, top_k + 1, i + 2)
        plt.imshow(plt.imread(caminhos[idx]))
        plt.title(f"Sim: {similaridades[idx]:.2f}")
        plt.axis("off")

    plt.savefig("resultado.png")
    print("✅ Resultado salvo como resultado.png")


# ================================
# USO:
# Altere o caminho abaixo para a imagem de teste
# ================================
imagem_teste = "dataset/flower_photos/daisy/100080576_f52e8ee070_n.jpg"
buscar_similares(imagem_teste, top_k=5)
