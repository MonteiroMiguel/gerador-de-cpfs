import streamlit as st
from src.application.generate_cpf import generate_cpf
from src.application.validate_cpf import validate_cpf






st.title('Gerador de CPF')
st.button('Gerar CPF', on_click=generate_cpf)

st.session_state.formatting = st.checkbox("Gerar com formatação:", value=True)

if 'cpf' not in st.session_state:
    st.session_state.cpf = ''

if st.session_state.cpf:
    st.subheader('CPF gerado:')
    st.write(st.session_state.cpf)


st.title("Validador de CPF")
cpf_input = st.text_input("Escreva um cpf aqui",placeholder="Ex: 12345678910", key='cpf_input', on_change=validate_cpf)

if 'cpf_input_status' not in st.session_state:
    st.session_state.cpf_input_status = ''

if st.session_state.cpf_input_status:
    match st.session_state.cpf_input_status:
        case 1:
            st.write("Digitos demais")
        case 2:
            st.write("Estão faltando digitos")
        case 3:
            st.write("CPF válido")
        case 4:
            st.write("CPF inválido")