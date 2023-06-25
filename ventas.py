class Venta:
    def __init__(self, cliente, productos, cantidad, pago, envio):
        self.cliente = cliente
        self.productos = productos
        self.cantidad = cantidad
        self.pago = pago
        self.envio = envio

class GestionVentas:
    def __init__(self):
        self.ventas = []

    def agregar_venta(self, cliente, productos, cantidad, pago, envio):
        venta = Venta(cliente, productos, cantidad, pago, envio)
        self.ventas.append(venta)

    def guardar_ventas_txt(self):
        with open('ventas.txt', 'w') as f:
            for venta in self.ventas:
                f.write(f'{venta.id},{venta.cliente.id},{[producto.id for producto in venta.productos]}\n')
