from pathlib import Path
import shutil

# Ruta al directorio que contiene los archivos
directorio = Path('.')

# Obtener una lista de los archivos en el directorio
ruta = '22. Actas de Cabildo del H. Ayuntamiento de Centro correspondientes a los años 1998-2000 Libro 7'
carpeta = '22'
archivos = directorio.joinpath('1S.1 - Sesiones de Cabildo',ruta).glob('*')
# Recorrer la lista de archivos



if __name__ == '__main__':
    print('la carpeta que se esta manipulando es')
    print(str(directorio.joinpath('1S.1 - Sesiones de Cabildo',ruta)),)
    print('='*30,'\n')
    
    print('Mover archivos?')
    b = int(input('0: no            1: si\n'))

    if b == 1:
        i = 0
        for archivo in archivos:
            # Crear el nuevo nombre de archivo
            nuevo_nombre = carpeta + '_' + str(i)+'_'+ archivo.name[-8:]

            ruta_nueva = archivo.parent.parent.with_name(nuevo_nombre)
            
            archivo.rename(ruta_nueva)
            i = i+1
            
        print('Archivos copiados con exito')
        
    print('\n','='*30)
    print('Desea eliminar los archivos ')
    a= int(input('0: no            1: si\n'))
    if a==1:
        carpeta_eliminar = directorio.joinpath('1S.1 - Sesiones de Cabildo',ruta)
        shutil.rmtree(carpeta_eliminar)
        print('Archivos y carpeta elimnada con exito')
        
    input('Presione una tecla para salir')