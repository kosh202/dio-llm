import fiftyone as fo
import fiftyone.zoo as foz
import os

# Carrega o dataset que você criou anteriormente
dataset = fo.load_dataset("coco_val_cup_bottle")

# (Opcional) Mostra o esquema de campos para verificar o nome correto
print(dataset.get_field_schema())

# Define o diretório de exportação
export_dir = "export_yolo"

# Exporta no formato YOLOv5
dataset.export(
    export_dir=export_dir,
    dataset_type=fo.types.YOLOv5Dataset,
    label_field="ground_truth",  # campo correto para COCO
)

print(f"Exportado para: {export_dir}")
