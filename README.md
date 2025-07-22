# 📋 Cadastro de Usuários com Interface Gráfica

Este é um sistema simples de cadastro de usuários com interface gráfica usando Python, SQLite3 e Tkinter.

Permite que o usuário insira **nome** e **e-mail**, e armazena essas informações em um banco de dados local (`usuarios.db`). O programa impede o cadastro de e-mails duplicados.

---

## 🛠 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – Interface gráfica
- [SQLite3](https://www.sqlite.org/index.html) – Banco de dados local embutido

---

## 💡 Funcionalidades

- Cadastro de usuários com nome e e-mail
- Validação de campos obrigatórios
- Prevenção de duplicidade de e-mails
- Interface gráfica amigável e simples

---

## 🧩 Estrutura do Projeto
cadastro_app/
├── main.py # Ponto de entrada da aplicação
├── database.py # Criação e manipulação do banco de dados SQLite
├── ui.py # Interface Tkinter com campos e botões
├── utils.py # (Opcional) Funções auxiliares
├── assets/ # Imagens e ícones, se houver
├── .gitignore # Arquivos ignorados pelo Git
└── README.md # Documentação do projeto

---

## 📦 Funcionalidades que podem ser implementadas (ideias para o futuro)
- Validação de e-mail com regex

- Listar todos os usuários cadastrados na interface

- Remoção ou edição de usuários

- Exportação de dados para CSV ou Excel

- Criação de .exe com PyInstaller

- Interface mais moderna com ttkbootstrap

- Tela de login com autenticação

---

## ▶️ Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd cadastro_app
Execute o programa (requer Python 3):

2. **Execute o programa(Requer Python 3):**
   ```bash
   python main.py
---
## Observações finais
- Importante lembrar que, caso haja desejo de consulta ao banco de dados, pode ser realizado o acesso por meio do programa de banco de dados que preferir. Como por exemplo, o DB Browser.

## 🧑‍💻 Autor
Desenvolvido por Rafael Ribeiro


