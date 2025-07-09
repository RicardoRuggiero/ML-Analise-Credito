# ML-Analise-Credito
# SBank: Análise de Crédito com Machine Learning

## Descrição do Projeto

Este projeto foi desenvolvido como parte da disciplina de Inteligência Artificial e tem como objetivo principal a criação de uma solução automatizada para análise de risco de crédito, voltada para o banco digital fictício SBank.

A aplicação utiliza técnicas de aprendizado de máquina para prever a probabilidade de aprovação de clientes para solicitação de cartão de crédito. O modelo escolhido para essa tarefa foi o Random Forest, devido à sua robustez, capacidade de lidar com dados categóricos e boa performance em classificações binárias.

Com base nos dados cadastrais dos clientes o sistema é capaz de avaliar, de forma preditiva, o risco associado a cada perfil. Essa solução pode ser utilizada para auxiliar a equipe de crédito do banco na tomada de decisões mais rápidas, eficientes e baseadas em dados.

## Como Executar a Aplicação

Para executar a interface interativa, siga os passos abaixo a partir da pasta raiz do projeto.

1.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv .venv
    # Ativar no Windows (PowerShell)
    .\.venv\Scripts\Activate.ps1
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *Nota: Se estiver a usar o Git LFS pela primeira vez, pode ser necessário instalar o cliente do [site oficial](https://git-lfs.github.com/) e executar `git lfs install`.*


3.  **Execute a aplicação Streamlit:**
    ```bash
    streamlit run src/app.py
    ```
A aplicação será aberta automaticamente no seu navegador.

## Estrutura do Projeto

* `/dados`: Contém os datasets originais fornecidos.
* `/notebooks`: Contém o notebook `analise_exploratoria.ipynb` com todo o processo de análise, limpeza de dados e experimentação de modelos.
* `/src`: Contém o código fonte da aplicação (`app.py`) e o modelo de Machine Learning salvo (`modelo_sbank_rf.pkl`).
* `requirements.txt`: Lista de todas as bibliotecas Python necessárias para o projeto.