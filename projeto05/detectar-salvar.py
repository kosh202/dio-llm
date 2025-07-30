import cv2
import os
from tqdm import tqdm

# Caminhos
origem = "dataset/Original Images/Original Images"
destino = "dataset/faces/Original Images"

# Carregador Haarcascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Lista de pessoas
pessoas = os.listdir(origem)

# Processa cada pessoa
for pessoa in tqdm(pessoas, desc="Processando pessoas"):
    pasta_origem = os.path.join(origem, pessoa)
    pasta_destino = os.path.join(destino, pessoa)
    os.makedirs(pasta_destino, exist_ok=True)

    # Itera sobre imagens
    for img_nome in os.listdir(pasta_origem):
        caminho_img = os.path.join(pasta_origem, img_nome)
        img = cv2.imread(caminho_img)

        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for i, (x, y, w, h) in enumerate(faces):
            rosto = img[y:y+h, x:x+w]
            nome_saida = f"{os.path.splitext(img_nome)[0]}_{i}.jpg"
            caminho_saida = os.path.join(pasta_destino, nome_saida)
            cv2.imwrite(caminho_saida, rosto)
