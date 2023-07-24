import random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path


class CoffeeStainImageGenerator:
    def __init__(self, width, height, tipo: str, num_stains=10):
        """Resumen

        Args:
            tipo (str): elegir alguna de las siguentes:
                        "ellipse", "polygon", "line"
            num_stains (int, optional): Numeros de figuras generadas
        """
        
        self.width = width
        self.height = height
        self.image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        self.draw = ImageDraw.Draw(self.image)
        self.tipo = tipo
        self.num_stains = num_stains
        self.generate_coffee_stain_image()

        
    def _random_coffee_color(self):
        return (
            np.random.randint(40, 80),
            np.random.randint(20, 60),
            np.random.randint(0, 30),
            np.random.randint(150, 200)
        )
    
    def generate_ellipse(self):
        x1, y1 = np.random.randint(0, self.width-100), np.random.randint(0, self.height-100)
        x2, y2 = x1 + np.random.randint(40, 150), y1 + np.random.randint(60, 120)
        coffee_color = self._random_coffee_color()
        ellipse_image = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        ellipse_draw = ImageDraw.Draw(ellipse_image)
        ellipse_draw.ellipse([(x1, y1), (x2, y2)], fill=coffee_color)
        return ellipse_image.filter(ImageFilter.GaussianBlur(7))
    
    def generate_line(self):
        x1, y1 = np.random.randint(0, self.width-100), np.random.randint(0, self.height-100)
        x2, y2 = np.random.randint(0, self.width), np.random.randint(0, self.height)
        coffee_color = self._random_coffee_color()
        line_image = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        line_draw = ImageDraw.Draw(line_image)
        line_draw.line([(x1, y1), (x2, y2)], fill=coffee_color,width=np.random.randint(30, 90))
        return line_image.filter(ImageFilter.GaussianBlur(7))
        
    def generate_poly(self):
        num_points = np.random.randint(10, 20)
        points = [(np.random.randint(0, self.width), np.random.randint(0, self.height)) for _ in range(num_points)]
        coffee_color = self._random_coffee_color()
        poly_image = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        poly_draw = ImageDraw.Draw(poly_image)
        poly_draw.polygon(points, fill=coffee_color)
        return poly_image.filter(ImageFilter.GaussianBlur(1))

    def generate_coffee_stain_image(self):
       
        if self.tipo == "ellipse":
            for i in range(self.num_stains):
                ellipse_image= self.generate_ellipse()
                paste_pos = (0,0)
                self.image.paste(ellipse_image, paste_pos, mask=ellipse_image)
                
        elif self.tipo == "line":
            for i in range(self.num_stains):
                line_image= self.generate_line()
                paste_pos = (0,0)
                self.image.paste(line_image, paste_pos, mask=line_image)
                
        elif self.tipo == "polygon":
            for i in range(self.num_stains):
                poly_image = self.generate_poly()
                paste_pos = (0,0)
                self.image.paste(poly_image, paste_pos, mask=poly_image)
                
        elif self.tipo == 'mix':
            for i in range(self.num_stains):
                shape = np.random.choice(["ellipse", "line"])
                if shape == "ellipse":
                    ellipse_image= self.generate_ellipse()
                    paste_pos = (0,0)
                    self.image.paste(ellipse_image, paste_pos, mask=ellipse_image)
                elif shape == "line":
                    poly_image = self.generate_line()
                    paste_pos = (0,0)
                    self.image.paste(poly_image, paste_pos, mask=poly_image)
        else:
            for i in range(self.num_stains):
                self.self.generate_ellipse()

        return self.image
    

def hacer_manchas(cantidad: int, IMAGEN: Path, manchas: list):
    ruta_imagen_original = str(IMAGEN)
    imagen_original = Image.open(ruta_imagen_original)
    for i in range(cantidad):
        ruta_mancha_cafe = str(random.choice(manchas))
        mancha_cafe = Image.open(ruta_mancha_cafe)
        posicion_x = np.random.randint(50,1650)
        posicion_y = np.random.randint(50,1150)
        alpha = 0.9
        mancha_cafe = mancha_cafe.convert("RGBA")
        data = mancha_cafe.getdata()
        new_data = []
        for item in data:
            new_data.append((*item[:3], int(item[3] * alpha)))
        mancha_cafe.putdata(new_data)
        imagen_original.paste(mancha_cafe, (posicion_x, posicion_y), mask=mancha_cafe)
    return imagen_original