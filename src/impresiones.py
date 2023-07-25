from PIL import Image, ImageDraw, ImageFilter
import random 
from pathlib import Path

class Impresion:
    def __init__(self):
        self.imagen_path = None
        self.imagen = None

    def direccion(self, dir):
        self.imagen_path = dir
        self.imagen = Image.open(dir)
     
    def coordenas_random(self):
        coor = [random.randint(50, 1400), random.randint(50,900)]
        coor2 =  [coor[0]+random.randint(200,500),coor[1]+random.randint(200,500)]
        return coor + coor2       
            
    def recortar(self, coordenadas):
        """
        Recorta una parte de la imagen.

        Args:
            coordenadas (tuple): Tupla con las coordenadas del área a recortar en formato (x1, y1, x2, y2).

        Returns:
            Image: La imagen recortada.
        """
        x1, y1, x2, y2 = coordenadas
        recorte = self.imagen.crop((x1, y1, x2, y2))
        return recorte
    
    def hacer_impresiones(self, recorte: Image, coordenadas: list):
        imagen_original = self.imagen
        recorte = recorte
        posicion_x = coordenadas[0]+random.randint(-50,50)
        posicion_y = coordenadas[1]+random.randint(-50,50)
        alpha = 0.5
        angulo_rotacion = random.randint(-1,1)
        recorte = recorte.rotate(angulo_rotacion, expand=True)
        
        recorte = recorte.convert("RGBA")
        data = recorte.getdata()
        new_data = []
        print(data)
        for item in data:
            new_data.append((*item[:3], int(item[3] * alpha)))
        recorte.putdata(new_data)
        imagen_original.paste(recorte, (posicion_x, posicion_y), mask=recorte)
        return imagen_original
    
