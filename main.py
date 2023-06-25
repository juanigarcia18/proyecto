from productos import GestionProductos
from ventas import GestionVentas
from clientes import GestionClientes
from pagos import GestionPagos
from envios import GestionEnvios
from estadisticas import Estadisticas
import os

def main():
    ruta_archivo = r'c:\Users\USUARIO\Desktop\UNIMET\ALGORITMOS Y PROGRAMACION\proyecto\productos.txt'
    gestion_productos = GestionProductos()
    if os.path.isfile(ruta_archivo):
        print("chiguire") # hacer funcion que lea el txt que se creo y hablar con yon
    
    else :
        gestion_productos.obtener_productos_api()
        gestion_productos.guardar_productos_txt()
    
    gestion_productos = GestionProductos()
    gestion_productos.obtener_productos_api()
    gestion_ventas = GestionVentas()
    gestion_clientes = GestionClientes()
    gestion_pagos = GestionPagos()
    gestion_envios = GestionEnvios()
    estadisticas = Estadisticas(gestion_ventas.ventas, gestion_pagos.pagos, gestion_envios.envios)

    while True:
        print("1-Registrar Producto")
        print("2-Registrar ventas")
        print("3-Registrar clientes")
        print("4-Registrar pago")
        print("5-Registrar envio")
        print("6-Generar informe ventas")
        print("7-Generar informe pagos")
        print("8-Generar informe envios")
        print("9-Salir")
        
        accion = input("¿Que desea hacer? Escriba su seleccion:\n")
        
        if accion == "1":
            name = input("Introduce el nombre del producto: ")
            description = input("Introduce la descripcion del producto: ")
            price = input("Introduce el precio del producto: ")
            while not price.replace(".", "").isdigit() or not price.replace(",", "").isdigit() :
                price = input("Error de sintaxis\nIntroduce el precio del producto: ")
            price = float(price)
            category = input("Introduce la categoria del producto: ")
            quantity = input("Introduce la cantidad del producto: ")
            while not quantity.isnumeric():
                quantity = input("Error de sintaxis\nIntroduce la cantidad del producto: ")
            quantity = int(quantity)
            gestion_productos.agregar_producto(name, description, price, category, quantity)
        
        elif accion == "2":
            
            cliente = input("Introduzca su nombre ")
            productos = input("Introduce los productos (separados por comas): ").split(",")
            cantidad = [int(x) for x in input("Introduce la cantidad de cada producto (separados por comas): ").split(",")]
            metodo_pago = input("=========Metodo de pago=========\nIntroduzca el numero de su seleccion:\n1-Zelle \n2-Pago Movil \n3-Cash \n4-Transferencia\n")
            while metodo_pago not in ["1", "2", "3", "4"]:
                print("\nError, intente nuevamente\n")
                metodo_pago = input("=========Metodo de pago=========\nIntroduzca el numero de su seleccion:\n1-Zelle \n2-Pago Movil \n3-Cash \n4-Transferencia\n")
            if metodo_pago == "1" :
                metodo_pago = "Zelle"
            if metodo_pago == "2" :
                metodo_pago = "Pago Movil"
            if metodo_pago == "3" :
                metodo_pago = "Cash"
            if metodo_pago == "4" :
                metodo_pago = "Transferencia"
            
            metodo_envio = input("=========Metodo de Envio=========\nIntroduzca el numero de su seleccion:\n1-Delivery \n2-MRW \n3-Zoom \n")
            while metodo_pago not in ["1", "2", "3"]:
                print("\nError, intente nuevamente\n")
                metodo_envio = input("=========Metodo de Envio=========\nIntroduzca el numero de su seleccion:\n1-Delivery \n2-MRW \n3-Zoom \n")
            if metodo_envio == "1" :
                metodo_envio = "Delivery"
            if metodo_envio == "2" :
                metodo_envio = "MRW"
            if metodo_envio == "3" :
                metodo_envio = "Zoom"

            subtotal = float(input("Introduce el subtotal: "))
            descuentos = 0.05
            iva = 0.16
            igtf = 0.03
            total = float(input("Introduce el total: "))
            gestion_ventas.registrar_venta(cliente, productos, cantidad, metodo_pago, metodo_envio, subtotal, descuentos, iva, igtf, total)
        
        elif accion == "3":
            
            nombre = input("Introduce el nombre del cliente: ")
            tipo_cliente =input("Introduce el tipo de cliente: ")
            documento =input("Introduce el documento del cliente: ")
            correo = input("Introduce el correo electronico del cliente: ")
            direccion =input("Introduce la direccion: ")
            telefono = input("Introduce el numero de telefono: ")
            gestion_clientes.agregar_cliente(nombre, tipo_cliente, documento, correo, direccion, telefono)
        
        elif accion == "4":
            id = input("Introduce el ID del pago: ")
            cliente = input("Introduce el cliente: ")
            monto = float(input("Introduce el monto del pago: "))
            moneda = input("Introduce la moneda del pago: ")
            tipo = input("Introduce el tipo de pago: ")
            fecha = input("Introduce la fecha del pago: ")
            gestion_pagos.registrar_pago(id, cliente, monto, moneda, tipo, fecha)
        
        elif accion == "5":
            order_compra = input("Introduce el numero de orden de compra: ")
            servicio = input("Introduce el servicio de envio: ")
            direccion = input("Introduce la direccion de envio: ")
            estado = input("Introduce el estado del envio: ")
            gestion_envios.registrar_envio(order_compra, servicio, direccion, estado)
        
        elif accion == "6":
            periodo = input("Introduce el periodo para el informe de ventas: ")
            estadisticas.generar_informe_ventas(periodo)
        
        elif accion == "7":
            periodo = input("Introduce el periodo para el informe de pagos: ")
            estadisticas.generar_informe_pagos(periodo)
        
        elif accion == "8":
            periodo = input("Introduce el periodo para el informe de envíos: ")
            estadisticas.generar_informe_envios(periodo)
        
        elif accion == "9":
            break
        
        else:
            print("Accion no valida. Por favor, intenta nuevamente.")

if __name__ == "__main__":
    main()