'''Ejercicio: Escribir un programa que convierta kilómetros a millas y viceversa y que incluya un menu iteractivo'''

while True:
    print("""\nSeleccione un numero de las siguientes opciones:
      1. Kilometros a Millas
      2. Millas a Kilometros
      3. Salir\n""")
    seleccion = int(input("Opcion: "))
    
    if seleccion == 1:
        kilometros = float(input('\nIngresa los kilometros a convertir a millas: '))
        millas =  0.621371
        conversion = kilometros*millas
        print(f"\n{kilometros} kilómetros son aproximadamente: {conversion:.2f} millas")
    elif seleccion ==2:
        millas = float(input('Ingresa las millas a convertir en kilometros: '))
        kilometros =  1.60934
        conversion = kilometros*millas
        print(f"\n{millas} millas son aproximadamente: {conversion:.2f} kilometros")
    elif seleccion == 3:
        print('\nAdios!!')
        break