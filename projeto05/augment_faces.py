import os
import cv2
import random
from PIL import Image, ImageEnhance
import numpy as np

def augment_image(img):
    augmentations = []

    # Inversão horizontal
    augmentations.append(cv2.flip(img, 1))

    # Rotação aleatória
    angle = random.randint(-15, 15)
    h, w = img.shape[:2]
    matrix = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
    augmentations.append(cv2.warpAffine(img, matrix, (w, h)))

    # Aumento de brilho
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    bright = ImageEnhance.Brightness(pil_img).enhance(random.uniform(1.2, 1.5))
    augmentations.append(cv2.cvtColor(np.array(bright), cv2.COLOR_RGB2BGR))

    # Redução de brilho
    dark = ImageEnhance.Brightness(pil_img).enhance(random.uniform(0.6, 0.9))
    augmentations.append(cv2.cvtColor(np.array(dark), cv2.COLOR_RGB2BGR))

    return augmentations

def augment_directory(input_dir, output_dir, target_count=30):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    images = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    total = len(images)
    count = 0

    print(f"Iniciando aumento de dados para: {input_dir}")

    for img_name in images:
        img_path = os.path.join(input_dir, img_name)
        img = cv2.imread(img_path)
        out_path = os.path.join(output_dir, f"orig_{img_name}")
        cv2.imwrite(out_path, img)
        count += 1

    i = 0
    while count < target_count:
        img_name = images[i % len(images)]
        img_path = os.path.join(input_dir, img_name)
        img = cv2.imread(img_path)

        aug_imgs = augment_image(img)
        for aug in aug_imgs:
            if count >= target_count:
                break
            aug_name = f"aug_{count}.jpg"
            aug_path = os.path.join(output_dir, aug_name)
            cv2.imwrite(aug_path, aug)
            count += 1
        i += 1

    print(f"Total de imagens salvas em {output_dir}: {count}")

# Exemplo de uso:
base_dir = "dataset"
aug_dir = "dataset_aug"
target_imgs_per_person = 30

# Para cada pessoa/pasta
for person in os.listdir(base_dir):
    input_path = os.path.join(base_dir, person)
    output_path = os.path.join(aug_dir, person)
    if os.path.isdir(input_path):
        augment_directory(input_path, output_path, target_imgs_per_person)
