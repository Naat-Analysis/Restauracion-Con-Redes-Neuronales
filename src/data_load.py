import numpy as np
import tensorflow as tf
from keras.utils import Sequence

class CustomImageDataGenerator(Sequence):
    def __init__(self, image_paths_noisy, image_paths_clean , batch_size, target_size, class_mode='input',shuffle=True):
        self.image_paths_noisy = image_paths_noisy
        self.image_paths_clean = image_paths_clean
        self.batch_size = batch_size
        self.target_size = target_size
        self.class_mode = class_mode
        self.shuffle = shuffle
        self.on_epoch_end()

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
            return np.array(x), np.array(y)  # Devolver imágenes de entrada y salida iguales
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