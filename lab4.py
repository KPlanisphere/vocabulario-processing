import os
import re

# Función para obtener el vocabulario de un archivo
def obtener_vocabulario(archivo):
    with open(archivo, 'r') as f:
        texto = f.read()
        palabras = re.findall(r'\b(?![0-9]+\b)\w+\b', texto.lower())
        return set(palabras)  

# Carpeta donde se encuentran los archivos .txt
directoriardo = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab4'
directorio = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab4\documentos'
output_file = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab4\vocabularioTruncado.txt'
output_file_final = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab4\vocabularioReducidoT.txt'

# Lista para almacenar el vocabulario de todos los archivos
vocabulario_total = set()

# Recorremos todos los archivos en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith('.txt'):
        ruta_archivo = os.path.join(directorio, archivo)
        vocabulario_archivo = obtener_vocabulario(ruta_archivo)
        vocabulario_total.update(vocabulario_archivo)

# Ordenamos el vocabulario alfabéticamente
vocabulario_ordenado = sorted(vocabulario_total)

# Recorremos todos los archivos en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith('.txt'):
        ruta_archivo = os.path.join(directorio, archivo)
        palabras_archivo = obtener_vocabulario(ruta_archivo)
        cantidad_palabras = len(palabras_archivo)
        #print(f"Documento: {archivo} - Cantidad de palabras: {cantidad_palabras}")

# Eliminamos palabras de 2 caracteres o menos
vocabulario_filtrado = [palabra for palabra in vocabulario_ordenado if len(palabra) > 2]

for archivo in os.listdir(directoriardo):
    if archivo.endswith('.txt'):
        ruta_archivo = os.path.join(directoriardo, archivo)
        palabras_archivo = obtener_vocabulario(ruta_archivo)
        cantidad_palabras = len(palabras_archivo)
        print(f"Documento: {archivo} - Cantidad de palabras: {cantidad_palabras}")
        