import os

def info_arquivo():
    """
    Função para gerar informações das redes socias em arquivo txt.
    
    """
    string ="""     Duplo File Master Alfa 0.1
Siga-nos nas redes sociais:
    Instagram: @2p_analytcs
    Facebook: Duplo P Analytics
    """

    if not os.path.exists("info.txt"):
        with open("info.txt", "w") as arquivo:
            arquivo.write(string)

        

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
    arq = {
        "Audios": extensao_audio, 
        "Videos": extensao_video, 
        "Imagens": extensao_imagem, 
        "Documentos": extensao_doc, 
        "Compactados": extensao_compactado, 
        "Programas": extensao_exe, 
        "Script": extensao_script
        }
        
        # Verifica a extensão do arquivo e move para a pasta correspondente
        #percorrendo o dicionário
    extensao = os.path.splitext(arquivo)[1]
    for chave, valor in arq.items():
        #verificando se a extensão do arquivo está no valor(valor é uma tupla que contém as extensões)
        
        if extensao in valor:
            #verificando se a pasta existe
            if not os.path.exists(chave):
                #Se não existir, cria a pasta
                os.mkdir(chave)
            #Move o arquivo para a pasta correspondente
            os.rename(arquivo, chave + '/' + arquivo)
            return
    #Se a extensão não estiver na lista de extensões
    if not os.path.exists("Outros Arquivos"):
        os.mkdir("Outros Arquivos")
    os.rename(arquivo, "Outros Arquivos/" + arquivo)
    
def moverDoc():
    """Essa função verifica a extensão do arquivo e move para a pasta correspondente,
    neste caso dentro da pasta Documentos, cria subpastas com base nas extensões. 
    """

    NomePasta="Documentos"
    extensao_doc = ('.txt', '.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.wpd', '.wps', '.xml', '.msg', '.odt', '.odp', '.ods', '.odg', '.odf', '.sxw', '.sxi', '.sxc', '.sxd', '.sxi', '.sxm', '.sxg', '.stw', '.stc', '.std', '.stc', '.stw', '.sxw', '.sxd', '.sxi', '.sxm', '.sxg', '.sxc', '.sxd', '.pptx', '.ppt', '.pptm', '.potx', '.pot', '.potm', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pot', '.pps', '.ppa')
    
    # Indica a pasta como a de trabalho(onde vai criar as subpastas)
    os.chdir(NomePasta)
    
    # Lista de arquivos na pasta
    lista_doc = os.listdir(os.getcwd()) 
    
    # Percorrendo a lista de arquivos
    for arquivo in lista_doc:
         # Separa a extensão do arquivo
        extensao = os.path.splitext(arquivo)[1]
        
        for ext in extensao_doc:
            if ext == extensao:
                if not os.path.exists(ext):
                    os.mkdir(ext)
                os.rename(arquivo, ext + '/' + arquivo)
                break
        else:
            if not os.path.exists("Outros Documentos"):
                os.mkdir("Outros Documentos")
            os.rename(arquivo, "Outros Documentos/" + arquivo)

def organizar(caminho):
    """
    Função para organizar os dados do arquivo de entrada.
    
   """
        
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
    
    # Gera informações das redes sociais em arquivo txt
    info_arquivo()
    
    # Organiza os documentos
    moverDoc()
    