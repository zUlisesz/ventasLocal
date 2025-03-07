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
    
