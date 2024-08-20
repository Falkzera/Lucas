import streamlit as st
import re
import requests

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def display_email_form():
    col1, col2 = st.columns(2)
    with col1:
        st.header("Envie-me um Email :email:")
        st.caption("E-mail via FormSubmit. O aplicativo está em desenvolvimento, então pode não funcionar corretamente. Caso não funcione, entre em contato pelas redes na sidebar.")

    # Validação para e-mail
    with st.form(key='contact_form'):
        name = st.text_input("Seu Nome", max_chars=50)
        email = st.text_input("Seu Email", max_chars=50, type='default')
        if email:
            if not is_valid_email(email):
                st.error("Por favor, insira um email válido.")
        message = st.text_area("Sua Mensagem", height=150)
        submit_button = st.form_submit_button(label='Enviar')

    if submit_button:
        if name and email and message:
            # Lógica para enviar o email usando FormSubmit
            form_data = {
                'name': name,
                'email': email,
                'message': message
            }
            response = requests.post(
                'https://formsubmit.co/falcovisk@gmail.com',
                data=form_data
            )
            if response.status_code == 200:
                st.success("Mensagem enviada com sucesso!")
            else:
                st.error("Falha ao enviar a mensagem. Tente novamente mais tarde.")
        else:
            st.error("Por favor, preencha todos os campos.")

if __name__ == "__main__":
    display_email_form()