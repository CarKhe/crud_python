from tkinter import *
class Ventana(Frame):
    def __init__(self,master=None):
        super().__init__(master,width=680,height=260)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def f_nuevo(self):
        pass
    
    def f_modificar(self):
        pass
    
    def f_eliminar(self):
        pass
    
    def create_widgets(self):
        frame1 = Frame(self,bg="#bfdaff")
        frame1.place(x=0,y=0,width=93,height=259)
        
        self.btn_nuevo = Button(frame1,text="nuevo",command=self.f_nuevo, bg="blue",fg="white")
        self.btn_nuevo.place(x=5,y=50,width=80,height=30)
        
        self.btn_modificar = Button(frame1,text="modificar",command=self.f_modificar, bg="blue",fg="white")
        self.btn_modificar.place(x=5,y=90,width=80,height=30)
        
        self.btn_eliminar = Button(frame1,text="eliminar",command=self.f_eliminar, bg="blue",fg="white")
        self.btn_eliminar.place(x=5,y=130,width=80,height=30)
        
        frame2 = Frame(self,bg="#d3dde3")
        frame2.place(x=95,y=0,width=150,height=259)
        
        lbl1 = Label(frame2,text="ISO 3: ")
        lbl1.place(x=3,y=5)
        self.txtISO3 = Entry(frame2)
        self.txtISO3.place(x=3,y=25,width=50,height=20)
