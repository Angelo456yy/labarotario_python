def cargar_diccionario(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
            diccionario = {}
            for linea in lineas:
                clave, valor = linea.strip().split('=')
                diccionario[clave] = valor
            return diccionario
    except FileNotFoundError:
        return {}

def guardar_diccionario(archivo, diccionario):
    with open(archivo, 'w', encoding='utf-8') as file:
        for clave, valor in diccionario.items():
            file.write(f'{clave}={valor}\n')

archivo_diccionario = "EN-ES.txt"
diccionario = cargar_diccionario(archivo_diccionario)

# Agregar las palabras
diccionario["dog"] = "perro"
diccionario["chair"] = "silla"
diccionario["table"] = "mesa"

# Guardar el diccionario actualizado en el archivo
guardar_diccionario(archivo_diccionario, diccionario)

print("Palabras agregadas con éxito.")
