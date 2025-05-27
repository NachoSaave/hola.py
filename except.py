# while True:
#     try:
#         num=int(input("Ingrese un número: "))
#         break
#     except Exception:
#         print("Solo puede ingresar números enteros")


# Ejemplo de sintataxis de try except 
# try:
#     num=int(input("Ingrese un número: "))
# except Exception:
#     print("Solo puede ingresar números enteros")
# else:
#     print("Si no hay excepción")
# finally:
#     print("Este bloque es ejecutará si o si, sin importar si hay excepción o no")


# while True:
#     try:
#         opcion=int(input('''
#             Seleccione una opción
#             1.-Opción 1 
#             1.-Opción 2
#             1.-Opción 3 
#             1.-Opción 4 '''))
#         match opcion:
#             case 1:
#                 print("Has seleccionado opcion 1")
#             case 2:
#                 print("Has seleccionado opcion 2")
#             case 3:
#                 print("Has seleccionado opcion 3")
#             case 4:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Opción invalida")
#     except Exception:
#         print("Solo puede ingresar numeros enteros")
