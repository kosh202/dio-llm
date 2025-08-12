import os
import base64
import tempfile
from openai import AzureOpenAI
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles

env_path = Path(__file__).resolve(strict=True).parent / ".env"
load_dotenv(dotenv_path = env_path)

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION ")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")


#Configuracao do fastapi

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"], #permitir todos os metodos
    allow_headears=["*"] #permitir todos os cabecalhos
)

#configuracao do cliente openai
client = AzureOpenAI(
    api_key = AZURE_OPENAI_API_KEY,
    azure_endpoint= AZURE_OPENAI_ENDPOINT,
    api_version = AZURE_OPENAI_API_VERSION,
    azure_deployment= AZURE_OPENAI_DEPLOYMENT_NAME
)

def criar_prompt_modelo_ameacas(tipo_aplicacao, autenticacao, acesso_internet, dados_sensiveis, descricao_aplicacao):
    prompt = f"""
Aja como um especialista em cibersegurança com mais de 20 anos de experiência, utilizando a metodologia de modelagem de ameaças STRIDE para produzir modelos abrangentes
para uma ampla gama de aplicações. Sua tarefa é analisar o resumo do código, o conteúdo do README e a descrição da aplicação fornecidos, a fim de produzir uma lista de ameaças específicas para essa aplicação.

Preste atenção especial à descrição da aplicação e aos detalhes técnicos fornecidos.

Para cada categoria do STRIDE:
- Falsificação de identidade (Spoofing)
- Violação de integridade (Tampering)
- Repúdio (Repudiation)
- Divulgação de informações (Information Disclosure)
- Negação de serviço (Denial of Service)
- Elevação de privilégio (Elevation of Privilege)

Liste múltiplas (3 ou 4) ameaças reais, se aplicável.  
Cada cenário de ameaça deve apresentar uma situação plausível em que a ameaça poderia ocorrer no contexto da aplicação.

A lista de ameaças deve ser apresentada em formato JSON com as chaves:
- **"threat_model"**: array de objetos contendo as chaves `"Threat Type"` (Tipo de Ameaça), `"Scenario"` (Cenário) e `"Potential Impact"` (Impacto Potencial).
- **"improvement_suggestions"**: array de strings com sugestões sobre quais informações adicionais poderiam ser fornecidas para tornar o modelo de ameaças mais completo e preciso na próxima iteração.

Nas sugestões, foque em identificar lacunas na descrição da aplicação que, se preenchidas, permitiriam uma análise mais detalhada e precisa, como por exemplo:
- Detalhes arquiteturais ausentes que ajudariam a identificar ameaças mais específicas.
- Fluxos de autenticação pouco claros que precisam de mais detalhes.
- Informações técnicas da stack não informadas.
- Fronteiras ou zonas de confiança do sistema não especificadas.
- Descrição incompleta do tratamento de dados sensíveis.
- Detalhes sobre como os dados são processados ou armazenados.

⚠️ **Não** forneça recomendações de segurança genéricas — foque apenas no que ajudaria a criar um modelo de ameaças mais eficiente.

---

**INFORMAÇÕES FORNECIDAS**
- Tipo de aplicação: {tipo_aplicacao}
- Métodos de autenticação: {autenticacao}
- Exposta na Internet: {acesso_internet}
- Dados sensíveis: {dados_sensiveis}
- Resumo de código, conteúdo do README e descrição da aplicação: {descricao_aplicacao}

---

**EXEMPLO DE FORMATO ESPERADO EM JSON**:
{{
    "threat_model": [
        {{
            "Threat Type": "Spoofing",
            "Scenario": "Cenário de exemplo 1",
            "Potential Impact": "Impacto potencial de exemplo 1"
        }},
        {{
            "Threat Type": "Spoofing",
            "Scenario": "Cenário de exemplo 2",
            "Potential Impact": "Impacto potencial de exemplo 2"
        }}
        // ... mais ameaças
    ],
    "improvement_suggestions": [
        "Forneça mais detalhes sobre o fluxo de autenticação entre os componentes.",
        "Adicione informações sobre como os dados sensíveis são armazenados e transmitidos."
        // ... mais sugestões para melhorar o modelo de ameaças
    ]
}}
"""
    return prompt


@app.post("/analisar_ameacas")
async def analisar_ameacas(
    imagem: UploadFile = File(...),
    tipo_aplicacao: str =Form(...),
    autenticacao: str = Form(...),
    acesso_internet: str = Form(...),
    dados_sensiveis: str = Form(...),
    descricao_aplicacao: str = Form(...)
):
    try:
        #criar o prompt para o modelo de ameacas
        prompt = criar_prompt_modelo_ameacas(tipo_aplicacao,
                                                autenticacao,
                                                acesso_internet,
                                                dados_sensiveis,
                                                descricao_aplicacao)
        # salvar a imagem temporariamente
        with tempfile.NamedTemporaryFile(delete=False, suffix = Path(imagem.filename).suffix) as temp_file:
            content= await imagem.read()
            temp_file.write(await imagem.read())
            temp_file_path = temp_file.name

        #convert imagem para base 64
        with open(temp_file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('ascii')

        #adicionar a aimagem codificada ao prompt
        chat_prompt = [
            {"role": "system", "content":"voce é uma ua especialistaa em cibersegurnaca"},
            {"role": "user", "content":{"type":"text", "text":prompt}},
            {"role": "user", "content":{"type":"image_url", "image_url":f"data:image/png;base64,{encoded_string}"}},
            {"role": "user", "content":{"type":"text", "text":"Por favor, analise a imagem e o texto acima e forneca um modelo de ameacas detalhado"}},
        ]
        
        #chamar o modelo openai
        response = client.chat(
            messages = chat_prompt,
            temperature= 0.7,
            max_tokens = 1500,
            top_p = 0.95
        )
        os.remove(temp_file_path) #remover o arquivo temporrario apos o uso

        #retornar a resposta do modelo
        return JSONResponse(conten=response.to_dict(), status_code = 200)
    
    except Exception as e:
        return JSONResponse(content={"error":str(e)}, status_code=500)