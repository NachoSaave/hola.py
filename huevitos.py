# Domingo de pascua

import random
while True:
    try:
        cantNinos=int(input("Cuanto niños irán a buscar huevitos?: ")) 
        noob=0
        master=0
        legend=0
        top=0
        for n in range(cantNinos):
            cantHuevos=random.randint(5,30)
            if cantHuevos>top:
                top=cantHuevos
            print(f"El niño número {n+1} trajo {cantHuevos} huevos")
            if cantHuevos<12:
                noob+=1
            elif cantHuevos>=12 and cantHuevos<=24:
                master+=1
            else:
                legend=+1
        print(f"La cantidad de noobs es {noob}")
        print(f"La cantidad de masters es {master}")
        print(f"La cantidad de legends es {legend}")
        print(f"La mayor cantidad de huevos encontrados por un niño fue {top}")
        break
    except Exception:
        print("Ingrese numeros enteros")