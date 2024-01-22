import streamlit as st
import re
from src.application.generate_cpf import generate_10th_digit, generate_11th_digit

def validate_cpf():
    st.session_state.cpf_input = re.sub(r'[^0-9]', '', st.session_state.cpf_input)    
    if len(st.session_state.cpf_input) > 11:
        st.session_state.cpf_input_status = 1
       
    elif len(st.session_state.cpf_input) < 11:
        st.session_state.cpf_input_status = 2
    else:
        nine_digits = st.session_state.cpf_input[:9]
        ten_digits = generate_10th_digit(nine_digits)
        complete_cpf = generate_11th_digit(ten_digits)
        is_valid = True if st.session_state.cpf_input == complete_cpf else False
        if is_valid:
           st.session_state.cpf_input_status = 3
            
        else:
            st.session_state.cpf_input_status = 4
        
