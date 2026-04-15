#!/usr/bin/python
from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# 🔌 conexão com banco
def conectar():
    return sqlite3.connect("/tmp/pizzaria.db")

# 🧱 criar tabelas
def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        quantidade INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pizzas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        ingredientes TEXT
    )
    """)

    conn.commit()
    conn.close()

criar_tabelas()

# =========================
# INGREDIENTES
# =========================

@app.route('/ingredientes', methods=['GET'])
def listar_ingredientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingredientes")
    dados = cursor.fetchall()
    conn.close()

    lista = []
    for d in dados:
        lista.append({"id": d[0], "nome": d[1], "quantidade": d[2]})
    return jsonify(lista)


@app.route('/ingredientes', methods=['POST'])
def adicionar_ingrediente():
    data = request.json
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ingredientes (nome, quantidade) VALUES (?, ?)",
        (data["nome"], data["quantidade"])
    )
    conn.commit()
    conn.close()
    return jsonify({"msg": "Ingrediente adicionado"})

@app.route('/ingredientes/<int:id>', methods=['PUT'])
def atualizar_ingrediente(id):
    data = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE ingredientes
        SET quantidade = ?
        WHERE id = ?
    """, (data["quantidade"], id))

    conn.commit()
    conn.close()

    return jsonify({"msg": "Ingrediente atualizado"})


# =========================
# PIZZAS
# =========================

@app.route('/pizzas', methods=['GET'])
def listar_pizzas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pizzas")
    dados = cursor.fetchall()
    conn.close()

    lista = []
    for d in dados:
        lista.append({"id": d[0], "nome": d[1], "ingredientes": d[2]})
    return jsonify(lista)


@app.route('/pizzas', methods=['POST'])
def adicionar_pizza():
    data = request.json
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO pizzas (nome, ingredientes) VALUES (?, ?)",
        (data["nome"], data["ingredientes"])
    )
    conn.commit()
    conn.close()
    return jsonify({"msg": "Pizza cadastrada"})


# =========================
# PEDIDOS
# =========================

@app.route('/pedidos', methods=['POST'])
def fazer_pedido():
    data = request.json
    nome_pizza = data["pizza"]

    conn = conectar()
    cursor = conn.cursor()

    # pegar ingredientes da pizza
    cursor.execute("SELECT ingredientes FROM pizzas WHERE nome=?", (nome_pizza,))
    resultado = cursor.fetchone()

    if not resultado:
        conn.close()
        return jsonify({"msg": "Pizza não encontrada"}), 404

    ingredientes = resultado[0].split(",")

    # 🔍 1. VERIFICAR ESTOQUE
    for ing in ingredientes:
        nome_ing = ing.strip()

        cursor.execute(
            "SELECT quantidade FROM ingredientes WHERE nome=?",
            (nome_ing,)
        )
        result = cursor.fetchone()

        # ingrediente não existe ou quantidade insuficiente
        if not result or result[0] < 1:
            conn.close()
            return jsonify({
                "erro": f"Estoque insuficiente para {nome_ing}"
            }), 400

    # 🔻 2. BAIXAR ESTOQUE (SÓ SE TUDO OK)
    for ing in ingredientes:
        nome_ing = ing.strip()

        cursor.execute(
            "UPDATE ingredientes SET quantidade = quantidade - 1 WHERE nome=?",
            (nome_ing,)
        )

    conn.commit()
    conn.close()

    return jsonify({"msg": f"Pedido de {nome_pizza} realizado!"})


# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
