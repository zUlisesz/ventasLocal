from tkinter import *
from producto import Producto
from pedido import Pedido
from PIL import Image, ImageTk

def moverPedidos():
    mainWindow.withdraw()
    ventanaPedido()
    

def moverVentas():
    pass

def main():
    global mainWindow
    mainWindow = Tk()
    mainWindow.geometry('400x400')
    
    pedidos = Button( mainWindow, text = 'Hacer Pedido',font = ('Aptos', 20, 'bold'),  command= moverPedidos)
    ventas = Button(mainWindow, text = 'Revisar ventas', font = ('Aptos', 20 , 'bold'), command= moverVentas)
    
    pedidos.pack(pady = 20 )
    ventas.pack(pady = 20)
    
    mainWindow.mainloop()
    
    
def ventanaPedido(): 
        
    global ventasWindow, carritoLabel
    
    ventasWindow = Toplevel()
    ventasWindow.title('Main')
    ventasWindow.config(bg = "AliceBlue")
    ventasWindow.resizable(width= False , height= False)
    
    #frame para imprimir la cuenta
    frame = LabelFrame(ventasWindow, text = 'CUENTA TOTAL', padx = 70, pady = 80, border= 4,)
    carritoLabel = Label(frame, text= Pedido.elementosCarrito(carrito), font= ('bold') )
    carritoLabel.pack()
    
    #letreros 
    mainLabel = Label(ventasWindow, text = 'CREANDO PEDIDO', font= ('Aptos', 26, 'bold'), bg = 'AliceBlue')
    molotesLabel = Label(ventasWindow , text = 'MOLOTES', font= ( 'Aptos', 18,'bold'), bg = 'AliceBlue')
    tostadasLabel = Label(ventasWindow, text= 'TOSTADAS',font= ('Aptos', 18,'bold'), bg = 'AliceBlue')
    bebidasLabel = Label(ventasWindow, text = 'BEBIDAS', font= ('Aptos', 18,'bold'), bg = 'AliceBlue')
    
    #botones para agregar molotes
    normalBoton = Button(ventasWindow, text = 'NORMAL', font= ('Aptos', 14,'bold'), command= lambda: updateCar(moloteNormal),border= 4)
    mixtoBoton = Button(ventasWindow, text = 'MIXTO', font= ('Aptos', 14,'bold'), command= lambda: updateCar(moloteMixto), border= 4)
    
    #botones para agregar tostadas
    tingaBoton = Button(ventasWindow, text = 'TINGA', font= ('Aptos', 14,'bold'), command= lambda: updateCar(tostadaTinga), border= 4)
    pataBoton  = Button(ventasWindow, text = 'PATA', font= ('Aptos', 14,'bold'), command= lambda: updateCar(tostadaPata), border = 4)
    
    #boton para agregar bebidas
    refresco = Button(ventasWindow, text  = 'REFRESCO', font= ('Aptos', 14,'bold'), command= lambda: updateCar(bebidaMedio), border = 4)
    cafe = Button(ventasWindow, text  = 'CAFÉ', font= ('Aptos', 14,'bold'), command= lambda: updateCar(coffee), border = 4)
    
    guardarBoton =  Button(ventasWindow, text  = 'GUARDAR', font= ('Aptos', 16, 'bold'), padx = 14 , border = 4,  command= save)

    #empaquetado de los widgets de la pantalla
    mainLabel.grid(row  = 0 , column= 1, columnspan= 3, pady = 10 ,sticky= 'W')
    
    frame.grid(row=1, column= 3, rowspan= 6, padx= 20 , pady = 20 )
    
    molotesLabel.grid( row = 1, column= 0 ,padx =20  , pady = 2)
    normalBoton.grid(row = 2, column= 0 , padx = 20 , pady = 2)
    mixtoBoton.grid(row = 2, column= 1, padx = 20 ,pady = 2)
    
    tostadasLabel.grid(row = 3, column= 0 ,padx = 20 , pady = 2  )
    tingaBoton.grid(row = 4, column= 0, padx = 20 , pady= 2 )
    pataBoton.grid(row= 4, column= 1, padx = 20 , pady = 2)
    
    bebidasLabel.grid( row = 5, column= 0 , padx = 20 , pady = 2)
    refresco.grid( row = 6, column= 0, padx = 20 , pady = 2)
    cafe.grid(row = 6, column=1 , padx = 20 , pady = 2)
    
    guardarBoton.grid(row = 7 , column= 0, pady = 20,sticky= 'E')

    ventasWindow.mainloop()
    

def save():
    Pedido.sendPackage(carrito)
    Pedido.limpiarCarrrito(carrito)
    carritoLabel.config( text= Pedido.elementosCarrito(carrito))

def updateCar(producto):
    Pedido.agg(producto)
    carritoLabel.config( text= Pedido.elementosCarrito(carrito))
     
moloteNormal = Producto('MoloteNormal', 13)
moloteMixto = Producto('MoloteMixto', 15)
 
tostadaTinga = Producto('TostadaTinga', 35)
tostadaPata = Producto('TostadaPata', 40)

bebidaMedio = Producto('Bebida', 25)
coffee = Producto('Coffee', 15) 

carrito = [moloteNormal, moloteMixto, tostadaTinga, tostadaPata, bebidaMedio, coffee]


main()
