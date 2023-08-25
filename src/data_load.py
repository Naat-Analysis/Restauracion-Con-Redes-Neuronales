import numpy as np
import tensorflow as tf
from keras.utils import Sequence
from keras.preprocessing.image import ImageDataGenerator

class CustomImageDataGenerator(Sequence):
    """Creamos una clase la cuales es un generador de imagenes con las caracteristicas especiales para este proyecto
    """
    def __init__(self, image_paths_noisy, image_paths_clean , batch_size, target_size, class_mode='input',shuffle=True, datagen_args=None):
        """Funcion iniciadora de la clase, incluye los valores con los que inicializa
        
        En esta funcion cargamos las imagenes con imperfecciones y en buene estado, las procesamos bajo el mismo ImageDataGenerador
        y regreamos las imagenes de tal forma que "x" es la imagen con imperfeccion procesada con el ImageDataGenerator y
        "y"  es la imagen en buen estado procesada bajo el mismo ImageDataGenerator

        Args:
            image_paths_noisy (list): lista con las rutas de las imagenes con imperfecciones
            image_paths_clean (list): lista con las rutas de las imagenes en buen estado
            batch_size (int): batch_sie
            target_size ((int, int)): tuple con el tamaño de las imagnes
            class_mode (str, optional): Defaults to 'input'.
            shuffle (bool, optional): Activar o no modo aleatorio.
            datagen_args (_type_, optional): Funcion ImageDataGenerador, se describe como sera
        """
        self.image_paths_noisy = image_paths_noisy
        self.image_paths_clean = image_paths_clean
        self.batch_size = batch_size
        self.target_size = target_size
        self.class_mode = class_mode
        self.shuffle = shuffle
        self.on_epoch_end()
        
        
        self.datagen_args = datagen_args if datagen_args else {}
        self.datagen = ImageDataGenerator(**self.datagen_args)
        #self.image_x_datagen = ImageDataGenerator(**self.datagen_args)
        #self.image_y_datagen = ImageDataGenerator(**self.datagen_args)

    def __len__(self):
        if len(self.image_paths_clean)==len(self.image_paths_noisy):
            return int(np.ceil(len(self.image_paths_clean) / float(self.batch_size)))

    def __getitem__(self, idx):
        indexes = self.indexes[idx * self.batch_size: (idx + 1) * self.batch_size]

        batch_files_clean = self.image_paths_clean[idx * self.batch_size: (idx + 1) * self.batch_size]
        batch_files_noisy = self.image_paths_noisy[idx * self.batch_size: (idx + 1) * self.batch_size]
        
        y = [self.load_and_preprocess_image(str(file)) for file in batch_files_clean]
        x = [self.load_and_preprocess_image(str(file)) for file in batch_files_noisy]

        if self.class_mode == 'input':
            #return np.array(x), np.array(y)  # Devolver imágenes de entrada y salida iguales
            seed = np.random.randint(1, 1000)
            X = self.datagen.flow(np.array(x), batch_size=self.batch_size, seed=seed).next()
            y = self.datagen.flow(np.array(y), batch_size=self.batch_size, seed=seed).next()

            #return self.datagen.flow(np.array(x), np.array(y), batch_size=self.batch_size).next()
            return X,y
        
        elif self.class_mode == 'output':
            return np.array(x)  # Devolver solo las imágenes de salida (limpias)
        else:
            raise ValueError("Invalid class_mode. Use 'input' or 'output'.")

    def on_epoch_end(self):
        self.indexes = np.arange(len(self.image_paths_clean))
        if self.shuffle:
            np.random.shuffle(self.indexes)

    def load_and_preprocess_image(self, file_path):
        img = tf.keras.preprocessing.image.load_img(file_path, target_size=self.target_size, color_mode='grayscale')
        img_array = tf.keras.preprocessing.image.img_to_array(img)

        img_array = img_array / 255.
        img_array = img_array.astype('float16')

        return img_array