import requests
import json
import os

class Producto:
    def __init__(self, name, description, price, category, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.quantity = quantity
    
    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nPrice: {self.price}\nCategory: {self.category}\nQuantity: {self.quantity}"

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
        with open("productos.txt", 'w') as f:
            for producto in self.productos:
                f.write(f'{producto.name},{producto.description},{producto.price},{producto.category},{producto.quantity}\n')
   
    # Revisar lo de la ruta donde se guarda
    # Este es 2 porque cambia de 'w' a 'a' para que haga un append en vez de write ya que los elementos anteriores se borraban y solo se imprimia en el txt el nuevo
    def guardar_productos2_txt(self):
        with open("productos.txt", 'a') as f:
            for producto in self.productos:
                f.write(f'{producto.name},{producto.description},{producto.price},{producto.category},{producto.quantity}\n')

    def buscar_producto(self, name=None, category=None):
        resultados = []
        for producto in self.productos:
            if (name is None or producto.name == name) and (category is None or producto.category == category):
                resultados.append(producto)
        return resultados

    def modificar_producto(self, name, new_name=None, new_description=None, new_price=None, new_category=None, new_quantity=None):
        for i, producto in enumerate(self.productos):
            if producto.name == name:
                if new_name is not None:
                    producto.name = new_name
                if new_description is not None:
                    producto.description = new_description
                if new_price is not None:
                    producto.price = new_price
                if new_category is not None:
                    producto.category = new_category
                if new_quantity is not None:
                    producto.quantity = new_quantity
                self.productos.pop(i)  # Eliminar el producto de la posición original
                self.productos.insert(i, producto)  # Insertar el producto modificado en la misma posición
                self.guardar_productos2_txt()
                return True
        return False

    def eliminar_producto(self, name):
        for producto in self.productos:
            if producto.name == name:
                self.productos.remove(producto)
                self.guardar_productos_txt()
                return True
        return False