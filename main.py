from database import criar_tabela
from ui import iniciar_interface

def main():
    # Cria a tabela se ainda não existir
    criar_tabela()
    
    # Inicia a interface gráfica
    iniciar_interface()

if __name__ == "__main__":
    main()
