import requests
import json
#from productos import Producto

class Producto:
    def __init__(self, name, description, price, category, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.quantity = quantity

class GestionProductos:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, name, description, price, category, quantity):
        producto = Producto(name, description, price, category, quantity)
        self.productos.append(producto)

    def obtener_productos_api(self):
        response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json')
        data = response.json()
        for item in data:
            self.agregar_producto(item['name'], item['description'], item['price'], item['category'], item['quantity'])

    
    # Revisar lo de la ruta donde se guarda
    def guardar_productos_txt(self):
        ruta_archivo = r'c:\Users\USUARIO\Desktop\UNIMET\ALGORITMOS Y PROGRAMACION\proyecto\productos.txt'
        with open("productos.txt", 'w') as f:
            for producto in self.productos:
                f.write(f'{producto.name},{producto.description},{producto.price},{producto.category},{producto.quantity}\n')
