# YOLOv8 - Detecção de Capacete e Máscara 😷🪖

Este projeto é um exemplo de uso do YOLOv8 para detectar objetos em imagens. As classes detectadas são:

- **capacete**
- **máscara**

## 📁 Estrutura do Dataset

O dataset foi rotulado manualmente e possui a seguinte estrutura:

test01/
├── images/
│ ├── train/
│ └── val/
├── labels/
│ ├── train/
│ └── val/
└── data.yaml

bash
Copiar
Editar

## 🚀 Treinamento

O treinamento foi feito no Google Colab usando a versão leve do modelo YOLOv8 (`yolov8n.pt`) com 10 épocas e imagens 640x640.

Comando usado:

```bash
!yolo task=detect mode=train \
  model=yolov8n.pt \
  data=/content/drive/MyDrive/dio/projeto04/test01/data.yaml \
  epochs=10 imgsz=640 \
  project=/content/drive/MyDrive/dio/projeto04/resultados_yolo \
  name=treinamento_mascara_capacete
🧠 Modelo treinado
O modelo final é salvo automaticamente em:

bash
Copiar
Editar
resultados_yolo/treinamento_mascara_capacete/weights/best.pt
📌 Requisitos
Google Colab com GPU

Python + Ultralytics YOLOv8 (pip install ultralytics)

Dataset rotulado (pode ser feito com LabelMe)

