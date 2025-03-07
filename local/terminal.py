from connection import Connection
from producto import Producto
from pedido import Pedido

moloteNormal = Producto('MoloteNormal', 13)
moloteMixto = Producto('MoloteMixto', 15)
 
tostadaTinga = Producto('TostadaTinga', 35)
tostadaPata = Producto('TostadaPata', 40)

bebidaMedio = Producto('Bebida', 25)
coffee = Producto('Coffee', 15)


lista = [moloteNormal, moloteMixto, tostadaTinga, tostadaPata, bebidaMedio, coffee]

for element in lista:
    Pedido.agg(element)
    
for element in lista:
    Pedido.agg(element)
    
for element in lista:
    Pedido.agg(element)
    
for element in lista:
    Pedido.agg(element)
    
Pedido.sendPackage(lista)