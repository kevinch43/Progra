from tkinter import *
import os
import random
import time

def cargar_imagen(nombre):    #Se crea una función para abrir iamgenes
    ruta = os.path.join("img", nombre)
    imagen = PhotoImage(file = ruta)
    return imagen

class Ventana1:

    def __init__(self, master):
        self.canvas = Canvas(master, width = 600, height = 800,
                             highlightthickness=0, relief='ridge')
        self.canvas.place(x=0,y=0)
        
        self.fondo = cargar_imagen("Fondo1.gif")
        self.label_fondo = Label(self.canvas, image = self.fondo)  #Se llama al fondo de la pantalla principal
        self.label_fondo.place(x=0,y=0, width=600, height=800)

        self.v2 = Button(self.canvas, text = "Jugar", #Se crea un boton para Ir a la pantalla de juego
                                     command = self.open_window)
        self.v2.place(x=250,y=300, width=100,height=60)

        self.v2 = Button(self.canvas, text = "About", #Se crea un boton para Ir a la pantalla de About
                                     command = self.open_window2)
        self.v2.place(x=250,y=370, width=100,height=60)
        
        self.v2 = Button(self.canvas, text = "Tops", #Se crea un boton para Ir a la pantalla de Tops
                                     command = self.open_window3)
        self.v2.place(x=250,y=440, width=100,height=60)

        self.nombre= Entry(self.canvas, font= "Calibri 16")    #Se crea un entry para ingresar el nombre
        self.nombre.place(x=200, y =260, width=200, height=30)

    def open_window(self):
        global nombre
        nombre=self.nombre.get()
        Ventana2(nombre)

    def open_window2(self):
        Ventana3()

    def open_window3(self):
        Ventana4()

class Ventana2:

    def __init__(self, nombre):
                
        self.canvas = Canvas(window, width = 600, height = 800,
                             highlightthickness=0, relief='ridge')
        self.canvas.place(x=0,y=0)
        
        self.fondo_image= PhotoImage(file= "img/Fondo.gif")
        self.fondo= self.canvas.create_image(0,0, image = self.fondo_image, anchor=NW)
        
        self.nave_image= PhotoImage(file= "img/NA.png")
        self.nave= self.canvas.create_image(250,620, image = self.nave_image, anchor=NW)
        
        self.miNombre = Label(self.canvas, text ="")
        self.miNombre.place(x=480,y=760, width=100, height=30)
        self.miNombre["text"] = nombre

        self.enemy_image= PhotoImage(file= "img/NE1.png") #llamamos a la imagen del carro
        self.enemy= self.canvas.create_image(0, 100, image = self.enemy_image, anchor=NW)
        
        self.move_enemy(5,0)
        def move_enemy(self, xvelocity, yvelocity):
        
            while True:
                coordinates = self.canvas.coords(self.enemy)
                print(coordinates)
                window.update()
                time.sleep(0.01)
                if(coordinates[0]>=400 or coordinates[0]<0):
                    xvelocity = -xvelocity
                self.canvas.move(self.enemy, xvelocity, yvelocity)
        

        def left(event):
            x = -10
            y = 0
            self.canvas.move(self.nave,x,y)
        def right(event):
            x = +10
            y = 0
            self.canvas.move(self.nave,x,y)
        def up(event):
            x = 0
            y = -10
            self.canvas.move(self.nave,x,y)
        def down(event):
            x = 0
            y = +10
            self.canvas.move(self.nave,x,y)
        window.bind("<Up>", up)
        window.bind("<Down>",down)
        window.bind("<Left>", left)
        window.bind("<Right>", right)
        window.mainloop()
        
    
    
            
       
        #Funcion para mover la nave
       

        
  
        
  
                
            

class Ventana3:

    def __init__(self):
        self.canvas = Canvas(window, width = 600, height = 800,
                             highlightthickness=0, relief='ridge')
        self.canvas.place(x=0,y=0)
        
        self.fondo = cargar_imagen("Fondo2.gif")
        self.label_fondo = Label(self.canvas, image = self.fondo)  #Se llama al fondo de la pantalla principal
        self.label_fondo.place(x=0,y=0, width=600, height=800)
   

        window.mainloop()
class Ventana4:

    def __init__(self):
        self.canvas = Canvas(window, width = 600, height = 800,
                             highlightthickness=0, relief='ridge')
        self.canvas.place(x=0,y=0)
        
        self.fondo = cargar_imagen("Fondo2.gif")
        self.label_fondo = Label(self.canvas, image = self.fondo)  #Se llama al fondo de la pantalla principal
        self.label_fondo.place(x=0,y=0, width=600, height=800)
 

        window.mainloop()

window = Tk()
ventana_principal = Ventana1(window)
window.title("Hello World")
window.minsize(600,800)
window.mainloop()
