import time
import datetime
import os
def dibujo():
    os.system('cls' if os.name == "nt" else "clear")
    print("       ¡SOY UN SMARTWATCH!")
    print("")
    print("          ------------")
    print("/////////|             |/////////")
    print("/////////|     🍎      |/////////")
    print("/////////|    Apple    |/////////")
    print("          ------------")
    print("")

def Menu():
    print("=============================================")
    print("1. Mostrar la fecha y hora ")
    print("2. Abrir temporizador")
    print("3. Abrir Contador de pasos")
    print("4. Realizar llamada")
    print("5. Salir")
    print("=============================================")

while True:
    dibujo()
    Menu()
    funcion=input("¿Que funcion desea realizar? ")
    if funcion=="1":
        dibujo()
        today=datetime.datetime.today()
        print(f"\nFecha: {today.strftime('%d-%m-%Y')}")
        print(f"Hora: {today.strftime('%H:%M')}")
        input("Presione Enter para volver al menu principal")

    elif funcion=="2":
        dibujo()
        segundos=int(input("Ingresa la cantidad de segundos: "))
        for i in range(segundos,0,-1):
            print(i)
            time.sleep(1)
        print("Tiempo completado")
        input("Presione Enter para volver al menu principal")

    elif funcion=="3":
        dibujo()
        pasos=0
        inicio=time.time()
        print("Presiona Enter en cada paso o 'x' para finalizar: ")
        while True:
            paso=input().strip().lower()
            if paso=="":
                pasos+=1
            elif paso=='x':
                break
            else:
                print("Por que presionas eso???? SIGUE INSTRUCCIONES")
        tiempo=time.time()-inicio
        print(f"Total pasos: {pasos}")
        print(f"Tiempo de actividad:{tiempo:.2f} segundos")
        print(f"Velocidad promedio: {(pasos/tiempo):.2f} pasos/s")
        input("Presione Enter para volver al menu principal")

    elif funcion=="4":
        dibujo()
        input("Ingrese el numero a llamar: ")
        print("Llamando...")
        input("Presione Enter para finalizar la llamada")
        print("****Llamada finalizada****")
        input("Presione Enter para volver al menu principal")

    elif funcion=="5":
        print("Apagado")
        break