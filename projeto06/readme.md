# 🔍 Busca de Imagens por Similaridade

Este projeto implementa um sistema simples de **busca de imagens por similaridade visual** usando **deep learning** com **ResNet50** pré-treinada no ImageNet.  
Dada uma imagem de consulta, o sistema retorna as imagens mais semelhantes do conjunto de dados.

---

## 📌 Funcionalidades

- Carregamento e organização de dataset de imagens  
- Padronização e pré-processamento das imagens  
- Extração de **embeddings** com **ResNet50** (Keras / TensorFlow)  
- Cálculo de similaridade usando **cosseno**  
- Exibição visual das imagens mais parecidas  

---

## 📂 Estrutura do Projeto

projeto06/ └── test01/ ├── baixarDados.py # Baixa o dataset ├── visualizar_padronizar.py # Padroniza e visualiza imagens ├── vetor_caminho.py # Extrai embeddings e salva vetores/caminhos ├── buscar_similaridade.py # Busca imagens mais parecidas ├── dataset/ # Dataset organizado │ └── flower_photos/ ├── vetores.npy # Vetores extraídos └── caminhos.npy # Caminhos das imagens correspondentes


---

## ⚙️ Instalação

### 1️⃣ Clone este repositório

```bash
git clone https://github.com/seu-usuario/projeto06.git
cd projeto06/test01
2️⃣ Crie um ambiente virtual e instale dependências
bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```
3️⃣ (Opcional) Baixe o dataset automaticamente
bash
python baixarDados.py
Caso prefira, você pode colocar manualmente o dataset em dataset/flower_photos.

🚀 Uso
1️⃣ Padronizar e visualizar imagens
bash
python visualizar_padronizar.py
2️⃣ Extrair vetores e salvar
bash
python vetor_caminho.py
3️⃣ Buscar imagens similares
bash
python buscar_similaridade.py
Altere no código de buscar_similaridade.py a variável imagem_teste para a imagem que deseja usar como consulta.

📊 Exemplo de Execução
bash
Embeddings carregados: (3670, 2048)
Total de imagens: 3670
Categorias encontradas: ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

Imagens mais parecidas com: dataset/flower_photos/daisy/100080576_f52e8ee070_n.jpg
💡 O sistema exibirá a imagem de consulta seguida das mais similares.

🛠 Tecnologias Utilizadas
```
Python 3.12+

TensorFlow / Keras

NumPy

Matplotlib

scikit-learn