import matplotlib.pyplot as plt
import random
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from PIL import Image
from pathlib import Path

def nueve_plot(files: list):
    """Funcion para graficar 9 imagenes dada una lista con muchas imagenes

    Args:
        files (list): Lista con la tura de las imagenes, debe ser una lista de objetos PathFile
    """

    fig, axs = plt.subplots(3,2, figsize=(10,10))
    for ax in axs.flat:
        imagen = load_img(str(random.choice(files)))
        imagen_array = img_to_array(imagen)
        ax.imshow(imagen_array.astype('uint8'))
        ax.set_axis_off()
    plt.show()

def redimensionar(files: list, ancho, alto):
    """Funcion para redimensionar una lista de images.

    Args:
        files (list): Lista con las rutas de las imagenes, del tipo Pathlib
        ancho (int): Numero entero
        alto (int): Numero entero
    """
    for file in files:
        imagen = load_img(str(file))
        imagen_red = imagen.resize((ancho, alto))
        
        nueva_ruta = file.parent.parent.joinpath('Test',file.name)
        imagen_red.save(str(nueva_ruta))
    print('Redimension exitosa')
        

    
def recortar_imagen_horizontal(imagen_path: Path, ancho_corte, save_path: Path):
    """Funcion para dada una imagen, recortarla de forma horizontal generado imagen izq y der

    Args:
        imagen_path (Path): Ruta de la imagen de tipo Pathlib
        ancho_corte (int): ancho donde se hara el corte
        save_path (int): ruta donde guardara la imagen
    """
    # Abrir la imagen
    imagen = Image.open(str(imagen_path))

    # Obtener dimensiones originales
    ancho_original, altura_original = imagen.size

    # Calcular el ancho para recortar la imagen en dos partes iguales
    ancho_corte = min(ancho_original, ancho_corte)

    # Recortar y guardar la parte izquierda de la imagen
    imagen_izquierda = imagen.crop((0, 0, ancho_corte, altura_original))
    imagen_izquierda.save(save_path.joinpath(imagen_path.name[:-5]+"_izq.jpg"))

    # Recortar y guardar la parte derecha de la imagen
    imagen_derecha = imagen.crop((ancho_original - ancho_corte, 0, ancho_original, altura_original))
    imagen_derecha.save(save_path.joinpath(imagen_path.name[:-5]+"_der.jpg"))
    
def recortar_imagen_vertical(imagen_path: Path, alto_corte, save_path: Path):
    """Funcion para dada una imagen, recortarla de forma vertical generando arriba y abajo

    Args:
        imagen_path (Path): Ruta de la imagen de tipo Pathlib
        alto_corte (int): altura donde se hara el corte
        save_path (int): ruta donde guardara la imagen
    """
    # Abrir la imagen
    imagen = Image.open(str(imagen_path))

    # Obtener dimensiones originales
    ancho_original, altura_original = imagen.size

    # Calcular el ancho para recortar la imagen en dos partes iguales
    alto_corte = min(altura_original, alto_corte)

    # Recortar y guardar la parte izquierda de la imagen
    imagen_arriba = imagen.crop((0, 0, ancho_original, alto_corte))
    imagen_arriba.save(save_path.joinpath(imagen_path.name[:-5]+"_arriba.jpg"))

    # Recortar y guardar la parte derecha de la imagen
    imagen_abajo = imagen.crop((0, altura_original - alto_corte, ancho_original, altura_original))
    imagen_abajo.save(save_path.joinpath(imagen_path.name[:-5]+"_abajo.jpg"))
        
    
def rgb_a_escala_de_grises(imagen_path: Path):
    """Convierte una imagen a escala grises y la guarda directamente.

    Args:
        imagen_path (Path): Ruta de la imagen
    """
    # Abrir la imagen en modo RGB
    imagen_rgb = Image.open(str(imagen_path))

    # Convertir a escala de grises
    imagen_gris = imagen_rgb.convert("L")

    # Guardar la imagen en escala de grises
    imagen_gris.save(str(imagen_path))