import cv2
import os
import numpy as np
import pickle

# Caminho das faces recortadas
caminho_faces = "dataset/faces/Original Images"
tamanho_padrao = (200, 200)

# Listas para imagens e labels
imagens, labels = [], []
label_id = 0
pessoa_ids = {}

# Carrega rostos e associa a um label numérico
for pessoa in os.listdir(caminho_faces):
    pessoa_path = os.path.join(caminho_faces, pessoa)
    if not os.path.isdir(pessoa_path):
        continue

    pessoa_ids[pessoa] = label_id

    for arquivo in os.listdir(pessoa_path):
        caminho_arquivo = os.path.join(pessoa_path, arquivo)
        imagem = cv2.imread(caminho_arquivo, cv2.IMREAD_GRAYSCALE)

        if imagem is None:
            continue

        imagem_redimensionada = cv2.resize(imagem, tamanho_padrao)
        imagens.append(imagem_redimensionada)
        labels.append(label_id)

    label_id += 1

# Converte listas para arrays compatíveis
labels = np.array(labels)

# Cria e treina o reconhecedor
modelo = cv2.face.LBPHFaceRecognizer_create()
modelo.train(imagens, labels)
modelo.save("modelo_reconhecimento.yml")

# Salva dicionário de nomes
with open("labels.pkl", "wb") as f:
    pickle.dump(pessoa_ids, f)

print("✅ Modelo treinado e salvo com sucesso.")
