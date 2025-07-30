import cv2
import os

# Caminhos
modelo_path = "/mnt/c/Users/raphael/Desktop/github/dio-llm/projeto05/modelo_reconhecimento.yml"
pasta_imagens = "imagens_teste"  # Substitua pelo caminho das imagens de teste
pasta_faces = "dataset/faces/Original Images"  # Onde estão as pastas dos nomes

# Pasta para salvar resultados
pasta_resultados = "resultados"
os.makedirs(pasta_resultados, exist_ok=True)

# Carregar modelo
modelo = cv2.face.LBPHFaceRecognizer_create()
modelo.read(modelo_path)

# Carregar nomes (ordenados)
nomes = sorted(os.listdir(pasta_faces))

# Detector de rosto
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Processar cada imagem
for idx, nome_arquivo in enumerate(os.listdir(pasta_imagens)):
    caminho_imagem = os.path.join(pasta_imagens, nome_arquivo)
    imagem = cv2.imread(caminho_imagem)
    if imagem is None:
        print(f"⚠️ Erro ao carregar imagem: {caminho_imagem}")
        continue

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(imagem_cinza, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        rosto = imagem_cinza[y:y + h, x:x + w]
        id, confianca = modelo.predict(rosto)

        texto = f"{nomes[id]} ({round(confianca, 2)})" if confianca < 80 else "Desconhecido"
        cor = (0, 255, 0) if confianca < 80 else (0, 0, 255)

        cv2.rectangle(imagem, (x, y), (x + w, y + h), cor, 2)
        cv2.putText(imagem, texto, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, cor, 2)

    caminho_saida = os.path.join(pasta_resultados, f"resultado_{idx}_{nome_arquivo}")
    cv2.imwrite(caminho_saida, imagem)
    print(f"Imagem salva: {caminho_saida}")
