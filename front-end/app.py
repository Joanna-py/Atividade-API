import streamlit as st
import requests

API_URl = "http://127.0.0.1:5500/"

st.set_page_config(page_title="Harity", page_icon="🌎")

st.title("Produtos da Harity💻")

menu = st.sidebar.radio("Navegação", ["Catálogo", "Adicionar produto", "Atualizar produto", "Deletar produto"])

   
