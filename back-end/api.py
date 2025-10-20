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
    produtos = funcao.listar.products()
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
    funcao.adicionar_filme(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adicionado com sucesso!"}

@app.put("/produtos/{id_produto}")
def atualizar_produto(id_produtos: int, novo_preco: int):
    produtos = funcao.buscar_products(id_produtos)
    if produtos:
        funcao.atualizar_products(id_produtos, novo_preco)
        return {"mensagem": "Preco atualizado com sucesso"}
    else:
        return {"erro": "Produto não encontrado"}
    

@app.delete("/produtos/{id_produtos}")
def deletar_produtos(id_produtos: int):
    produtos = funcao.buscar_products(id_produtos)
    if produtos:
        funcao.deletar_produtos(id_produtos)
        return {"mensagem": "Produto deletado com sucesso!"}
    else:
        return {"erro": "Produto não encontrado!"}
    