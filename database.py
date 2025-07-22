import sqlite3

# Caminho do banco de dados
DB_NAME = "usuarios.db"

def conectar():
    """Conecta ao banco de dados (ou cria se não existir)."""
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    """Cria a tabela de usuários se ela ainda não existir."""
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()

def inserir_usuario(nome, email):
    """Insere um novo usuário no banco de dados."""
    try:
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome, email))
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False  # e-mail já cadastrado

def listar_usuarios():
    """Retorna todos os usuários cadastrados."""
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, email FROM usuarios')
        return cursor.fetchall()
