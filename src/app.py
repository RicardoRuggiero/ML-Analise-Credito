import streamlit as st
import pandas as pd
import joblib

# --- Carregamento do Modelo ---
# Carregamos o modelo treinado uma única vez e o guardamos em cache para performance
@st.cache_resource # Isso evita que o modelo seja recarregado a cada interação do usuário
def load_model():
    model = joblib.load('src/modelo_sbank_rf.pkl')
    return model

modelo = load_model()

# --- Definição das Colunas Esperadas pelo Modelo ---
# É CRUCIAL que os dados de entrada tenham as mesmas colunas do X_train
# (baseado no nosso notebook)
colunas_modelo = [
    'idade', 'renda_mensal', 'score_credito', 'tem_conta_corrente',
    'estado_AL', 'estado_AM', 'estado_AP', 'estado_BA', 'estado_CE',
    'estado_DF', 'estado_ES', 'estado_GO', 'estado_MA', 'estado_MG',
    'estado_MS', 'estado_MT', 'estado_PA', 'estado_PB', 'estado_PE',
    'estado_PI', 'estado_PR', 'estado_RJ', 'estado_RN', 'estado_RO',
    'estado_RR', 'estado_RS', 'estado_SC', 'estado_SE', 'estado_SP',
    'estado_TO'
]

# --- Interface do Usuário (Streamlit) ---

st.title("SBank - Análise de Crédito com ML(IA)")
st.write("Esta aplicação utiliza um modelo de Machine Learning(ML) para prever a probabilidade de aprovação de um cartão de crédito.")
st.sidebar.header("Insira os Dados do Cliente")

# Lista de estados para o selectbox
estados_brasil = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT',
    'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

# Função para coletar os dados de entrada
def user_input_features():
    idade = st.sidebar.number_input('Idade', 18, 100, 30)
    renda_mensal = st.sidebar.number_input('Renda Mensal (R$)', 0, 100000, 5000)
    score_credito = st.sidebar.slider('Score de Crédito', 300, 850, 650)
    estado_selecionado = st.sidebar.selectbox('Estado', estados_brasil)
    tem_conta_corrente_check = st.sidebar.checkbox('Cliente já possui conta corrente?', value=True)
    
    # Dicionário com os dados
    data = {
        'idade': idade,
        'renda_mensal': renda_mensal,
        'score_credito': score_credito,
        'estado': estado_selecionado, # Essa variável de string será transformada pelo pd.get_dummies()
        'tem_conta_corrente': tem_conta_corrente_check
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('Dados Inseridos')
st.write(input_df)

# Botão para fazer a previsão
if st.button('Realizar Análise de Crédito'):
    # --- PREPARAÇÃO DOS DADOS DE ENTRADA ---
    # 1. Aplica o 'One-Hot Encoding' no estado inserido (string)
    input_encoded = pd.get_dummies(input_df, columns=['estado'])
    
    # 2. Reorganiza as colunas para bater com o modelo treinado
    # O .reindex garante que todas as colunas do 'colunas_modelo' existam
    # e na ordem correta, preenchendo com 0 as que não foram inseridas.
    input_final = input_encoded.reindex(columns=colunas_modelo, fill_value=0)

    # --- REALIZAR A PREVISÃO ---
    prediction_proba = modelo.predict_proba(input_final)
    prediction = modelo.predict(input_final)

    st.subheader('Resultado da Análise')

    # Acessa a probabilidade da classe 'True' (índice 1)
    prob_aprovacao = prediction_proba[0][1] 

    if prediction[0] == True:
        st.success('**APROVADO**')
        st.write(f"Probabilidade de aprovação: **{prob_aprovacao:.2%}**")
    else:
        st.error('**REPROVADO**')
        st.write(f"Probabilidade de aprovação: **{prob_aprovacao:.2%}**")

else:
    st.write("Por favor, clique no botão para realizar a análise.")