print("=== REGISTRO DE EQUIPAJE - VUELOSCHILE ===")
#1.- Validar la cantidad total de equipaje a registrar
total_equipaje = 0
while total_equipaje <= 0:
    try:
        entrada = input("¿Cuantos equipajes desea registrar?: ")
        total_equipaje = int(entrada)
        if total_equipaje <= 0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
#inicializacion de contadores 
equipajes_cabina = 0
equipajes_bodega = 0

#2.- Ciclo de registro del equipaje
for i in range(total_equipaje):
    print(f"\n--- Registro del equipaje N° {i+1} ---")
    #validacion del codigo del ticket
    codigo_ticket = ""
    while True:
        codigo_ticket = input("Ingrese codigo de ticket (Min 5 caracteres, sin espacios)")
        if len(codigo_ticket) < 5:
            print("¡Error! el codigo debe tener almenos 5 caracteres")
            continue
        #validar que no tenga espacios
        tiene_espacios = False
        for caracter in codigo_ticket:
            if caracter == " ":
                tiene_espacios = True
        if tiene_espacios:
            print("¡Error! el codigo no debe incluir espacios")
            continue
        break
#validacion del peso
peso = -1
while peso <= 0:
    try:
        entrada_peso = input("Ingrese el peso del equipaje en KG (entero positivo) ")
        peso = int(entrada_peso)
        if peso <= 0:
            print("¡Error de pesaje! ingrese un numero positivo para el peso")
    except ValueError:
        print("¡Error de pesaje! ingrese un numero positivo para el peso")
    #3.- Clasificacion del equipaje
    if peso > 10:
        equipajes_bodega += 1
        print("Clasificado como equipaje de bodega")
    else:
        equipajes_cabina += 1
        print("Clasificado como equipaje de cabina")
#4.- Salida final
print("\n================================================")
print(f"¡El avion transportara {equipajes_cabina} equipajes en Cabina y {equipajes_bodega} equipajes en Bodega! ¡Manifiesto de carga listo!")
print("\n================================================")