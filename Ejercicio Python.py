

def run():


    

    print(  "[1] EJERCICIO 1 \n"
            "[2] EJERCICIO 2 \n"
            "[3] EJERCICIO 3 \n"
            "[4] EJERCICIO 4")
    opcion = int(input("Elige una opción: "))




    if opcion == 1:
        ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 3:
        ejercicio3()
    elif opcion == 4:
        ejercicio4()
    

def ejercicio1():
    print("Bienvenido al Ejercicio 1!")
    salario = int(input("Introduzca el salario: \n"))
    antigüedad = int(input("Y ahora la antigüedad: \n"))

    if salario < 1000 and antigüedad >= 5:
         salario = salario * 1.15
         print("Con una antiguedad de "+str(antigüedad)+" años se incrementará el sueldo en un 15%.\n El sueldo será de "+str(salario)+"€")
    elif salario < 1000 and antigüedad < 5:
        salario = salario * 1.05
        print("Con una antiguedad de "+str(antigüedad)+" años se incrementará el sueldo en un 5%.\n El sueldo será de "+str(salario)+"€")
    else:
        print("El salario seguirá siendo el mismo, de "+str(salario)+"€")


def ejercicio2():

    print("Bienvenido al Ejercicio 2!")
    numeros = [7,28,14,96,25,33,25,22,10,3,7,80,90]
    pares = 0
    impares = 0
    print("Estos son los numeros enteros: "+str(numeros))
    for numero in numeros:
        if numero%2 == 0:
            pares = pares+1
        else:
            impares = impares +1
    print("Pares: " +str(pares)+ " || Impares: " +str(impares))

def ejercicio3():

    print("Bienvenido al Ejercicio 3!")
    numeros = [7,28,14,96,25,33,25,22,10,3,7,80,90]
    pares = 0
    impares = 0
    listaPares = []
    listaImpares = []
    print("Estos son los numeros enteros: "+str(numeros))
    for numero in numeros:
        if numero%2 == 0:
            pares = pares+1
            listaPares.append(numero)
        else:
            impares = impares +1
            listaImpares.append(numero)
    print(  "\nPares: " +str(pares)+ " || Impares: " +str(impares)+ "\n"
            "Lista de Pares: "+str(listaPares)+"\n"
            "Lista de Impares: "+str(listaImpares))


def ejercicio4():

    print("Bienvenido al Ejercicio 4!")
    palabra = input("Introduce una palabra: ")
    newPalabra = ""
    letra = ""

    for l in palabra:
        letra = l
        
        if letra in newPalabra:
            letra = ""
        else:
            newPalabra += letra

        

        
        
        

     
    print(newPalabra)







if __name__ == '__main__':
    run()