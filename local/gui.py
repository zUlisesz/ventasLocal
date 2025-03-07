from tkinter import *
from queries import Query
from tkinter.ttk import Treeview
from producto import Producto
from pedido import Pedido
from PIL import Image, ImageTk

def moverPedidos():
    mainWindow.withdraw()
    ventanaPedido()
 
def fromVentasToMain():
    ventasWindow.withdraw()
    main() 
    
def fromPedidoToMain():
    pedidoWindow.withdraw()
    main()  

def moverVentas():
    mainWindow.withdraw()
    ventanaVentas()

def main():
    global mainWindow
    mainWindow = Tk()
    mainWindow.geometry('400x400')
    
    pedidos = Button( mainWindow, text = 'Hacer Pedido',font = ('Aptos', 20, 'bold'),  command= moverPedidos)
    ventas = Button(mainWindow, text = 'Revisar ventas', font = ('Aptos', 20 , 'bold'), command= moverVentas)
    
    pedidos.pack(pady = 20 )
    ventas.pack(pady = 20)
    
    mainWindow.mainloop()
    
def ventanaVentas():
    global ventasWindow
    ventasWindow = Toplevel()
    frame_all = LabelFrame(ventasWindow, text="Todos los Pedidos")
    frame_all.pack( expand= 'yes' , padx=10, pady=10)
    
    columns = ("id", "Molote normal", "Molote mixto", "Tostada tinga", "Tostada Pata", "Refresco", "Café", "Fecha", "Cuenta")
    
    tree_all = Treeview(frame_all, columns= columns, show='headings')
    tree_all.pack(fill="both", expand="yes")
    
    for col in tree_all["columns"]:
        tree_all.heading(col, text=col.upper())
        tree_all.column(col, width= 120)
        
    Query.getAll(tree_all)
    
    regresarBoton = Button(ventasWindow, text = 'REGRESAR', font= ('Aptos',16, 'bold'), command= fromVentasToMain)
    
    
    #empaquetado de los widgets a la ventana
    regresarBoton.pack(pady = 10 , padx= 10)
    
    ventasWindow.mainloop()
    
def ventanaPedido(): 
        
    global  carritoLabel, pedidoWindow
    pedidoWindow = Toplevel()
    
    pedidoWindow.title('Main')
    pedidoWindow.config(bg = "AliceBlue")
    pedidoWindow.resizable(width= False , height= False)
    
    #frame para imprimir la cuenta
    frame = LabelFrame(pedidoWindow, text = 'CUENTA TOTAL', padx = 70, pady = 80, border= 4,)
    carritoLabel = Label(frame, text= Pedido.elementosCarrito(carrito), font= ('bold') )
    carritoLabel.pack()
    
    #letreros 
    mainLabel = Label(pedidoWindow, text = 'CREANDO PEDIDO', font= ('Aptos', 26, 'bold'), bg = 'AliceBlue')
    molotesLabel = Label(pedidoWindow , text = 'MOLOTES', font= ( 'Aptos', 18,'bold'), bg = 'AliceBlue')
    tostadasLabel = Label(pedidoWindow, text= 'TOSTADAS',font= ('Aptos', 18,'bold'), bg = 'AliceBlue')
    bebidasLabel = Label(pedidoWindow, text = 'BEBIDAS', font= ('Aptos', 18,'bold'), bg = 'AliceBlue')
    
    #botones para agregar molotes
    normalBoton = Button(pedidoWindow, text = 'NORMAL', font= ('Aptos', 14,'bold'), command= lambda: updateCar(moloteNormal),border= 4)
    mixtoBoton = Button(pedidoWindow, text = 'MIXTO', font= ('Aptos', 14,'bold'), command= lambda: updateCar(moloteMixto), border= 4)
    
    #botones para agregar tostadas
    tingaBoton = Button(pedidoWindow, text = 'TINGA', font= ('Aptos', 14,'bold'), command= lambda: updateCar(tostadaTinga), border= 4)
    pataBoton  = Button(pedidoWindow, text = 'PATA', font= ('Aptos', 14,'bold'), command= lambda: updateCar(tostadaPata), border = 4)
    
    #boton para agregar bebidas
    refresco = Button(pedidoWindow, text  = 'REFRESCO', font= ('Aptos', 14,'bold'), command= lambda: updateCar(bebidaMedio), border = 4)
    cafe = Button(pedidoWindow, text  = 'CAFÉ', font= ('Aptos', 14,'bold'), command= lambda: updateCar(coffee), border = 4)
    
    guardarBoton =  Button(pedidoWindow, text  = 'GUARDAR', font= ('Aptos', 16, 'bold'), padx = 14 , border = 4,  command= save)
    regresarBoton = Button(pedidoWindow, text  = 'REGRESAR', font= ('Aptos', 16, 'bold'), padx = 14 , border = 4,  command= fromPedidoToMain)

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
    regresarBoton.grid (row = 7, column= 1, pady= 20 , sticky='E')

    pedidoWindow.mainloop()
    

def save():
    Query.sendPackage(carrito)
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
