import fiftyone as fo
import fiftyone.zoo as foz

# Define as classes que você quer
classes = ["cup", "bottle"]

# Baixa o dataset COCO 2017 (validação) com apenas essas classes
dataset = foz.load_zoo_dataset(
    "coco-2017",
    split="validation",
    label_types=["detections"],
    classes=classes,
    max_samples=100,  # Pode mudar esse número se quiser mais
    dataset_name="coco_val_cup_bottle"
)

# Inicia o app do FiftyOne com o dataset carregado
session = fo.launch_app(dataset)

# Mantém o app aberto até você fechar manualmente
session.wait()
