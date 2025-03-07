from connection import Connection
from pedido import Pedido
from datetime import date
import mysql.connector

class Query:
    
        
    @staticmethod
    def sendPackage(carrito):
        key = Connection.connectBD()
        if  key  is None:
            print("No se pudo establecer la conexión con la base de datos.")
            return
        
        cursor = key.cursor()
        
        query = '''
        INSERT INTO local.pedido (molote_normal, molote_mixto, tostada_tinga, tostada_pata, refresco, cafe, fecha, cuenta_total)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);\ncommit; '''
        
        values = (
            carrito[0].cantidad,
            carrito[1].cantidad,
            carrito[2].cantidad,
            carrito[3].cantidad,
            carrito[4].cantidad,
            carrito[5].cantidad,
            date.today(),
            Pedido.calcularCarrito(carrito),
        )
        
        try:
            cursor.execute(query, values)
            print("Pedido enviado correctamente.")
        except mysql.connector.Error as error:
            print('Error: {}'.format(error))
        finally:
            cursor.close()
            key.close()
    
            
    @staticmethod
    def getAll( tree):
        
        for row in tree.get_children():
                tree.delete(row)
        
        key = Connection.connectBD()
        
        if key is None:
            print("No se pudo establecer la conexión con la base de datos.")
            return
        
        cursor = key.cursor()
        
        try:
            cursor.execute("SELECT * FROM pedido")
            myresult = cursor.fetchall()
            
            for row in myresult:
                tree.insert("", "end", values=row)
                
        except mysql.connector.Error as error:
            print('Error: {}'.format(error))
        finally:
            cursor.close()
            key.close()