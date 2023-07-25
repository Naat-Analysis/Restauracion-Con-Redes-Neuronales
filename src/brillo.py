import impresiones
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

tool = impresiones.Impresion()

def colores(direccion: str):
    tool.direccion(direccion)
    
    rojo, azul, verde = 0, 0, 0
    rojo2, azul2, verde2 = 0, 0, 0
    numero_de_veces = 10
    for i in range(numero_de_veces):
        coor2 = tool.coordenas_random()
        imagen = tool.recortar(coor2)
        array_im = np.array(imagen)

        histograma0, bordes_bins0 = np.histogram(array_im[:,:,0].reshape(-1), bins=10)
        histograma1, bordes_bins1 = np.histogram(array_im[:,:,1].reshape(-1), bins=10)
        histograma2, bordes_bins2 = np.histogram(array_im[:,:,2].reshape(-1), bins=10)

        rojo = int(bordes_bins0[np.argmax(histograma0)]) + rojo
        verde = int(bordes_bins1[np.argmax(histograma1)]) + verde
        azul = int(bordes_bins2[np.argmax(histograma2)]) + azul
        
        array_2d = np.sum(array_im, axis=2)

        indices_maximo = np.unravel_index(np.argmin(array_2d), array_2d.shape)
    
        rojo2 = array_im[indices_maximo[0],indices_maximo[1],0] + rojo2 
        verde2 = array_im[indices_maximo[0],indices_maximo[1],1] + verde2
        azul2 = array_im[indices_maximo[0],indices_maximo[1],2] + verde2
    # Crear una matriz con el color deseado
    color_rgb = np.array([[rojo//numero_de_veces, verde//numero_de_veces, azul//numero_de_veces]])
    color_rgb2 = np.array([[rojo2//numero_de_veces, verde2//numero_de_veces, azul2//numero_de_veces]])
    return color_rgb, color_rgb2

def modicacion(direccion: str):
    color_rgb, color_rgb2 = colores(direccion)
    tool.direccion(direccion)
    imagen_array = np.array(tool.imagen)
    for i in range(imagen_array.shape[2]):
        imagen_array[:,:,i] = np.where(imagen_array[:,:,i] < color_rgb2[0,i]+70, color_rgb[0,i]+np.random.randint(-10,10), imagen_array[:,:,i])
    modificado = Image.fromarray(imagen_array)
    return modificado
