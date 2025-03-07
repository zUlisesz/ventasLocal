import json
from pedido import Pedido

class Producto:
    
    carrito = []
    
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio 
        self.cantidad = 0
        Producto.carrito.append(self)
            
    def info(self):
        return '{}, precio: {}, cantidad: {}'.format(self.tipo, self.precio, self.cantidad)
    
    def increment(self):
        self.cantidad += 1
        
    def cantidadxPrecio(self):
        return self.cantidad * self.precio
        
    def resetCantidad(self):
        self.cantidad = 0
        
    @staticmethod     
    def guardarPedido(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        newCarrito = []
        for producto in Producto.carrito:
            data = {
                'Tipo': producto.tipo,
                'Cantidad': producto.cantidad,
                'Precio': producto.precio
            }
            newCarrito.append(data)

        existing_data.extend(newCarrito)
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(existing_data, file, indent=4, ensure_ascii=False)
            print("Datos enviados correctamente a: {}".format(filename))
        except Exception as e:
            print("{}".format(e))
    
    @classmethod
    def savePedido(cls, archivo):
        pedidos = [{"Tipo": u.tipo, "Precio": u.precio, "Cantidad": u.cantidad} for u in cls.carrito]
        with open(archivo, "w") as f:
            json.dump(pedidos, f, indent=4)
