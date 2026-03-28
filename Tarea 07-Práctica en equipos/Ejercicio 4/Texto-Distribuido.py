import urllib.request
from collections import Counter
import re
import threading

# Lista de libros
libros = [
    ("https://www.gutenberg.org/cache/epub/1342/pg1342.txt", "Orgullo y Prejuicio"),
    ("https://www.gutenberg.org/cache/epub/84/pg84.txt", "Frankenstein"),
    ("https://www.gutenberg.org/cache/epub/11/pg11.txt", "Alicia en el país de las maravillas")
]

# Lista compartida para guardar resultados parciales
resultados_parciales = []

# Lock para controlar acceso concurrente
lock = threading.Lock()


def contar_palabras(url):
    respuesta = urllib.request.urlopen(url)
    texto = respuesta.read().decode("utf-8").lower()
    palabras = re.findall(r'\b\w+\b', texto)
    return Counter(palabras)


def procesar_libro(url, nombre):
    print(f"Iniciando análisis de: {nombre}")
    contador = contar_palabras(url)

    with lock:
        resultados_parciales.append((nombre, contador))

    print(f"Finalizó análisis de: {nombre}")


if __name__ == "__main__":
    hilos = []

    for url, nombre in libros:
        hilo = threading.Thread(target=procesar_libro, args=(url, nombre))
        hilos.append(hilo)

     # Iniciar los hilos
    for hilo in hilos:
        hilo.start()

    # Esperar hilos
    for hilo in hilos:
        hilo.join()

    resultado_final = Counter()

    for nombre, contador in resultados_parciales:
        resultado_final.update(contador)

    # Mostrar top 20
    print("\nTop 20 palabras más frecuentes:")
    for palabra, frecuencia in resultado_final.most_common(20):
        print(f"{palabra}: {frecuencia}")