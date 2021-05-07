from tkinter import *

def inicio():

    #EVENTO PARA EL CLICK DE LOS BOTONES 
    def evento():           
        print("click de los botones")

    def evento2():      #EVENTO para el boton 2
        boton2["text"] = "X"

    #CREACION DE LA VENTANA DE TKINTER
    root = Tk()                         #OBJETO DE TIPO TK PARA ABRIR LA VENTANA

    root.title("Totito-Multijugador")   #TITULO DE LA VENTANA
    root.resizable(True,True)           #PARA REDIMENSIONAR LA VENTANA
    root.geometry("550x450")            #DIMENSIONES DE VENTANA
    root.config(bg="palegreen")         #CARACTERISTICAS DE VENTANA

    #CREACION DE OBJETOS DE TIPO LABEL PARA MOSTRAR TEXTO EN VENTANA
    label = Label(root, text="Totito-Multijugador", font=("Helvatica", 18), bg="palegreen").place(x=150, y=30)#OBJETO TIPO LABEL CON ATRIBUTOS PARA TEXTO, FUENTE, FONDO, FUNCION PLACE PARA LA ORIENTACION 
    label2 = Label(root, text="Jugador1", font=("Helvatica", 18), bg="palegreen").place(x=50, y=400)#OBJETO TIPO LABEL CON ATRIBUTOS PARA TEXTO, FUENTE, FONDO, FUNCION PLACE PARA LA ORIENTACION 
    label3 = Label(root, text="Jugador2", font=("Helvatica", 18), bg="palegreen").place(x=350, y=400)#OBJETO TIPO LABEL CON ATRIBUTOS PARA TEXTO, FUENTE, FONDO, FUNCION PLACE PARA LA ORIENTACION 
    
    #CREACION DE OBJETOS DE TIPO BUTTON PARA LA JUGABILIDAD 
    boton = Button(root, text="    ", font=("Helvatica", 18), background="gray", command= evento).place(x=150, y=150)#OBJETO TIPO BUTTON CON ATRIBUTOS PARA TEXTO, FUENTE, FONDO, Y EL EVENTO
    boton2 = Button(root, text="    ", font=("Helvatica", 18), background="gray", command=evento).place(x=230, y=150)#OBJETO TIPO BUTTON CON ATRIBUTOS PARA TEXTO, FUENTE, FONDO, Y EL EVENTO
    boton3 = Button(root, text="    ", font=("Helvatica", 18), background="gray", command= evento).place(x=310, y=150)#OBJETO TIPO BUTTON CON ATRIBUTOS PARA TEXTO, FUENTE, FONDO, Y EL EVENTO
    boton4 = Button(root, text="    ", font=("Helvatica", 18), background="gray", command= evento).place(x=150, y=240)
    boton5 = Button(root, text="    ", font=("Helvatica", 18), background="gray",  command= evento).place(x=230, y=240)
    boton6 = Button(root, text="    ", font=("Helvatica", 18), background="gray",  command= evento).place(x=310, y=240)
    boton7 = Button(root, text="    ", font=("Helvatica", 18), background="gray", command= evento).place(x=150, y=330)
    boton8 = Button(root, text="    ", font=("Helvatica", 18), background="gray", command= evento).place(x=230, y=330)
    boton9 = Button(root, text="    ", font=("Helvatica", 18), background="gray", command= evento2).place(x=310, y=330)
    
    root.mainloop()

if __name__=="__main__":
    inicio()                #CORRER EL PROGRAMA DESDE LA FUNCION INICIO