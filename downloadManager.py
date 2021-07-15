# Gestor de descargas
from os.path import isdir 

# Funciones
def err():
    print('Dato erroneo')
    exit()

numLinks = input("Ingresa el numero de links: ")
try: numLinks = int(numLinks)
except: err()

directorio = input("Ingresa la ruta de descarga: ")
if isdir(directorio) == False: err()

nombre = input("Ingresa el nombre del fichero a ejecutar: ")
crearDir = input("¿Crear directorio para almacenar archivos descargados? s (Enter omitir) ")
comandos, count = [], 0

if crearDir == "s":
    nomDirectorio = input("Ingresa el nombre del directorio a crear: ")
    directorioN = f"mkdir '{nomDirectorio}' && cd '{nomDirectorio}'" 
    comandos.append(directorioN)

for i in range(0, int(numLinks), 1):
    link = input (f"Ingresa el link {i+1} de {numLinks}: ")  
    comandos.append(link)

file = open(f"{directorio}/{nombre}.sh", "w")

inicio = "echo -e '\\n' && date +'Inicio: %D %r' && echo -e '\\n'"
print(inicio)
file.write(f'{inicio}\n')

for j in comandos:
    if count == 0 and comandos[count].find('mkdir') == 0:
        print(comandos[count])
        file.write(f'{comandos[count]}\n')
    
    count+=1
    comando = f"echo -e '  Archivo {count} de {len(comandos)}\\n'\nwget --retry-connrefused -nc '{j}'"
    print(comando)
    file.write(f'{comando}\n')

fin = "date +'Finalizado: %D %r'"
print(fin) 
file.write(fin)

file.close()
