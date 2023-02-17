import math
class Triangle:

    def __init__(self,lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def hipotenusa(self):

        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            
            hipo = math.sqrt(math.pow(self.lado2,2)+math.pow(self.lado3,2))
            self.equilatero()
            
            return "Esta es la hipotenusa: "+str(hipo)
            

        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            
            hipo = math.sqrt(math.pow(self.lado1,2)+math.pow(self.lado3,2))
            self.equilatero()
            return "Esta es la hipotenusa: "+str(hipo)
           

        elif self.lado3 > self.lado1 and self.lado3 > self.lado2:
            
            hipo = math.sqrt(math.pow(self.lado1,2)+math.pow(self.lado2,2))
            self.equilatero()
            return "Esta es la hipotenusa: "+str(hipo)
        
        else:
            self.equilatero()

        
        

    def equilatero(self):

        if self.lado1 == self.lado2 == self.lado3:
             return "El triangulo es Equilatero"
        else:
            return "El triangulo no es Equilatero"
                
