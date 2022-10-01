import hashlib,  os
from datetime import datetime
import time

with open("PAI1/Config.config","r") as configfile:
    directorio=configfile.readline().rstrip()
    sha=configfile.readline().rstrip()
    hora=configfile.readline().rstrip()

directorio_elegido = directorio.replace("directorio=","")
sha_elegido=sha.replace("hash=","")
hora_establecida=hora.replace("hora_comprobacion=","")



def crear_dics_definitivo():
    directorio_listado=os.listdir(directorio_elegido)
    dic_def224={}
    dic_def256={}
    dic_def384={}
    dic_def512={}
    for archivo in directorio_listado:
        with open("PAI1/Carpeta_Para_Hashear/"+archivo,'r') as f:
            contenido=f.readline().rstrip()
        dic_def224[archivo]=hashlib.sha224(contenido.encode('utf-8')).hexdigest()
        dic_def256[archivo]=hashlib.sha256(contenido.encode('utf-8')).hexdigest()
        dic_def384[archivo]=hashlib.sha384(contenido.encode('utf-8')).hexdigest()
        dic_def512[archivo]=hashlib.sha512(contenido.encode('utf-8')).hexdigest()

    return dic_def224,dic_def256,dic_def384,dic_def512

dic224,dic256,dic384,dic512=crear_dics_definitivo()

def crear_dic_temporal():
    dic_temporal={}
    directorio_listado = os.listdir(directorio_elegido)
    for archivo in directorio_listado:
        with open("PAI1/Carpeta_Para_Hashear/"+archivo,'r') as f:
            contenido=f.readline().rstrip()
        if sha_elegido== 'sha224':
            dic_temporal[archivo]=hashlib.sha224(contenido.encode('utf-8')).hexdigest()
        elif sha_elegido== 'sha256':
            dic_temporal[archivo]=hashlib.sha256(contenido.encode('utf-8')).hexdigest()
        elif sha_elegido== 'sha384':
            dic_temporal[archivo]=hashlib.sha384(contenido.encode('utf-8')).hexdigest()
        elif sha_elegido== 'sha512':
            dic_temporal[archivo]=hashlib.sha512(contenido.encode('utf-8')).hexdigest()
        else: 
            print("Hash mal escrito")

    return dic_temporal

def compara_dicc():
    lista_para_log=[]
    for archivo in os.listdir(directorio_elegido):
            if sha_elegido== 'sha224':
                if dic224[archivo] != dic_dinamico[archivo]:
                    lista_para_log.append("El fichero "+ archivo +" ha sido modificado")   
            elif sha_elegido== 'sha256':
                if dic256[archivo] != dic_dinamico[archivo]:
                    lista_para_log.append("El fichero "+ archivo +" ha sido modificado")   
            elif sha_elegido== 'sha384':
                if dic384[archivo] != dic_dinamico[archivo]:
                    lista_para_log.append("El fichero "+ archivo +" ha sido modificado")
            elif sha_elegido== 'sha512':
                if dic512[archivo] != dic_dinamico[archivo]:
                    lista_para_log.append("El fichero "+ archivo +" ha sido modificado")
            else: 
                print("Hash mal escrito")
    return lista_para_log

def main():

    dic_comparado = compara_dicc()
    print(dic_comparado)
    if dic_comparado != []:
        with open("Log.txt","a+") as opfile:
            opfile.write(str(dic_comparado)+'\n')
        
if __name__ == '__main__':
    while True:
        dic_dinamico=crear_dic_temporal()
        if datetime.now().strftime('%X') == hora_establecida:
            main()
            time.sleep(10)