import re
import csv

def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()
    
def extraer_productos(html):
    regex_nombre = r'<h3>\s*<a[^>]*class="list-hide"[^>]*>.*?</a>\s*<a[^>]*class="list-show"[^>]*>(.*?)</a>\s*</h3>' #Regex de texto en HTML
    regex_imagen = r'<a href="https://istore\.gt/product/[^"]+">\s*<img[^>]*src="(https://istore\.gt/wp-content/uploads/[^"]+)"' #Regex de imagen en HTML
    
    nombres = re.findall(regex_nombre, html, re.DOTALL)
    imagenes = re.findall(regex_imagen, html, re.DOTALL)
    
    return zip(nombres, imagenes)

def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre del Producto", "URL de la Imagen"])
        writer.writerows(productos)
    
def procesar_productos_en_buffer(productos, tamano_buffer):
    buffer = []
    for producto in productos:
        buffer.append(producto)
        if len(buffer) >= tamano_buffer:    
            yield buffer
            buffer = []

    if buffer:
        yield buffer

# Ejecución principal
tamano_buffer = 100
raw_html = cargar_html("index.html")
productos = list(extraer_productos(raw_html))

archivo_salida = "productos.csv"
with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Nombre del Producto", "URL de la Imagen"])
    
    for buffer in procesar_productos_en_buffer(productos, tamano_buffer):
        writer.writerows(buffer)
