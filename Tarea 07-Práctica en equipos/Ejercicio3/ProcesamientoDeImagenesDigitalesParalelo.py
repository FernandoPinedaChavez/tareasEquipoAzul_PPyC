import threading
import requests
from PIL import Image
import numpy as np
import io
import time

url_img = "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?w=1080"

with open("imagen_original.jpg", "wb") as f:
    f.write(requests.get(url_img).content)

response = requests.get(url_img)
img = Image.open(io.BytesIO(response.content))
matriz = np.array(img)  # Matriz de pixeles (Height, Width, Channels)


def escala_grises_paralela(matriz,inicio, fin):
    for i in range(inicio, fin):
        for j in range(ancho):
            r, g, b = matriz[i, j]
            # Ecuacion de luminancia CIE 1931
            gris = int(0.299 * r + 0.587 * g + 0.114 * b)
            matriz[i, j] = [gris, gris, gris]
    with open("imagen_grises.jpg", "wb") as f:
        Image.fromarray(matriz).save(f)
    return matriz


if __name__ == "__main__":

    numero_segmentos = 8
    alto, ancho, canales = matriz.shape
    filas_por_hilo = alto // numero_segmentos
    hilos = []

    inicio_tiempo = time.time()

    for i in range(numero_segmentos):
        fila_inicio = i * filas_por_hilo
        fila_fin = (i + 1) * filas_por_hilo if i != numero_segmentos - 1 else alto
        hilo = threading.Thread(target=escala_grises_paralela, args=(matriz, fila_inicio, fila_fin))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    fin_tiempo = time.time()
    print(f"Tiempo de ejecución: {fin_tiempo - inicio_tiempo} segundos")

# Tarea: Dividir el rango de filas en N segmentos y distribuir entre N hilos