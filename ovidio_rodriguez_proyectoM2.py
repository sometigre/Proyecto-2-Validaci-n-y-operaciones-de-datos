# Validación y operaciones de datos

# -------- Parte 1: LLongitud de una frase --------

# Le pedimos al usuario que escriba una palabra
palabra = input("Escribe una palabra: ")

# Contamos cuántas letras tiene la palabra
longitud = len(palabra)

# Revisamos si la cantidad de letras está entre 4 y 8 
if 4 <= longitud <= 8:
    print("La palabra es correcta.")  #Si escribimos una palabra con 8 letras exactas
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.") # Si escribimos una palabra con menos de 8 letras
else:  # longitud > 8
    print(f"Sobran letras. Tiene {longitud} letras.") # Si escribimos una palabra con mas de 8 letras

# -------- Parte 2: Cuadrante de un punto --------

# Le pedimos al usuario dos números: uno para X (horizontal) y otro para Y (vertical) 


x = int(input("Escribe el número para X: ")) 
y = int(input("Escribe el número para Y: "))
# El sistema carteciano cuenta con cuatro cuadrantes, I, II, III, y IV, siendo las X horizontales y las Y las verticales
# Verificamos que ninguno de los números sea cero
if x == 0 or y == 0:
    print("Las coordenadas no pueden ser cero. No se puede determinar el cuadrante.") # Es muy impotante poner reglas para valores reales
else:
    # Según si los números son positivos o negativos, decimos en qué cuadrante está
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.") # El cuadrante I es representado por los numeros naturales (positivos) de X y Y
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.") # El cuadrante II es representado por los numeros positivos Y, y Negativos X
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.") # El cuadrante III es representado por los Negativos X y Y
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV.") # El cuadrante IV es representado por lso positivos X y negativos Y.
