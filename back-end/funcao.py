from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id SERIAL PRIMARY KEY,
                    nome TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    preco INTEGER NOT NULL,
                    quantidade REAL       
                    )
                           
                """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir {erro}")
        finally:
            cursor.close()
            conexao.close()

criar_tabela()


def criar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome, categoria, preco, quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir produto {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_products():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos ORDER BY id"

            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao inserir {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()

def atualizar_products(id_produtos, novo_preco):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET preco = %s WHERE id = %s",
                (novo_preco, id_produtos)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar o preco do produto {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_produto(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                    "DELETE FROM produtos WHERE id = %s", (id_produto,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar filme: {erro}")
        finally:
            cursor.close()
            conexao.close()