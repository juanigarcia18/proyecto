class Envio:
    def __init__(self, order_compra, servicio, direccion, estado):
        self.order_compra = order_compra
        self.servicio = servicio
        self.direccion = direccion
        self.estado = estado

class GestionEnvios:
    def __init__(self):
        self.envios = []

    def registrar_envio(self, order_compra, servicio, direccion, estado):
        envio = Envio(order_compra, servicio, direccion, estado)
        self.envios.append(envio)

    def buscar_envio(self, order_compra=None, servicio=None, estado=None):
        resultados = []
        for envio in self.envios:
            if (order_compra is None or envio.order_compra == order_compra) and \
                (servicio is None or envio.servicio == servicio) and \
                (estado is None or envio.estado == estado):
                resultados.append(envio)
        return resultados
