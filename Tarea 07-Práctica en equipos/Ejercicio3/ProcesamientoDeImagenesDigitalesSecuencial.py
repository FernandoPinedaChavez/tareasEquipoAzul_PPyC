import requests
from PIL import Image
import numpy as np
import io
import time

url_img = "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?w=1080"

with open("imagen_original_secuencial.jpg", "wb") as f:
	f.write(requests.get(url_img).content)

response = requests.get(url_img)
img = Image.open(io.BytesIO(response.content))
matriz = np.array(img)  # Matriz de pixeles (Height, Width, Channels)


def escala_grises_secuencial(matriz):
	alto, ancho, canales = matriz.shape
	for i in range(alto):
		for j in range(ancho):
			r, g, b = matriz[i, j]
			# Ecuacion de luminancia CIE 1931
			gris = int(0.299 * r + 0.587 * g + 0.114 * b)
			matriz[i, j] = [gris, gris, gris]
	with open("imagen_grises_secuencial.jpg", "wb") as f:
		Image.fromarray(matriz).save(f)
	return matriz


if __name__ == "__main__":
	inicio_tiempo = time.time()
	escala_grises_secuencial(matriz)
	fin_tiempo = time.time()
	print(f"Tiempo de ejecucion secuencial: {fin_tiempo - inicio_tiempo} segundos")
