# Duplo File Master Alfa 0.1

Duplo File Master Alfa é um programa desenvolvido em Python com uma interface gráfica usando Tkinter. Ele organiza arquivos em pastas com base em suas extensões, facilitando a organização de diretórios com muitos arquivos.

## Funcionalidades

- **Organizar Arquivos**: Move arquivos para pastas específicas com base em suas extensões.
- **Gerar Informações**: Cria um arquivo `info.txt` com informações sobre as redes sociais do Duplo P Analytics.
- **Ajuda**: Exibe uma mensagem de ajuda com informações sobre o programa.
- **Sair**: Fecha o programa.

## Estrutura do Projeto

```
Duplo-File-Master-Alfa/
├── src/
│   ├── main.py
│   ├── gui.py
│   ├── funcionalidades.py
├── README.md
```
## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/Duplo-P/Duplo-File-Master-Alfa.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd Duplo-File-Master-Alfa
    ```

3. Instale as dependências necessárias (se houver).

## Uso

1. Execute o arquivo main.py:
    ```bash
    python src/main.py
    ```

2. A interface gráfica será aberta com as seguintes opções:
    - **Organizar**: Clique neste botão para selecionar um diretório e organizar os arquivos dentro dele.
    - **Ajuda**: Clique neste botão para exibir uma mensagem de ajuda.
    - **Sair**: Clique neste botão para fechar o programa.

## Código Principal

### main.py

Este arquivo contém a definição necessárias para excutar o programa.

```python
import tkinter as tk
from gui import JanelaPrincipal  
# Importa a classe da sua interface gráfica

def main():
    root = tk.Tk()
    janela = JanelaPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```

### gui.py

Este arquivo contém a definição da interface gráfica do programa.

```python
import tkinter as tk
from tkinter import messagebox, filedialog
from funcionalidades import organizar, info_arquivo

class JanelaPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Duplo File Master Alfa 0.1")
        master.resizable(False, False)
        self.master.config(bg = "#201f1f")
        self.centralizar_janela()
        comprimento = 18
        background_btb = "#000000"
        font_color = "#FFFFFF"
        font_size = ("Helvetica", 14)
        font_size_verson = ("Helvetica", 9, "italic")
        
        # Criação dos widgets da interface
        frm = tk.Frame(self.master, bg = "#201f1f")
        
        btb_organizar = tk.Button(frm, width = comprimento, background = background_btb, foreground = font_color, font = font_size, text="Organizar", command = self.organizar)
        btb_organizar.config(cursor = "hand2")
        btb_organizar.pack(pady = 20)

        btb_ajuda = tk.Button(frm, width = comprimento, background = background_btb, foreground = font_color, font = font_size, text="Ajuda", command = self.ajuda)
        btb_ajuda.pack(pady = 20)
        btb_ajuda.config(cursor = "hand2")

        btb_sair = tk.Button(frm, width = comprimento, background = background_btb, foreground = font_color, font = font_size, text="Sair", command = self.sair)
        btb_sair.pack(pady = 20)
        btb_sair.config(cursor = "hand2")

        frm.pack(pady = 80)
        
        lbl_versao = tk.Label(self.master, text = "Duplo P Analytics - Versão 0.1   ", font = font_size_verson, bg = "#201f1f", fg = "#ffffff")
        lbl_versao.pack(side = "bottom", anchor="se")
    
    def info(self):
        try:
            if self.caminho:
                info_arquivo(self.caminho) 
        except Exception as e:
            messagebox.showerror(f"Erro", "Erro ao gerar informações do arquivo {e}")
        
    def organizar(self):
        self.caminho = filedialog.askdirectory(parent=self.master, title="Selecione a pasta para organizar")
        try:
            if self.caminho:
                organizar(self.caminho) 
                messagebox.showinfo("Sucesso", "Arquivos organizados com sucesso!")
        except Exception as e:
            messagebox.showerror(f"Erro", "Erro ao organizar arquivos {e}")
             
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

if __name__ == "__main__":
    root = tk.Tk()
    app = JanelaPrincipal(root)
    root.mainloop()
```

### `funcionalidades.py`

Este arquivo contém as funções que realizam a organização dos arquivos e a geração de informações.

```python
import os
from tkinter import messagebox

def info_arquivo(caminho):
    """
    Função para gerar informações das redes sociais em arquivo txt.
    """
    string = """
    Siga-nos nas redes sociais:
    Instagram: @2p_analytcs
    Facebook: Duplo P Analytics
    """
    os.chdir(caminho)
    try:
        if not os.path.exists("info.txt"):
            with open("info.txt", "w") as arquivo:
                arquivo.write(string)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao criar info.txt: {e}")

def moverArq(arquivo):
    """Essa função verifica a extensão do arquivo e move para a pasta correspondente.

    Args:
        arquivo (str): Variável que armazena o nome do arquivo
    """
    extensao_imagem = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.heic', '.ico', '.jfif', '.pjpeg', '.pjp', '.avif')
    extensao_video = ('.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm', '.mpeg', '.mpg', '.m4v', '.hevc', '.3gp', '.3g2', '.asf', '.avchd', '.m2ts', '.mts', '.mxf', '.ogg', '.rm', '.rmvb', '.ts', '.vob')
    extensao_doc = ('.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp', '.odg', '.odf', '.odc', '.odb', '.odm', '.ott', '.ots', '.otp', '.otg', '.otf', '.otc', '.otb', '.oth', '.docm', '.dot', '.dotx', '.dotm', '.docb', '.xlsb', '.xlsm', '.xltx', '.xltm', '.pptm', '.potx', '.potm', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm')
    extensao_exe = ('.exe', '.bat', '.sh', '.bin', '.cmd', '.com', '.msi', '.jar', '.py', '.pl')
    extensao_audio = ('.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.aiff', '.alac')
    extensao_compactado = ('.zip', '.rar', '.7z', '.tar', '.gz', '.tgz', '.bz2', '.tbz2', '.tar.bz2', '.tar.gz', '.tar.xz', '.tar.zst', '.tar.lz', '.tar.lzma', '.tar.lz4', '.tar.lzo', 'iso')
    extensao_script = ('.sh', '.bash', '.csh', '.ksh', '.zsh', '.cmd', '.ps1', '.psm1', '.psd1', '.ps1xml', '.psc1', '.pssc', '.msh', '.msh1', '.msh2', '.mshxml', '.msh1xml', '.msh2xml')

    arq = {
        "Audios": extensao_audio,
        "Videos": extensao_video,
        "Imagens": extensao_imagem,
        "Documentos": extensao_doc,
        "Compactados": extensao_compactado,
        "Programas": extensao_exe,
        "Script": extensao_script
    }

    try:
        extensao = os.path.splitext(arquivo)[1]
        for chave, valor in arq.items():
            if extensao in valor:
                if not os.path.exists(chave):
                    os.mkdir(chave)
                os.rename(arquivo, chave + '/' + arquivo)
                return
        if not os.path.exists("Outros Arquivos"):
            os.mkdir("Outros Arquivos")
        os.rename(arquivo, "Outros Arquivos/" + arquivo)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao mover arquivo: {e}")

def organizar(caminho):
    """
    Função para organizar os dados do arquivo de entrada.
    """
    try:
        os.chdir(caminho)
        lista_arquivos = os.listdir()
        
        for arquivo in lista_arquivos:
            if os.path.isfile(arquivo):
                moverArq(arquivo)
        
        info_arquivo(caminho)
        messagebox.showinfo("Concluído", "Organização concluída com sucesso")
    except Exception as e:
        messagebox.showwarning("Aviso", f"Erro ao organizar arquivos: {e}")
```

## Contribuição

Se você quiser contribuir para o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
```
Autor: Pedrito Pedro
Por: Duplo P Analytics
