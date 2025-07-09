# ML-Analise-Credito
# SBank: An�lise de Cr�dito com Machine Learning

## Descri��o do Projeto

Este projeto foi desenvolvido como parte da disciplina de Intelig�ncia Artificial e tem como objetivo principal a cria��o de uma solu��o automatizada para an�lise de risco de cr�dito, voltada para o banco digital fict�cio SBank.

A aplica��o utiliza t�cnicas de aprendizado de m�quina para prever a probabilidade de aprova��o de clientes para solicita��o de cart�o de cr�dito. O modelo escolhido para essa tarefa foi o Random Forest, devido � sua robustez, capacidade de lidar com dados categ�ricos e boa performance em classifica��es bin�rias.

Com base nos dados cadastrais dos clientes o sistema � capaz de avaliar, de forma preditiva, o risco associado a cada perfil. Essa solu��o pode ser utilizada para auxiliar a equipe de cr�dito do banco na tomada de decis�es mais r�pidas, eficientes e baseadas em dados.

## Como Executar a Aplica��o

Para executar a interface interativa, siga os passos abaixo a partir da pasta raiz do projeto.

1.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv .venv
    # Ativar no Windows (PowerShell)
    .\.venv\Scripts\Activate.ps1
    ```

2.  **Instale as depend�ncias:**
    ```bash
    pip install -r requirements.txt
    ```
    *Nota: Se estiver a usar o Git LFS pela primeira vez, pode ser necess�rio instalar o cliente do [site oficial](https://git-lfs.github.com/) e executar `git lfs install`.*


3.  **Execute a aplica��o Streamlit:**
    ```bash
    streamlit run src/app.py
    ```
A aplica��o ser� aberta automaticamente no seu navegador.

## Estrutura do Projeto

* `/dados`: Cont�m os datasets originais fornecidos.
* `/notebooks`: Cont�m o notebook `analise_exploratoria.ipynb` com todo o processo de an�lise, limpeza de dados e experimenta��o de modelos.
* `/src`: Cont�m o c�digo fonte da aplica��o (`app.py`) e o modelo de Machine Learning salvo (`modelo_sbank_rf.pkl`).
* `requirements.txt`: Lista de todas as bibliotecas Python necess�rias para o projeto.