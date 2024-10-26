# PROJETO CREWAI + OLLAMA LOCAL
# by geanclm on 28/8/2024

# - - -
# Passo 1: importante verificar esse procedimento - para esse caso apresentou problema na instalação do crewai
# UMA BOA PRÁTICA PARA ORGANIZAR O PROJETO
    # criar ambiente virtual
    # python -m venv ollama  
    #  .\ollama\Scripts\activate  
    # deactivate    
# - - -

# Passo 2:
    # instalações necessárias
        # pip instaal OpenAI
        # pip install langchain-ollama
        # pip install --q crewai
        # pip install --q 'crewai[tools]'

# Passo 3:
# gerar arquivo requirements.txt com dependências do projeto
    # pip freeze > requirements.txt
# caso necessário retomar o projeto com as mesmas dependências    
    # pip install -r requirements.txt


# Passo 4:
# importar as bibliotecas
import os
from openai import OpenAI
from langchain_ollama import ChatOllama
from crewai import Crew, Process, Agent, Task

# crewai - - - TESTE 1 PARA RODAR CREWAI COM OLLAMA LOCAL
# executar o modelo no prompt local do windows
# ollama run llama3.1:8b

os.environ["OPENAI_API_KEY"] = "NA"

brain = ChatOllama(
    model = "llama3.1",
    base_url = "http://localhost:11434")


redator_revisor = Agent(
    role='Redator e Revisor',
    goal='Redigir uma dissertação argumentativa de alto nível em português do Brasil sobre {topic}, garantindo clareza, coesão e persuasão.',
    verbose=True,
    memory=True,
    backstory=("Você é um redator versátil e meticuloso, com profunda habilidade em criar conteúdos envolventes e garantir sua precisão."),
    llm=brain,
    allow_delegation=False,    
)

redigir_revisar_task = Task(
    description="Elaborar uma dissertação em português do Brasil com 30 linhas sobre {topic}.",
    expected_output="Uma dissertação argumentativa de 30 linhas, sobre {topic}, coesa, coerente e gramaticalmente correta.",
    agent=redator_revisor,
    async_execution=False,
    allow_delegation=False,
)

crew = Crew(
    agents=[redator_revisor],
    tasks=[redigir_revisar_task],
    verbose=True      
)

result = crew.kickoff(inputs={'topic': 'Tipos de Aprendiado de Máquina'})
print(result)



# # - - -
# # TESTE 2 PARA RODAR crewai COM OLLAMA LOCAL
# # TAMBÉM NÃO RODOU --- DEVE SER A INSTALAÇÃO DO PYTHON!!!
# # by geanclm on 29/8/2024
# client = OpenAI(api_key="nada", base_url = "http://localhost:11434/v1")
# response = client.chat.completions.create(
#     model = "llama3.1:8b",
#     messages=[
#         {'role': 'user', 'content': "Qual a capital do Brasil?"}
#     ],
#     stream=False
# )
# print(response.choices[0].message.content)