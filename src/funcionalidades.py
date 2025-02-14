import os
from tkinter import filedialog, messagebox

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
        with open("info.txt", "w") as arquivo:
            arquivo.write(string)
    except:
        messagebox.showerror("Erro", "Siga-nos nas redes sociais")
        
  
def get_caminho():
    """
    Função para pegar o caminho da pasta a ser organizada.
    
    """
    caminho = filedialog.askdirectory()
    
    return caminho

def moverArq(arquivo, extensao):
    """Essa função verifica a extensão do arquivo e move para a pasta correspondente.

    Args:
        arquivo : Variavel que armazena o nome do arquivo
        extensao (str): Variavel que armazena a extensão do arquivo
    """
    
    # Criação de Tuplas para armazenar as extensões de arquivos
    extensao_audio = ('.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.aiff', '.alac', '.amr', '.mid', '.midi', '.mpa', '.ra', '.ram', '.rmi', '.cda', '.m3u', '.pls', '.wpl', '.m4p', '.m4b', '.m4r', '.m4v', '.3gp', '.3g2', '.avi', '.flv', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv', '.asf', '.asx', '.m3u8', '.m3u', '.pls', '.xspf')
    extensao_video = ('.3gp', '.3g2', '.avi', '.flv', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv', '.asf', '.asx', '.m3u8', '.m3u', '.pls', '.xspf')
    extensao_imagem = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.psd', '.pdf', '.eps', '.ai', '.indd', '.raw', '.svg', '.cdr', '.ico', '.webp', '.heif', '.heic', '.bpg', '.jxr', '.wdp', '.hdp', '.jng', '.jif', '.jfif', '.jpe', '.jfi', '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2', '.j2c', '.jpc', '.j2p', '.jps', '.jxl', '.jls','.jxr', '.wdp', '.hdp', '.jng', '.jif', '.jfif', '.jpe', '.jfi', '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2', '.j2c', '.jpc', '.j2p', '.jps', '.jxl', '.jls')
    extensao_doc = ('.txt', '.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.wpd', '.wps', '.xml', '.msg', '.odt', '.odp', '.ods', '.odg', '.odf', '.sxw', '.sxi', '.sxc', '.sxd', '.sxi', '.sxm', '.sxg', '.stw', '.stc', '.std', '.stc', '.stw', '.sxw', '.sxd', '.sxi', '.sxm', '.sxg', '.sxc', '.sxd')
    extensao_compactado = ('.zip', '.rar', '.7z', '.tar', '.gz', '.tgz', '.bz2', '.tbz2', '.tar.bz2', '.tar.gz', '.tar.xz', '.tar.zst', '.tar.lz', '.tar.lzma', '.tar.lz4', '.tar.lzo', '.tar.xz', '.tar.zst', '.tar.zstd', '.tar.z','iso')     
    extensao_executavel = ('.exe', '.msi', '.apk', '.app', '.bat', '.bin', '.cgi', '.com', '.gadget', '.jar', '.wsf', '.appref-ms', '.pif', '.vb', '.ws', '.msc', '.scr', '.reg', '.sh', '.bash', '.csh', '.ksh', '.sh', '.zsh', '.cmd', '.ps1', '.psm1', '.psd1', '.ps1xml', '.psc1', '.pssc', '.msh', '.msh1', '.msh2', '.mshxml', '.msh1xml', '.msh2xml', '.scf', '.lnk', '.inf', '.url', '.cplic', '.cplic')
    extensao_script = ('.sh', '.bash', '.csh', '.ksh', '.sh', '.zsh', '.cmd', '.ps1', '.psm1', '.psd1', '.ps1xml', '.psc1', '.pssc', '.msh', '.msh1', '.msh2', '.mshxml', '.msh1xml', '.msh2xml')        
    
    # Criação de dicionários para armazenar as extensão
    arq = {"Audios": extensao_audio, "Videos": extensao_video, "Imagens": extensao_imagem, "Documentos": extensao_doc, "Compactados": extensao_compactado, "Programas": extensao_executavel, "Script": extensao_script}
    
    try:
        # Verifica a extensão do arquivo e move para a pasta correspondente
        #percorrendo o dicionário
        for chave, valor in arq.items():
            #verificando se a extensão do arquivo está no valor(valor é uma tupla que contém as extensões)
            if extensao in valor:
                #verificando se a pasta existe
                if not os.path.exists(chave):
                    #Se não existir, cria a pasta
                    os.makedirs(chave)
                #Move o arquivo para a pasta correspondente
                os.rename(arquivo, chave + '/' + arquivo)
                break
    except:
        messagebox.showerror("Erro", "Erro ao mover arquivo")   
             
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
                
                # Separa a extensão do arquivo
                extensao = os.path.splitext(arquivo)[1]
                
                # Verifica a extensão do arquivo e move para a pasta correspondente
                moverArq(arquivo, extensao)
        
        # Organiza os documentos
        moverDoc("Documentos")
        
        # Gera informações das redes sociais em arquivo txt
        info_arquivo()
        
        messagebox.showinfo("Concluído", "Organização concluída com sucesso")
        
    except:
        messagebox.showwarning("Aviso", "Nenhuma pasta selecionada")