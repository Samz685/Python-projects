class Ejercicio1:


    def __init__(self, mylist):
        self.mylist = mylist

    def biggerSmaller(self):
        big = 0
        small = 0

        for num in self.mylist:
            if small == 0:
                small = num
            elif small > num:
                small = num
            elif big < num:
                big = num
                
            
        return "El más grande es: "+str(big)+" // El mas pequeño es: "+str(small)