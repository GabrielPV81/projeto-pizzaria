# 📦 Projeto Controle de Estoque

Aplicação web de controle de estoque desenvolvida com arquitetura baseada em containers Docker, separando frontend e backend.

## 🚀 Funcionalidades

- ✅ Cadastro de produtos
- ✅ Listagem de produtos
- ✅ Remoção de produtos
- ✅ Edição de produtos
- ✅ Busca de produtos
- ✅ Alerta de estoque baixo
- ✅ Persistência de dados com SQLite

## 🛠️ Tecnologias utilizadas

- Python (Flask)
- HTML, CSS e JavaScript
- Docker e Docker Compose
- SQLite

## 🧱 Arquitetura

O sistema é dividido em dois containers:

- **Frontend** → Interface com o usuário
- **Backend** → API REST responsável pelo processamento

A comunicação entre eles é feita via requisições HTTP.

## ▶️ Como executar o projeto

docker compose up --build

### 1. Clone o repositório

```bash
git clone https://github.com/GabrielPV81/projeto-final.git