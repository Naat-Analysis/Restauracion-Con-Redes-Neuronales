import random
import numpy as np
from PIL import Image, ImageDraw



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
        x1, y1 = np.random.randint(0, self.width-50), np.random.randint(0, self.height-50)
        x2, y2 = x1 + np.random.randint(20, 100), y1 + np.random.randint(50, 100)
        coffee_color = self._random_coffee_color()
        self.draw.ellipse([(x1, y1), (x2, y2)], fill=coffee_color)
    
    def generate_line(self):
        x1, y1 = np.random.randint(0, self.width), np.random.randint(0, self.height)
        x2, y2 = np.random.randint(0, self.width), np.random.randint(0, self.height)
        coffee_color = self._random_coffee_color()
        self.draw.line([(x1, y1), (x2, y2)], fill=coffee_color, width=np.random.randint(10, 50))
        
    def generate_poly(self):
        num_points = np.random.randint(10, 20)
        points = [(np.random.randint(0, self.width), np.random.randint(0, self.height)) for _ in range(num_points)]
        coffee_color = self._random_coffee_color()
        self.draw.polygon(points, fill=coffee_color)

    def generate_coffee_stain_image(self):
       
        if self.tipo == "ellipse":
            for i in range(self.num_stains):
                self.generate_ellipse()
        elif self.tipo == "polygon":
            for i in range(self.num_stains):
                self.generate_poly()
        elif self.tipo == "line":
            for i in range(self.num_stains):
                self.generate_line()
        elif self.tipo == 'mix':
            for i in range(self.num_stains):
                shape = np.random.choice(["ellipse", "polygon", "line"])
                if shape == "ellipse":
                    self.generate_ellipse()
                elif shape == "polygon":
                    self.generate_poly()
                elif shape == "line":
                    self.generate_line() 
        else:
            for i in range(self.num_stains):
                self.self.generate_ellipse()

        return self.image