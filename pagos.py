class Pago:
    def __init__(self, cliente, monto, moneda, tipo, fecha):
        self.cliente = cliente
        self.monto = monto
        self.moneda = moneda
        self.tipo = tipo
        self.fecha = fecha

class GestionPagos:
    def __init__(self):
        self.pagos = []

    def registrar_pago(self, cliente, monto, moneda, tipo, fecha):
        pago = Pago(cliente, monto, moneda, tipo, fecha)
        self.pagos.append(pago)

    def buscar_pago(self, cliente=None, fecha=None, tipo=None, moneda=None):
        resultados = []
        for pago in self.pagos:
            if (cliente is None or pago.cliente == cliente) and \
                (fecha is None or pago.fecha == fecha) and \
                (tipo is None or pago.tipo == tipo) and \
                (moneda is None or pago.moneda == moneda):
                resultados.append(pago)
        return resultados
