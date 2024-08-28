# PROJETO CREWAI + OLLAMA LOCAL
# by geanclm on 28/8/2024

# Passo 1: importante verificar esse procedimento - para esse caso apresentou problema na instalação do crewai
    # criar ambiente virtual
    # python -m venv ollama  
    #  .\ollama\Scripts\activate  
    # deactivate    

# Passo 2:
    # instalações necessárias
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
from langchain_ollama import ChatOllama
from crewai import Crew, Process, Agent, Task

# executar o modelo no prompt local
# ollama run llama3.1

os.environ["OPENAI_API_KEY"] = "NA"

ollama = ChatOllama(
    model = "llama3.1:8b",
    base_url = "http://localhost:11434"
)

redator_revisor = Agent(
    role='Redator e Revisor',
    goal='Redigir uma dissertação argumentativa de alto nível em português do Brasil sobre {topic}, garantindo clareza, coesão e persuasão.',
    verbose=True,
    memory=True,
    backstory=("Você é um redator versátil e meticuloso, com profunda habilidade em criar conteúdos envolventes e garantir sua precisão."),
    llm=ollama,
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
    process=Process.sequential,        
)

result = crew.kickoff(inputs={'topic': 'Tipos de Aprendiado de Máquina'})
print(result)