# 🗂️ TaskCloud

**TaskCloud** é uma aplicação web simples de gerenciamento de tarefas, com autenticação de usuários, interface amigável e backend leve feito em Flask. Ideal para aprendizado ou uso pessoal/local.

---

## 🚀 Funcionalidades

- Registro de usuários
- Login e autenticação
- Recuperação de senha (simulada ou com backend SMTP real)
- Listagem e gerenciamento de tarefas (em desenvolvimento)
- Interface web responsiva

---

## 🛠️ Tecnologias Utilizadas

### Frontend:
- HTML5 + CSS3 (sem frameworks)
- JavaScript puro (ES5 compatível)
- Layout responsivo básico

### Backend:
- Python 
- Flask
- SQLite (local)

---

## 📦 Como rodar o projeto

> Requisitos: `Python` e `pip` instalados no sistema (pode ser via Termux no Android)

### 1. Instalação do Python e pip:

```sh
pkg upgrade && update 
pkg install python && python-pip
```
### 2. Clonar repositório:

```sh
git clone https://github.com/Arthurtv/TaskCloud.git
cd TaskCloud
```
### 3. Instalação das dependência:

```sh
cd backend
pip install -r requirements.txt
```

### 4. Se aparecer um erro sobre o bcrypt instale o rust:

```sh
pkg install rust
```
### 5. ligando o server:
```sh
python app.py
```
### Na outra janela no terminal ou termux execute:
```sh
cd ..
```
```sh
cd frontend && python -m http.server 8080
```
### 6. Navegador:

http://localhost:8080


