# 🍕 Sistema de Pizzaria

Aplicação web para gerenciamento de uma pizzaria, permitindo o controle de ingredientes, cadastro de pizzas e realização de pedidos com validação automática de estoque.

O sistema foi desenvolvido utilizando arquitetura baseada em containers com separação entre frontend e backend.


## 🚀 Funcionalidades

### 🧀 Ingredientes (Estoque)
- ✅ Cadastro de ingredientes
- ✅ Listagem de ingredientes
- ✅ Atualização de quantidade em estoque
- ✅ Controle de estoque em tempo real

### 🍕 Pizzas
- ✅ Cadastro de pizzas
- ✅ Definição dos ingredientes de cada pizza
- ✅ Listagem de pizzas cadastradas

### 🧾 Pedidos
- ✅ Realização de pedidos
- ✅ Seleção de pizzas via dropdown
- ✅ Validação de estoque antes do pedido
- ✅ Baixa automática de ingredientes
- ✅ Bloqueio de pedidos com estoque insuficiente


## 🛠️ Tecnologias Utilizadas

- **Backend:** Python + Flask  
- **Frontend:** HTML, CSS e JavaScript puro  
- **Banco de Dados:** SQLite  
- **Containerização:** Docker e Docker Compose  


## 🧱 Arquitetura
Frontend (HTML/JS) → API REST (Flask) → Banco de Dados (SQLite)

## Como executar o projeto
git clone https://github.com/GabrielPV81/projeto-pizzaria.git
cd projeto-final
docker compose up --build
Frontend: http://localhost:8080
Backend: http://localhost:8001

## 🗄️ Banco de Dados

O sistema utiliza SQLite com duas tabelas principais:

ingredientes

id
nome
quantidade

pizzas

id
nome
ingredientes

## 👨‍💻 Autores
Nome: Gustavo Calin dos Santos — R.A.: 17.01190-6
Nome: Juliana Gomes Haroldo — R.A.: 18.00107-6
Nome: Gabriel Peixoto Varga — R.A.: 18.01470-4
Nome: Vinicius Costa de Sousa — R.A.: 25.80199-4
Nome: Marcio Guolo Malagrino — R.A.: 25.80203-4
