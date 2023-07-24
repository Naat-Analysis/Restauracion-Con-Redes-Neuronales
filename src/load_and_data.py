from pathlib import Path

def creacion_carpetas(nombres: list, DATA: Path ):
    for nombre in nombres:
        nueva_carpeta = DATA.joinpath(nombre)
        if not nueva_carpeta.exists():
            nueva_carpeta.mkdir()
            print("Carpeta creada exitosamente en:", str(nueva_carpeta))
        else:
            print("La carpeta ya existe en:", str(nueva_carpeta))