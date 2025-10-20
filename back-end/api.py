from fastapi import FastAPI
import funcao

app = FastAPI(title="Produtos da Harity")

@app.get("/")
def home():
    return {
        "mensagem":"Bom dia, quero café."
    }

@app.get("/catalogo")
def catalogo():
    produtos = funcao.listar_products()
    lista = []
    for produto in produtos:
        lista.append({
            "id": produto[0],
            "nome": produto[1],
            "categoria": produto[2],
            "preco": produto[3],
            "quantidade": produto[4]
        })
    return {"produtos": lista}

@app.post("/produtos")
def adicionar_produtos(nome: str, categoria: str, preco: int, quantidade: int):
    funcao.criar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adicionado com sucesso!"}

@app.put("/produtos/{id_produto}")
def atualizar_preco(id_produto: int, novo_preco: float):
    produto = funcao.atualizar_products(id_produto, novo_preco)
    if produto:
        funcao.atualizar_preco(id_produto, novo_preco)
        return {"mensagem": "Preço atualizado"}
    return {"erro": "Produto não encontrado"}
    

@app.delete("/produtos/{id_produtos}")
def deletar_produtos(id_produtos: int):
     produtos = funcao.listar_products()
     if produtos:
         funcao.deletar_produto(id_produtos)
         return {"mensagem": "Produto deletado com sucesso!"}
     else:
         return {"erro": "Produto não encontrado!"}
    