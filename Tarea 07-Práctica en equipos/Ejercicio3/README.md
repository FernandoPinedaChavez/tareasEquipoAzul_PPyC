# Ejercicio 3 - Procesamiento de Imagenes Digitales

Este proyecto convierte una imagen a escala de grises usando dos enfoques:

- Secuencial: `ProcesamientoDeImagenesDigitalesSecuencial.py`
- Paralelo con hilos: `ProcesamientoDeImagenesDigitalesParalelo.py`

## Requisitos

- Linux (o WSL)
- Python 3.9+
- Entorno virtual activo

Dependencias Python:

- numpy
- Pillow
- requests

## Instalacion

Si ya creaste el entorno virtual, activa el entorno e instala dependencias:

```bash
source v/bin/activate
pip install -r requirements.txt
```

Si tu entorno virtual tiene otro nombre, cambia `v` por el nombre correcto.

## Ejecucion

### Version secuencial

```bash
python ProcesamientoDeImagenesDigitalesSecuencial.py
```

Salida esperada:

- Descarga de imagen original: `imagen_original_secuencial.jpg`
- Imagen en escala de grises: `imagen_grises_secuencial.jpg`
- Tiempo de ejecucion en consola

### Version paralela

```bash
python ProcesamientoDeImagenesDigitalesParalelo.py
```

Salida esperada:

- Descarga de imagen original: `imagen_original.jpg`
- Imagen en escala de grises: `imagen_grises.jpg`
- Tiempo de ejecucion en consola

## Notas

- El script paralelo divide filas horizontales de la imagen en segmentos y asigna cada segmento a un hilo.
- Puedes ajustar la cantidad de hilos cambiando `numero_segmentos` en el archivo paralelo.
