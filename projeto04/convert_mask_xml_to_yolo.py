import os
import xml.etree.ElementTree as ET

INPUT_FOLDER = "projeto_yolo/face-mask/annotations"
OUTPUT_FOLDER = "projeto_yolo/converted/labels"
IMAGE_FOLDER = "projeto_yolo/face-mask/images"

TARGET_CLASS = "with_mask"
CLASS_NAME_YOLO = "mascara"
CLASS_ID = 0  # YOLO class id

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for xml_file in os.listdir(INPUT_FOLDER):
    if not xml_file.endswith(".xml"):
        continue

    tree = ET.parse(os.path.join(INPUT_FOLDER, xml_file))
    root = tree.getroot()

    image_name = root.find("filename").text
    image_path = os.path.join(IMAGE_FOLDER, image_name)

    width = int(root.find("size/width").text)
    height = int(root.find("size/height").text)

    yolo_annotations = []

    for obj in root.findall("object"):
        label = obj.find("name").text

        if label != TARGET_CLASS:
            continue  # só pega with_mask

        bbox = obj.find("bndbox")
        xmin = int(bbox.find("xmin").text)
        ymin = int(bbox.find("ymin").text)
        xmax = int(bbox.find("xmax").text)
        ymax = int(bbox.find("ymax").text)

        x_center = (xmin + xmax) / 2.0 / width
        y_center = (ymin + ymax) / 2.0 / height
        bbox_width = (xmax - xmin) / width
        bbox_height = (ymax - ymin) / height

        yolo_annotations.append(f"{CLASS_ID} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}")

    # salvar .txt com mesmo nome da imagem
    if yolo_annotations:
        txt_filename = os.path.splitext(xml_file)[0] + ".txt"
        with open(os.path.join(OUTPUT_FOLDER, txt_filename), "w") as f:
            f.write("\n".join(yolo_annotations))
