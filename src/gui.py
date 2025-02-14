import tkinter as tk


class JanelaPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Duplo File Master Alfa 0.1")
        master.geometry("800x600")
        master.resizable(False, False)
        self.centralizar_janela()

        # Criação dos widgets da interface
        label = tk.Label(master, text="Exemplo de label")
        label.pack()

        botao = tk.Button(master, text="Calcular")
        botao.pack()
        self.centralizar_janela()


    def centralizar_janela(self):
        largura_janela = 800
        altura_janela = 600

        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()

        pos_x = (largura_tela // 2) - (largura_janela // 2)
        pos_y = (altura_tela // 2) - (altura_janela // 2)

        self.master.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")