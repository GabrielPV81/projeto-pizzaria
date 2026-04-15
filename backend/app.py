from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def conectar():
    return sqlite3.connect("estoque.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            quantidade INTEGER
        )
    """)
    conn.commit()
    conn.close()

criar_tabela()

@app.route('/')
def root():
    return "API rodando com banco!"

@app.route('/produtos', methods=['GET'])
def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos ORDER BY nome")
    dados = cursor.fetchall()
    conn.close()

    produtos = [
        {"id": d[0], "nome": d[1], "quantidade": d[2]}
        for d in dados
    ]
    return jsonify(produtos)

@app.route('/produtos', methods=['POST'])
def adicionar():
    data = request.json
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, quantidade) VALUES (?, ?)",
        (data["nome"], data["quantidade"])
    )
    conn.commit()
    conn.close()
    return jsonify({"msg": "Produto adicionado"})

@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"msg": "Removido"})

@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar(id):
    data = request.json
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE produtos SET nome=?, quantidade=? WHERE id=?",
        (data["nome"], data["quantidade"], id)
    )
    conn.commit()
    conn.close()
    return jsonify({"msg": "Atualizado"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
