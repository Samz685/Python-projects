class Square:

    def __init__(self,lado):
        self.lado = lado

    def perimetro(self):
        perimetro = self.lado*4
        return "El perimetro es de: " +str(perimetro)
    
    def superficie(self):
        superficie = self.lado*self.lado
        return "La superficie es de: " +str(superficie)