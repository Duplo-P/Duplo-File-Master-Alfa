import tkinter as tk
from gui import JanelaPrincipal  
# Importa a classe da sua interface gráfica
from funcionalidades import *
# Importa funções de outros arquivos

def main():
    root = tk.Tk()
    janela = JanelaPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()