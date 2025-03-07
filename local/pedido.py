import mysql.connector
from datetime import date
from connection import Connection

class Pedido:
    
    @staticmethod
    def agg(producto):
        producto.increment()
        
    @staticmethod
    def calcularCarrito(carrito):
        total = 0 
        for element in carrito:
            total += element.cantidadxPrecio()
            
        return total
    
    @staticmethod
    def limpiarCarrrito(carrito):
        for element in carrito:
            element.resetCantidad()
    
        
    @staticmethod
    def elementosCarrito(lista):
        cadenaNormal = 'Molotes normales: {} -  $ {}'.format(lista[0].cantidad, lista[0].cantidadxPrecio())
        cadenaMixto = 'Molotes mixtos: {} -  $ {}'.format(lista[1].cantidad,lista[1].cantidadxPrecio())
        cadenaTinga = 'Tostadas tinga: {} -  $ {}'.format(lista[2].cantidad, lista[2].cantidadxPrecio())
        cadenaPata = 'Tostadas pata: {} -  $ {}'.format(lista[3].cantidad, lista[3].cantidadxPrecio())
        cadenaBebidaMedio = 'Refrescos: {} -  $ {}'.format(lista[4].cantidad, lista[4].cantidadxPrecio())
        coffe = 'Cafés: {} -  $ {}'.format(lista[5].cantidad, lista[5].cantidadxPrecio())
    
        return f'{cadenaNormal}\n\n{cadenaMixto}\n\n{cadenaTinga}\n\n{cadenaPata}\n\n{cadenaBebidaMedio}\n\n{coffe}\n\nTotal: ${Pedido.calcularCarrito(lista)}'
    
    
            

    @staticmethod
    def getImportantInfo():
        key = Connection.connectBD()
        
        if key is None:
            print("No se pudo establecer la conexión con la base de datos.")
            return
        
        cursor = key.cursor()
        
        try:
            cursor.execute("SELECT id, fecha, cuenta_total FROM pedido")
            myresult = cursor.fetchall()
            return myresult
            
        except mysql.connector.Error as error:
            print('Error: {}'.format(error))
        finally:
            cursor.close()
            key.close()
