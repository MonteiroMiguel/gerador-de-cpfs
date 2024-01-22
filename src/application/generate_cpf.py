import streamlit as st
import random

def generate_nine_digits() -> str:
    nove_numeros = ''
    for numero in range(9):        
        numero = str(random.randint(0, 9))
        nove_numeros += numero
    return nove_numeros

def generate_10th_digit(nine_digits: str) -> str:
    multiplier = 10
    total = 0
    for digit in nine_digits:
        total += int(digit) * multiplier
        multiplier -= 1
    tenth_digit = (total * 10) % 11
    tenth_digit = tenth_digit if tenth_digit <= 9 else 0
    return nine_digits + str(tenth_digit)
def generate_11th_digit(ten_digits: str) -> str:
    multiplier = 11
    total = 0
    for digit in ten_digits:
        total += int(digit) * multiplier
        multiplier -= 1
    eleventh_digit = (total * 10) %11
    eleventh_digit = eleventh_digit if eleventh_digit <= 9 else 0
    return ten_digits + str(eleventh_digit)

def generate_cpf() -> str:
    nine_digits = generate_nine_digits()
    ten_digits = generate_10th_digit(nine_digits)
    complete_cpf = generate_11th_digit(ten_digits)
    if complete_cpf == complete_cpf[0] * len(complete_cpf):
        generate_cpf()
    if st.session_state.formatting:
        st.session_state.cpf = f'{complete_cpf[:3]}.{complete_cpf[3:6]}.{complete_cpf[6:9]}-{complete_cpf[9:]}'
    else:
        st.session_state.cpf = complete_cpf