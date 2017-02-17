import exifread
import os
from datetime import datetime
from shutil import copyfile


def lista_arquivos(path):
    htmlfiles = [os.path.join(root, name)
                for root, dirs, files in os.walk(path)
                for name in files
                if name.endswith((".JPG"))]
    
    return htmlfiles

def get_info(file_path):
    f = open(file_path, 'rb')
    tags = exifread.process_file(f)
    for tag in tags.keys():
        if tag in ('Image DateTime'):
            return file_path, tag, str(tags[tag])

def define_pasta_destino(pasta, info_file):
    data = info_file[2].split(' ')[0]
    destino = data.split(':')[0] + '/' + data.split(':')[1] + '/' + data.split(':')[2] + '/'
    destino = pasta + '/' + destino.replace(' ','')
    return destino


fotos = lista_arquivos("fotos")

for foto in fotos:
    if get_info(foto) is not None:
        nome_arquivo = foto.split('/')[len(foto.split('/')) - 1]
        destino = define_pasta_destino('/vagrant/projeto/exifproj/novas', get_info(foto))
        if not os.path.exists(destino):
            os.makedirs(destino)
        copyfile(foto, destino + nome_arquivo)
        print(foto, destino + nome_arquivo)
        