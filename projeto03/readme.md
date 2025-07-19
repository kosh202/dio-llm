# 📊 Projeto: Cálculo de Métricas de Avaliação de Modelos de Classificação

Este projeto tem como objetivo demonstrar o cálculo das principais métricas utilizadas na avaliação de modelos de **classificação binária**, a partir de uma **matriz de confusão**.

---

## ✅ Objetivos do Projeto

- Simular o treinamento de um modelo de classificação simples com TensorFlow/Keras
- Obter a matriz de confusão a partir das predições
- Calcular manualmente as seguintes métricas de avaliação:
  - Acurácia
  - Precisão
  - Recall (Sensibilidade)
  - F1-Score
  - Especificidade (opcional)

---

## 🧮 Fórmulas Utilizadas

A partir dos valores:

- VP: Verdadeiros Positivos  
- VN: Verdadeiros Negativos  
- FP: Falsos Positivos  
- FN: Falsos Negativos

As fórmulas são:

- **Acurácia**:  
  \[
  \text{Acurácia} = \frac{VP + VN}{VP + VN + FP + FN}
  \]

- **Precisão**:  
  \[
  \text{Precisão} = \frac{VP}{VP + FP}
  \]

- **Recall (Sensibilidade)**:  
  \[
  \text{Recall} = \frac{VP}{VP + FN}
  \]

- **F1-Score**:  
  \[
  F1 = 2 \cdot \frac{\text{Precisão} \cdot \text{Recall}}{\text{Precisão} + \text{Recall}}
  \]

- **Especificidade** (opcional):  
  \[
  \text{Especificidade} = \frac{VN}{VN + FP}
  \]

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Google Colab
- TensorFlow / Keras
- Matplotlib e NumPy
- Scikit-learn (para a matriz de confusão)

---

## 🚀 Como Executar

1. Acesse o notebook no Google Colab (link sugerido no topo do notebook)
2. Execute as células em sequência
3. Após o treinamento, as métricas são calculadas manualmente com base na matriz de confusão

---

## 📌 Observações

- O dataset utilizado foi reduzido para acelerar o processo de treino (apenas para fins didáticos).
- O foco do projeto não está na performance do modelo, e sim na **interpretação das métricas** de avaliação.
- As fórmulas foram implementadas de forma manual para reforçar o entendimento teórico.

---

## 👨‍💻 Autor

Raphael Shodi Kawahara  
Projeto realizado como parte do curso de Ciência da Computação - SENAC  
Desafio: Cálculo de Métricas de Avaliação (DIO / Colab)

---
