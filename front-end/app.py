import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Harity", page_icon="📈")

st.title("Produtos da Harity💻")

menu = st.sidebar.radio("Navegação", ["Catálogo", "Adicionar produto", "Atualizar preço", "Deletar produto"])

if menu == "Catálogo":
    st.subheader("Produtos")
    response = requests.get(f"{API_URL}/catalogo")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            for produto in produtos:
                st.write(f"ID: {produto['id']} - {produto['nome']} - {produto['categoria']} - R${produto['preco']} - {produto['quantidade']} unidades")
        else:
            st.info("Nenhum produto encontrado.")

elif menu == "Adicionar produto":
    st.subheader("Adicionar produto ao catálogo")
    nome = st.text_input("Nome do produto")
    categoria = st.text_input("Categoria")
    preco = st.number_input("Preco do produto", min_value=80, max_value=10000, step=1)
    quantidade = st.number_input("Quantidade deste produto", min_value=100, max_value=10000, step=1)

    if st.button("Salvar"):
        
        params = {
            "nome": nome,
            "categoria": categoria,
            "preco": int(preco),
            "quantidade": int(quantidade)
        }
        response = requests.post(f"{API_URL}/produtos", params=params)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso")
        else:
            st.error(f"Erro {response.status_code}: {response.text}")

elif menu == "Atualizar preço":
    st.subheader("Atualizar preço")
    id_produto = st.number_input("ID do produto a atualizar", min_value=1, step=1)
    novo_preco = st.number_input("Novo preço", min_value=0, max_value=10000, step=1)
    
    if st.button("Atualizar"):
        
        params = {"novo_preco": int(novo_preco)}
        response = requests.put(f"{API_URL}/produtos/{int(id_produto)}", params=params)
        
        if response.status_code == 200:
            st.success("🎉 Produto atualizado com sucesso!")
        else:
            st.error(f"Erro {response.status_code}: {response.text}")

elif menu == "Deletar produto":
    st.subheader("Deletar produto")
    id_produto = st.number_input("ID do produto a deletar", min_value=1, step=1)
    
    if st.button("Deletar"):
        response = requests.delete(f"{API_URL}/produtos/{int(id_produto)}")
        
        if response.status_code == 200:
            st.success("Produto deletado com sucesso!")
        else:
            st.error(f"Erro {response.status_code}: {response.text}")