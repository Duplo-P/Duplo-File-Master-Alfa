import tkinter as tk
from tkinter import messagebox

class JanelaPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Duplo File Master Alfa 0.1")
        master.resizable(False, False)
        self.centralizar_janela()
        comprimento = 18
        background_btb = "#000000"
        font_color = "#FFFFFF"
        font_size = ("Helvetica", 14)
        
        # Criação dos widgets da interface
        frm = tk.Frame(self.master)
        
        btb_organizar = tk.Button(frm, width = comprimento, background = background_btb, foreground = font_color, font = font_size, text="Organizar")
        btb_organizar.pack(pady = 20)
        
        btb_ajuda = tk.Button(frm, width = comprimento, background = background_btb, foreground = font_color, font = font_size, text="Ajuda", command = self.ajuda)
        btb_ajuda.pack(pady = 20)
        
        btb_sair = tk.Button(frm, width = comprimento, background = background_btb, foreground = font_color, font = font_size, text="Sair", command = self.sair)
        btb_sair.pack(pady = 20)
        
        frm.pack(pady = 80)

    def sair(self):
        message = messagebox.askquestion("Sair", "Deseja Sair?")
        if message == "yes":
            self.master.quit()
    def ajuda(self):
        messagebox.showinfo("Ajuda", "Duplo File Master é um programa para organizar arquivos em pastas de acordo com a extensão do arquivo. Para organizar, clique no botão Organizar. Para sair, clique no botão Sair.")
        
    def centralizar_janela(self):
        largura_janela = 600
        altura_janela = 400

        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()

        pos_x = (largura_tela // 2) - (largura_janela // 2)
        pos_y = (altura_tela // 2) - (altura_janela // 2)

        self.master.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")