class Cliente:
    def __init__(self, nombre, tipo_cliente, documento, correo, direccion, telefono):
        
        self.nombre = nombre
        self.tipo_cliente = tipo_cliente
        self.documento = documento
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

class GestionClientes:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, nombre, tipo_cliente, documento, correo, direccion, telefono):
        cliente = Cliente(nombre, tipo_cliente, documento, correo, direccion, telefono)
        self.clientes.append(cliente)

    def guardar_clientes_txt(self):
        with open('clientes.txt', 'w') as f:
            for cliente in self.clientes:
                f.write(f'{cliente.nombre},{cliente.tipo_cliente},{cliente.documento},{cliente.correo},{cliente.direccion},{cliente.telefono}\n')
