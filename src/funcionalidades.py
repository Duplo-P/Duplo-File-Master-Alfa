import os
from tkinter import filedialog, messagebox, Tk

def info_arquivo():
    """
    Função para gerar informações das redes socias em arquivo txt.
    
    """
    string ="""
    Siga-nos nas redes sociais:
    Instagram: @2p_analytcs
    Facebook: Duplo P Analytics
    """
    caminho = get_caminho()
    os.chdir(caminho)
    try:
        if not os.path.exists("info.txt"):
            with open("info.txt", "w") as arquivo:
                arquivo.write(string)
    except:
        messagebox.showerror("Erro", "Siga-nos nas redes sociais")
        
  
def get_caminho():
    """
    Função para pegar o caminho da pasta a ser organizada.
    
    """
    root = Tk()
    root.withdraw()

    caminho = filedialog.askdirectory()
    root.destroy()
    
    return caminho

def moverArq(arquivo):
    """Essa função verifica a extensão do arquivo e move para a pasta correspondente.

    Args:
        arquivo : Variavel que armazena o nome do arquivo
        extensao (str): Variavel que armazena a extensão do arquivo
    """
    
    # Criação de Tuplas para armazenar as extensões de arquivos
    extensao_imagem = ('.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG', '.gif', '.GIF', '.bmp', '.BMP', '.tiff', '.TIFF', '.svg', '.SVG', '.webp', '.WEBP','.heic', '.HEIC', '.ico', '.ICO', '.jfif', '.JFIF', '.pjpeg', '.PJPEG', '.pjp', '.PJP', '.avif', '.AVIF')
    extensao_video = ('.mp4','.MOV','.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.mpeg', '.mpg', '.m4v','.MP4','.MOV','.AVI', '.MKV', '.MOV', '.WMV', '.FLV', '.WEBM', '.MPEG', '.MPG', '.M4V', '.hevc', '.HEVC', '.3gp', '.3GP', '.3g2', '.3G2', '.asf', '.ASF', '.avchd', '.AVCHD', '.flv', '.FLV', '.m2ts', '.M2TS', '.mts', '.MTS', '.mxf', '.MXF', '.ogg', '.OGG', '.rm', '.RM', '.rmvb', '.RMVB', '.ts', '.TS', '.vob', '.VOB', '.webm', '.WEBM', '.wmv', '.WMV')
    extensao_doc = ('.pdf','.PDF' ,'.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp','.odg', '.odf', '.odc', '.odb', '.odm', '.ott', '.ots', '.otp', '.otg', '.otf', '.otc', '.otb', '.oth', '.docm', '.dot', '.dotx', '.dotm', '.docb', '.xlsb', '.xlsm', '.xltx', '.xltm', '.xlsx', '.xlsm', '.xlt', '.xlm', '.xlw', '.pptm', '.potx', '.potm', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam')
    extensao_exe = ('.exe', '.bat', '.sh', '.bin', '.cmd', '.com', '.msi', '.jar', '.py', '.pl')
    extensao_audio = ('.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.aiff', '.alac')
    extensao_compactado = ('.zip', '.rar', '.7z', '.tar', '.gz', '.tgz', '.bz2', '.tbz2', '.tar.bz2', '.tar.gz', '.tar.xz', '.tar.zst', '.tar.lz', '.tar.lzma', '.tar.lz4', '.tar.lzo', '.tar.xz', '.tar.zst', '.tar.zstd', '.tar.z','iso')     
    extensao_script = ('.sh', '.bash', '.csh', '.ksh', '.sh', '.zsh', '.cmd', '.ps1', '.psm1', '.psd1', '.ps1xml', '.psc1', '.pssc', '.msh', '.msh1', '.msh2', '.mshxml', '.msh1xml', '.msh2xml')        
    
    # Criação de dicionários para armazenar as extensão
    arq = {"Audios": extensao_audio, "Videos": extensao_video, "Imagens": extensao_imagem, "Documentos": extensao_doc, "Compactados": extensao_compactado, "Programas": extensao_exe, "Script": extensao_script}
    
    try:
        # Verifica a extensão do arquivo e move para a pasta correspondente
        #percorrendo o dicionário
        for chave, valor in arq.items():
            #verificando se a extensão do arquivo está no valor(valor é uma tupla que contém as extensões)
            
            #if extensao in valor:
            if arquivo.endswith(valor):
                #verificando se a pasta existe
                if not os.path.exists(chave):
                    #Se não existir, cria a pasta
                    os.makedirs(chave)
                #Move o arquivo para a pasta correspondente
                os.rename(arquivo, chave + '/' + arquivo)
                break
    except:
        messagebox.showerror("Erro", "Erro ao mover arquivo ")   
             
def moverDoc():
    """Essa função verifica a extensão do arquivo e move para a pasta correspondente,
    neste caso dentro da pasta Documentos, cria subpastas com base nas extensões. 
    """

    NomePasta="Documentos"
    extensao_doc = ('.txt', '.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.wpd', '.wps', '.xml', '.msg', '.odt', '.odp', '.ods', '.odg', '.odf', '.sxw', '.sxi', '.sxc', '.sxd', '.sxi', '.sxm', '.sxg', '.stw', '.stc', '.std', '.stc', '.stw', '.sxw', '.sxd', '.sxi', '.sxm', '.sxg', '.sxc', '.sxd')

    try:
        
        # Indica a pasta como a de trabalho(onde vai criar as subpastas)
        os.chdir(NomePasta)
        
        # Lista de arquivos na pasta
        lista_doc = os.listdir(os.getcwd()) 
        
        # Percorrendo a lista de arquivos
        for arquivo in lista_doc:
            
            # Verifica se o arquivo é um arquivo
            if os.path.isfile(arquivo):
                
                # Separa a extensão do arquivo
                extensao = os.path.splitext(arquivo)[1]
                
                # Verifica a extensão do arquivo e move para a pasta correspondente
                if extensao in extensao_doc:
                    
                    # Verifica se a pasta da extensão existe
                    if not os.path.exists(extensao):
                        
                        # Se não existir, cria a pasta
                        os.makedirs(extensao)
                        
                    # Move o arquivo para a pasta correspondente
                    os.rename(os.getcwd() + "/" + arquivo, os.getcwd() + "/" + extensao + "/" + arquivo)
                
                # Se a extensão não estiver na lista de extensões de documentos
                else:
                    # Cria a pasta Outros, para armazenar os arquivos que as extensões não se encontram.
                    if not os.path.exists("Arquivos Outros"):
                        
                        os.makedirs("Arquivos Outros")
                    os.rename(os.getcwd() + "/" + arquivo, os.getcwd() + "/Arquivos Outros/" + arquivo)
    
    except:
        messagebox.showerror("Erro", "Erro ao mover arquivo")

def organizar():
    """
    Função para organizar os dados do arquivo de entrada.
    
   """
    try:
        # Caminho da pasta a organizar
        caminho = get_caminho()
        
        # Usar o caminho como pasta de trabalho
        os.chdir(caminho)
        
        # Lista de arquivos na pasta
        lista_arquivos = os.listdir()
        
        #Percorendo a lista de arquivos
        for arquivo in lista_arquivos:
            
            # Verifica se o arquivo é um arquivo
            if os.path.isfile(arquivo):
                
                # Verifica a extensão do arquivo e move para a pasta correspondente
                moverArq(arquivo)
        
        # Organiza os documentos
        #moverDoc("Documentos")
        
        # Gera informações das redes sociais em arquivo txt
        info_arquivo()
        
        messagebox.showinfo("Concluído", "Organização concluída com sucesso")
        
    except:
        messagebox.showwarning("Aviso", "Nenhuma pasta selecionada")