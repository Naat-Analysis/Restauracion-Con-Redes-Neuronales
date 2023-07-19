import matplotlib.pyplot as plt
import random
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from PIL import Image
 

def nueve_plot(files: list):

    fig, axs = plt.subplots(3,2, figsize=(10,10))
    for ax in axs.flat:
        imagen = load_img(str(random.choice(files)))
        imagen_array = img_to_array(imagen)
        ax.imshow(imagen_array.astype('uint8'))
        ax.set_axis_off()
    plt.show()

def redimensionar(ruta, alto, ancho)