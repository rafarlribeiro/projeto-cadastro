import tkinter as tk
from tkinter import messagebox
from database import inserir_usuario

def cadastrar():
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()

    if not nome or not email:
        messagebox.showwarning("Campos obrigatórios", "Por favor, preencha todos os campos.")
        return

    sucesso = inserir_usuario(nome, email)

    if sucesso:
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "E-mail já cadastrado.")

def iniciar_interface():
    global entry_nome, entry_email

    janela = tk.Tk()
    janela.title("Cadastro de Usuário")
    janela.geometry("300x200")
    janela.resizable(False, False)

    # Labels e entradas
    tk.Label(janela, text="Nome:").pack(pady=(10, 0))
    entry_nome = tk.Entry(janela, width=30)
    entry_nome.pack()

    tk.Label(janela, text="E-mail:").pack(pady=(10, 0))
    entry_email = tk.Entry(janela, width=30)
    entry_email.pack()

    # Botão de cadastro
    tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=20)

    janela.mainloop()
