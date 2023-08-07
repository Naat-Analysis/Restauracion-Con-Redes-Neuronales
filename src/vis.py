import matplotlib.pyplot as plt
import random
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from PIL import Image
from pathlib import Path

def nueve_plot(files: list):

    fig, axs = plt.subplots(3,2, figsize=(10,10))
    for ax in axs.flat:
        imagen = load_img(str(random.choice(files)))
        imagen_array = img_to_array(imagen)
        ax.imshow(imagen_array.astype('uint8'))
        ax.set_axis_off()
    plt.show()

def redimensionar(files: list, ancho, alto):
    for file in files:
        imagen = load_img(str(file))
        imagen_red = imagen.resize((ancho, alto))
        
        nueva_ruta = file.parent.parent.joinpath('Test',file.name)
        imagen_red.save(str(nueva_ruta))
    print('Redimension exitosa')
        

    
def recortar_imagen(imagen_path: Path, ancho_corte, save_path: Path):
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
    
    
def rgb_a_escala_de_grises(imagen_path: Path):
    # Abrir la imagen en modo RGB
    imagen_rgb = Image.open(str(imagen_path))

    # Convertir a escala de grises
    imagen_gris = imagen_rgb.convert("L")

    # Guardar la imagen en escala de grises
    imagen_gris.save(str(imagen_path))