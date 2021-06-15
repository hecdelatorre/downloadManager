# Gestor de descargas
numLinks = input("Ingresa el numero de links: ")
directorio = input("Ingresa la ruta de descarga: ")
nombre = input("Ingresa el nombre del fichero a ejecutar: ")
crearDir = input("¿Crear directorio para almacenar archivos descargados? s (Enter omitir) ")
links, count = [], 0

if crearDir == "s":
    nomDirectorio = input("Ingresa el nombre del directorio a crear: ")
    directorioN = f"mkdir '{nomDirectorio}' && cd '{nomDirectorio}'" 
    links.append(directorioN)

for i in range(0, int(numLinks), 1):
    link = input (f"Ingresa el link {i+1} de {numLinks}: ")  
    links.append(link)

file = open(f"{directorio}/{nombre}.sh", "w")

inicio = "echo -e '\\n' && date +'Inicio: %D %r' && echo -e '\\n'"
print(inicio)
file.write(f'{inicio}\n')

for j in links:
    if count == 0 and links[count].find('mkdir') == 0:
        print(links[count])
        file.write(f'{links[count]}\n')
    
    count+=1
    comando = f"echo -e '  Archivo {count} de {len(links)}\\n'\nwget --retry-connrefused -nc '{j}'"
    print(comando)
    file.write(f'{comando}\n')

fin = "date +'Finalizado: %D %r'"
print(fin) 
file.write(fin)

file.close()
