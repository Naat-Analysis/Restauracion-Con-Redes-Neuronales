from PIL import Image, ImageFilter
import random

def desenfoques(direccion: str):
    a = random.choice([1,2,3])
    if a == 1:
        imagen = Image.open(direccion)
        imagen_desenfocada = imagen.filter(ImageFilter.GaussianBlur(radius=2))
        return(imagen_desenfocada)
        
    elif a == 2:
        imagen = Image.open(direccion)
        imagen_desenfocada_caja = imagen.filter(ImageFilter.BoxBlur(radius=2))
        return imagen_desenfocada_caja
        
    elif a == 3:
        imagen = Image.open(direccion)
        imagen_desenfocada_medio = imagen.filter(ImageFilter.BLUR)
        return imagen_desenfocada_medio
