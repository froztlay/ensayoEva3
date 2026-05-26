# ✈️ Registro de Equipaje - VuelosChile

¡Bienvenido al sistema automatizado de gestión y manifiesto de carga de **VuelosChile**! Este es un script interactivo desarrollado en Python diseñado para registrar, validar y clasificar el equipaje de los pasajeros antes del despegue, asegurando que se cumplan las normativas de seguridad y peso.

## 📋 Características del Proyecto

El programa realiza el flujo completo de control de carga a través de la terminal mediante cuatro etapas clave:

1. **Validación de Inventario:** Controla que el número total de maletas a registrar sea un número entero positivo.
2. **Validación del Ticket:** Verifica que el código de pasaje cumpla con las condiciones de seguridad (mínimo 5 caracteres y sin espacios intermedios).
3. **Control de Pesaje Riguroso:** Filtra entradas erróneas o strings, aceptando solo pesos válidos.
4. **Clasificación Automática:** Distribuye el equipaje según su peso:
   * **🧳 Equipaje de Cabina:** Menor o igual a 10 KG.
   * **📦 Equipaje de Bodega:** Mayor a 10 KG.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Conceptos aplicados:** Bucles condicionales (`while`, `for`), manejo de excepciones (`try-except`), manipulación y validación de strings.

---

## 🚀 Código Fuente Corrido y Optimizado

A continuación se presenta el código fuente con la lógica de bloques e indentación corregida para su correcta ejecución:

```python
print("=== REGISTRO DE EQUIPAJE - VUELOSCHILE ===")

# 1.- Validar la cantidad total de equipaje a registrar
total_equipaje = 0
while total_equipaje <= 0:
    try:
        entrada = input("¿Cuántos equipajes desea registrar?: ")
        total_equipaje = int(entrada)
        if total_equipaje <= 0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

# Inicialización de contadores 
equipajes_cabina = 0
equipajes_bodega = 0

# 2.- Ciclo de registro del equipaje
for i in range(total_equipaje):
    print(f"\n--- Registro del equipaje N° {i+1} ---")
    
    # Validación del código del ticket
    codigo_ticket = ""
    while True:
        codigo_ticket = input("Ingrese código de ticket (Min 5 caracteres, sin espacios): ")
        if len(codigo_ticket) < 5:
            print("¡Error! El código debe tener al menos 5 caracteres.")
            continue
        
        # Validar que no tenga espacios
        tiene_espacios = False
        for caracter in codigo_ticket:
            if caracter == " ":
                tiene_espacios = True
                break
        
        if tiene_espacios:
            print("¡Error! El código no debe incluir espacios.")
            continue
        break

    # Validación del peso
    peso = -1
    while peso <= 0:
        try:
            entrada_peso = input("Ingrese el peso del equipaje en KG (entero positivo): ")
            peso =# ensayoEva3
Ensayo para evaluacion de fundamentos de programacion 
