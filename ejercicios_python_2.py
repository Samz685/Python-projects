from ejercicio_1 import Ejercicio1
from square import Square
from triangle import Triangle


def run():



    print(  "[1] EJERCICIO 1 \n"
            "[2] EJERCICIO 2 \n"
            "[3] EJERCICIO 3 \n")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 3:
        ejercicio3()




def ejercicio1():
    milista = [1,10,15,20,50,250,100]
    print("Bienvenido al Ejercicio 1!\n")
    print("La lista de numeros es la siguiente: "+str(milista)+"\n")
    ejercicio1 = Ejercicio1(milista)
    resultado = ejercicio1.biggerSmaller()
    
    print(str(resultado))

def ejercicio2():
    print("Bienvenido al Ejercicio 2!\n")
    print("Introduzcamos un lado del cuadrado\n")
    lado = int(input("Introduce Lado1: \n"))
    square = Square(lado)
    resultado1 = square.perimetro()
    resultado2 = square.superficie()

    print(str(resultado1))
    print(str(resultado2))

def ejercicio3():
    print("Bienvenido al Ejercicio 3!\n")
    print("Introduzcamos los 3 lados del triangulo\n")
    lado1 = int(input("Introduce Lado1: \n"))
    lado2 = int(input("Introduce Lado2: \n"))
    lado3 = int(input("Introduce Lado3: \n"))
    triangle = Triangle(lado1, lado2, lado3)

    resultado1 = triangle.hipotenusa()
    resultado2 = triangle.equilatero()

    print(str(resultado1))
    print(str(resultado2))








if __name__ == '__main__':
    run()