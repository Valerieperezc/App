from distutils.util import run_2to3
from doctest import master
import tkinter as tk
import os
from tkinter import Entry, StringVar, END, Listbox, Button, GROOVE
import webbrowser

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Maquillaje")
ventana.resizable(width=0, height=0)

seleccion = []

absolute_folder_path = os.path.dirname(os.path.realpath(__file__))


inicio = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/1.png'))
error = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/132.png'))
genero = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/2.png'))
tono = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/3.png'))
prototipo = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/4.png'))
evento = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/5.png'))
tipomujer = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/6.png'))
tipohombre = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/7.png'))
calorimetria = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/8.png'))
despedida = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/141.png'))
r1 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/9.png'))
r2 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/10.png'))
r3 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/11.png'))
r4 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/12.png'))
r5 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/13.png'))
r6 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/14.png'))
r7 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/15.png'))
r8 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/16.png'))
r9 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/17.png'))
r10 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/18.png'))
r11 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/19.png'))
r12 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/20.png'))
r13 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/21.png'))
r14 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/22.png'))
r15 =  tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/23.png'))
r16 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/24.png'))
r17 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/25.png'))
r18 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/26.png'))
r19 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/27.png'))
r20 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/28.png'))
r21 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/29.png'))
r22 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/30.png'))
r23 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/31.png'))
r24 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/32.png'))
r25 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/33.png'))
r26 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/34.png'))
r27 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/35.png'))
r28 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/36.png'))
r29 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/37.png'))
r30 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/38.png'))
r31 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/39.png'))
r32 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/40.png'))
r33 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/41.png'))
r34 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/42.png'))
r35 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/43.png'))
r36 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/44.png'))
r37 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/45.png'))
r38 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/46.png'))
r39 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/47.png'))
r40 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/48.png'))
r41 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/49.png'))
r42 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/50.png'))
r43 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/51.png'))
r44 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/52.png'))
r45 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/53.png'))
r46 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/54.png'))
r47 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/55.png'))
r48 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/56.png'))
r49 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/57.png'))
r50 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/58.png'))
r51 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/59.png'))
r52 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/60.png'))
r53 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/61.png'))
r54 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/62.png'))
r55 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/63.png'))
r56 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/64.png'))
r57 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/65.png'))
r58 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/66.png'))
r59 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/67.png'))
r60 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/68.png'))
r61 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/69.png'))
r62 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/70.png'))
r63 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/71.png'))
r64 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/72.png'))
r65 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/73.png'))
r66 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/74.png'))
r67 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/75.png'))
r68 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/76.png'))
r69 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/77.png'))
r70 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/78.png'))
r71 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/79.png'))
r72 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/80.png'))
r73 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/81.png'))
r74 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/82.png'))
r75 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/83.png'))
r76 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/84.png'))
r77 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/85.png'))
r78 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/86.png'))
r79 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/87.png'))
r80 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/88.png'))
r81 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/89.png'))
r82 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/90.png'))
r83 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/91.png'))
r84 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/92.png'))
r85 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/93.png'))
r86 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/94.png'))
r87 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/95.png'))
r88 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/96.png'))
r89 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/97.png'))
r90 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/98.png'))
r91 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/99.png'))
r92 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/100.png'))
r93 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/101.png'))
r94 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/102.png'))
r95 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/103.png'))
r96 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/104.png'))
r97 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/105.png'))
r98 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/106.png'))
r99 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/107.png'))



ingresar = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/boton de ingreso.png'))
siguiente1 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/botonsigui.png'))
anterior1 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/botonanteriobei.png'))
siguiente2 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/botonsiguibei.png'))
anterior2 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/flechaatraswhi.png'))
openlink= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/interrrogacion.png'))
anterior3= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/flechaatrasred.png'))
mujer= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/109.png'))
hombre = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/imagen108.png'))
piel1= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/110.png'))
piel2= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/111.png'))
piel3= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/112.png'))
piel4= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/113.png'))
piel5= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/114.png'))
piel6= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/115.png'))
dia= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/116.png'))
noche= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/117.png'))
tono1= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/126.png'))
tono2= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/127.png'))
tono3= tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/128.png'))
siguiente3 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/129.png'))
anterior3 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/130.png'))
ppiel1 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/134.png'))
ppiel2 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/135.png'))
ppiel3 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/136.png'))
ppiel4 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/137.png'))
ppiel5 = tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/138.png'))
tmmujer1 =tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/118.png'))
tmmujer2 =tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/119.png'))
tmmujer3 =tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/120.png'))
tmmujer4 =tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/121.png'))
tmhombre1 =tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/123.png'))
tmhombre2 =tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/124.png'))
tmhombre3 =tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/125.png'))
inicioboton =tk.PhotoImage(file=os.path.join(absolute_folder_path,'imagenes/131.png'))


def MainMenu():  # PRINCIPAL
    
    fondo = tk.Label(ventana, image=inicio).place(x=0, y=0)  # FRAME
    
    # CAMPO DE TEXTO PARA LOGUEARSE
    codigo = StringVar()
    campo = Entry(ventana, textvariable=codigo,
                  width=19, borderwidth=0, font=('Bahnschrift SemiBold SemiConden', 14)).place(x=260, y=355, height=30)
    # LEER TXT DE LOGUEO PARA STUDENT
    filename = ("codigos.txt")
    with open(filename) as file:
        lines = file.readlines()

    txtL = []
    for x in lines:
        txtL.append(x.rstrip())
    # print (txtL) # lista con los códigos estudiantiles

    # VALIDAR QUE LOS CAMPOS NO ESTÉN VACIOS, SI LO ESTAN SALDRÁ UNA ADVERTENCIA

    def login():
        code = codigo.get()
        if(code == ""):  # Campos vacios
            Error = tk.Label(ventana, image=error, borderwidth=0, width=200)
            Error.place(x=240, y=450, height=36)

        else:  # sino esta vacio
            # Buscar en el txt que ese código sea de la universidad del Norte
            if code in txtL:
                Genero()  # Si el código se encuentra que pase a la siguiente
            else:
                Error = tk.Label(ventana, image=error,
                                 borderwidth=0, width=194)
                # sino, el sale una advertencia
                Error.place(x=240, y=450, height=26)
    
    # BOTON LOGIN
    boton1 = tk.Button(ventana, image= ingresar, command=login, width=120, borderwidth=0, cursor="circle")
    boton1.place(x=280, y=400, height=50)

def llenarsel(pos,sel):
        seleccion.insert(pos,sel)
       

def Genero():

    fondo = tk.Label(ventana, image=genero).place(x=0, y=0)  # FRAME
    boton1 = tk.Button(ventana,image=siguiente1, command=TonoPiel, width=200, borderwidth=0, cursor="circle",text="Siguiente")
    boton1.place(x=140, y=372, height=78)
    hombrebot = tk.Button(ventana,image=hombre, command=lambda:[llenarsel(0,1),TipoMaquillajeHombre()],  width=130, borderwidth=0, cursor="circle",text="Siguiente")
    hombrebot.place(x=52, y=180, height=130)
    mujerbot = tk.Button(ventana,image=mujer, command=lambda:[TipoMaquillajeMujer(),llenarsel(0,2)], width=130, borderwidth=0, cursor="circle",text="Siguiente")
    mujerbot.place(x=300, y=180, height=130)
    

def TonoPiel():
    
    fondo = tk.Label(ventana, image=tono).place(x=0, y=0)  # FRAME
    boton1 = tk.Button(ventana,image=siguiente2, command=PrototipoPiel, width=150, borderwidth=0, cursor="circle",text="Siguiente")
    boton1.place(x=340, y=460, height=44)
    boton2 = tk.Button(ventana,image=anterior1, command=Genero, width=150, borderwidth=0, cursor="circle")
    boton2.place(x=0, y=460, height=42)
    pielt1 = tk.Button(ventana,image=piel1, command=lambda:[PrototipoPiel(),llenarsel(1,1)], width=150, borderwidth=0, cursor="circle")
    pielt1.place(x=0, y=100, height=150)
    pielt2 = tk.Button(ventana,image=piel2, command=lambda:[PrototipoPiel(),llenarsel(1,2)], width=150, borderwidth=0, cursor="circle")
    pielt2.place(x=174, y=100, height=150)
    pielt3 = tk.Button(ventana,image=piel3, command=lambda:[PrototipoPiel(),llenarsel(1,3)], width=150, borderwidth=0, cursor="circle")
    pielt3.place(x=350, y=100, height=150)
    pielt4 = tk.Button(ventana,image=piel4, command=lambda:[PrototipoPiel(),llenarsel(1,4)], width=150, borderwidth=0, cursor="circle")
    pielt4.place(x=0, y=320, height=134)
    pielt5 = tk.Button(ventana,image=piel5, command=lambda:[PrototipoPiel(),llenarsel(1,5)], width=150, borderwidth=0, cursor="circle")
    pielt5.place(x=174, y=320, height=134)
    pielt6 = tk.Button(ventana,image=piel6, command=lambda:[PrototipoPiel(),llenarsel(1,6)], width=150, borderwidth=0, cursor="circle")
    pielt6.place(x=350, y=320, height=134)

def PrototipoPiel():
    
    fondo = tk.Label(ventana, image=prototipo).place(x=0, y=0)  # FRAME
    boton1 = tk.Button(ventana,image=siguiente1, command=Evento, width=240, borderwidth=0, cursor="circle",text="Siguiente")
    boton1.place(x=128, y=454, height=50)

    url = "https://www.hogarmania.com/belleza/estetica/rostro/cual-tipo-piel-5811.html"
    def openweb():
        webbrowser.open(url)

    boton2 = tk.Button(ventana,image=openlink, command=openweb, width=92, borderwidth=0, cursor="circle",text="img")
    boton2.place(x=400, y=450, height=46)

    boton3 = tk.Button(ventana,image=anterior2, command=TonoPiel, width=88, borderwidth=0, cursor="circle",text="anterior")
    boton3.place(x=0, y=448, height=46)

    pielp1 = tk.Button(ventana,image=ppiel1, command=lambda:[Evento(),llenarsel(2,1)], width=150, borderwidth=0, cursor="circle",text="anterior")
    pielp1.place(x=170, y=80, height=170)
    pielp2 = tk.Button(ventana,image=ppiel2, command=lambda:[Evento(),llenarsel(2,2)], width=150, borderwidth=0, cursor="circle",text="anterior")
    pielp2.place(x=350, y=80, height=170)
    pielp3 = tk.Button(ventana,image=ppiel3, command=lambda:[Evento(),llenarsel(2,3)], width=146, borderwidth=0, cursor="circle",text="anterior")
    pielp3.place(x=0, y=270, height=170)
    pielp4 = tk.Button(ventana,image=ppiel4, command=lambda:[Evento(),llenarsel(2,4)], width=150, borderwidth=0, cursor="circle",text="anterior")
    pielp4.place(x=170, y=270, height=170)
    pielp5 = tk.Button(ventana,image=ppiel5, command=lambda:[Evento(),llenarsel(2,5)], width=150, borderwidth=0, cursor="circle",text="anterior")
    pielp5.place(x=350, y=270, height=170)

    
    

def Evento():
    
    fondo = tk.Label(ventana, image=evento).place(x=0, y=0)  # FRAME
    boton1 = tk.Button(ventana,image=siguiente1, command=Calorimetria, width=180, borderwidth=0, cursor="circle",text="Siguiente")
    boton1.place(x=300, y=396, height=50)

    boton2 = tk.Button(ventana,image=anterior1, command=PrototipoPiel, width=150, borderwidth=0, cursor="circle",text="Anterior")
    boton2.place(x=10, y=400, height=42)
    edia = tk.Button(ventana,image=dia, command=Calorimetria, width=150, borderwidth=0, cursor="circle",text="Anterior")
    edia.place(x=50, y=180, height=150)
    enoche = tk.Button(ventana,image=noche, command=Calorimetria, width=150, borderwidth=0, cursor="circle",text="Anterior")
    enoche.place(x=280, y=180, height=150)


def TipoMaquillajeMujer():
    
    fondo = tk.Label(ventana, image=tipomujer).place(x=0, y=0)  # FRAME
    boton1 = tk.Button(ventana,image=siguiente1, command=TonoPiel, width=150, borderwidth=0, cursor="circle",text="Siguiente")
    boton1.place(x=348, y=460, height=44)
    boton2 = tk.Button(ventana,image=anterior3, command=Genero, width=62, borderwidth=0, cursor="circle",text="Anterior")
    boton2.place(x=0, y=454, height=44)
    mujertm1 = tk.Button(ventana,image=tmmujer1, command=lambda:[TonoPiel(),llenarsel(3,1)], width=140, borderwidth=0, cursor="circle",text="Anterior")
    mujertm1.place(x=80, y=118, height=140)
    mujertm2 = tk.Button(ventana,image=tmmujer2, command=lambda:[TonoPiel(),llenarsel(3,2)], width=140, borderwidth=0, cursor="circle",text="Anterior")
    mujertm2.place(x=300, y=110, height=140)
    mujertm3 = tk.Button(ventana,image=tmmujer3, command=lambda:[TonoPiel(),llenarsel(3,3)], width=140, borderwidth=0, cursor="circle",text="Anterior")
    mujertm3.place(x=86, y=306, height=140)
    mujertm4 = tk.Button(ventana,image=tmmujer4, command=lambda:[TonoPiel(),llenarsel(3,4)], width=140, borderwidth=0, cursor="circle",text="Anterior")
    mujertm4.place(x=300, y=304, height=140)

def TipoMaquillajeHombre():
    
    fondo = tk.Label(ventana, image=tipohombre).place(x=0, y=0)  # FRAME
    boton1 = tk.Button(ventana,image=siguiente1, command=TonoPiel, width=150, borderwidth=0, cursor="circle",text="Siguiente")
    boton1.place(x=348, y=460, height=44)
    boton2 = tk.Button(ventana,image=anterior3, command=Genero, width=62, borderwidth=0, cursor="circle",text="Anterior")
    boton2.place(x=0, y=454, height=44)
    hombretm1 = tk.Button(ventana,image=tmhombre1, command=lambda:[TonoPiel(),llenarsel(3,1)], width=140, borderwidth=0, cursor="circle",text="Anterior")
    hombretm1.place(x=190, y=100, height=140)
    hombretm2 = tk.Button(ventana,image=tmhombre2, command=lambda:[TonoPiel(),llenarsel(3,3)], width=140, borderwidth=0, cursor="circle",text="Anterior")
    hombretm2.place(x=86, y=306, height=140)
    hombretm3 = tk.Button(ventana,image=tmhombre3, command=lambda:[TonoPiel(),llenarsel(3,4)], width=140, borderwidth=0, cursor="circle",text="Anterior")
    hombretm3.place(x=320, y=306, height=140)
    

def Calorimetria():
    
    fondo = tk.Label(ventana, image=calorimetria).place(x=0, y=0)  # FRAME
    boton1 = tk.Button(ventana,image=siguiente3, command=final, width=120, borderwidth=0, cursor="circle",text="Siguiente")
    boton1.place(x=380, y=454, height=50)
    boton2 = tk.Button(ventana,image=anterior3, command=Evento, width=70, borderwidth=0, cursor="circle",text="Anterior")
    boton2.place(x=30, y=440, height=60)
    tononeu = tk.Button(ventana,image=tono1, command=recomendacion, width=140, borderwidth=0, cursor="circle",text="Anterior")
    tononeu.place(x=0, y=50, height=130)
    tonofrio = tk.Button(ventana,image=tono2, command=recomendacion, width=140, borderwidth=0, cursor="circle",text="Anterior")
    tonofrio.place(x=180, y=50, height=130)
    tonocal = tk.Button(ventana,image=tono3, command=recomendacion, width=140, borderwidth=0, cursor="circle",text="Anterior")
    tonocal.place(x=370, y=50, height=130)

def recomendacion():
    if (seleccion[1]==1 and seleccion[2]==5 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r1).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==4 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r2).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==3 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r3).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==2 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r4).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==1 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r5).place(x=0, y=0)
    
    if (seleccion[1]==1 and seleccion[2]==1 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r6).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==2 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r7).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==3 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r8).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==4 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r9).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==5 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r10).place(x=0, y=0)
    
    if (seleccion[1]==5 and seleccion[2]==1 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r11).place(x=0, y=0)
    if (seleccion[1]==5 and seleccion[2]==2 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r12).place(x=0, y=0)
    if (seleccion[1]==5 and seleccion[2]==3 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r13).place(x=0, y=0)
    if (seleccion[1]==5 and seleccion[2]==4 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r14).place(x=0, y=0)
    if (seleccion[1]==5 and seleccion[2]==5 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r15).place(x=0, y=0)
    
    if (seleccion[1]==6 and seleccion[2]==1 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r16).place(x=0, y=0)
    if (seleccion[1]==6 and seleccion[2]==2 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r17).place(x=0, y=0)
    if (seleccion[1]==6 and seleccion[2]==3 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r18).place(x=0, y=0)
    if (seleccion[1]==6 and seleccion[2]==4 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r19).place(x=0, y=0)
    if (seleccion[1]==6 and seleccion[2]==5 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r20).place(x=0, y=0)
    
    if (seleccion[1]==2 and seleccion[2]==1 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r21).place(x=0, y=0)
    if (seleccion[1]==2 and seleccion[2]==2 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r22).place(x=0, y=0)
    if (seleccion[1]==2 and seleccion[2]==3 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r23).place(x=0, y=0)
    if (seleccion[1]==2 and seleccion[2]==4 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r24).place(x=0, y=0)
    if (seleccion[1]==2 and seleccion[2]==5 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r25).place(x=0, y=0)
    
    if (seleccion[1]==3 and seleccion[2]==1 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r26).place(x=0, y=0)
    if (seleccion[1]==3 and seleccion[2]==2 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r27).place(x=0, y=0)
    if (seleccion[1]==3 and seleccion[2]==3 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r28).place(x=0, y=0)
    if (seleccion[1]==3 and seleccion[2]==4 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r29).place(x=0, y=0)
    if (seleccion[1]==3 and seleccion[2]==5 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r30).place(x=0, y=0)

    if (seleccion[1]==4 and seleccion[2]==1 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r31).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==2 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r32).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==3 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r33).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==4 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r34).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==5 and seleccion[3]==3  ):
        fondo = tk.Label(ventana, image=r35).place(x=0, y=0)

    if (seleccion[1]==1 and seleccion[2]==1 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r36).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==2 and seleccion[3]==4 ):
        fondo = tk.Label(ventana, image=r37).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==3 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r38).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==4 and seleccion[3]==4 ):
        fondo = tk.Label(ventana, image=r39).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==5 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r40).place(x=0, y=0)

    if (seleccion[1]==4 and seleccion[2]==1 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r41).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==2 and seleccion[3]==4 ):
        fondo = tk.Label(ventana, image=r42).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==3 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r43).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==4 and seleccion[3]==4 ):
        fondo = tk.Label(ventana, image=r44).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==5 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r45).place(x=0, y=0)

    if (seleccion[1]==6 and seleccion[2]==1 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r46).place(x=0, y=0)
    if (seleccion[1]==6 and seleccion[2]==2 and seleccion[3]==4 ):
        fondo = tk.Label(ventana, image=r47).place(x=0, y=0)
    if (seleccion[1]==6 and seleccion[2]==3 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r48).place(x=0, y=0)
    if (seleccion[1]==6 and seleccion[2]==4 and seleccion[3]==4 ):
        fondo = tk.Label(ventana, image=r49).place(x=0, y=0)
    if (seleccion[1]==6 and seleccion[2]==5 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r50).place(x=0, y=0)
    
    if (seleccion[1]==2 and seleccion[2]==1 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r51).place(x=0, y=0)
    if (seleccion[1]==2 and seleccion[2]==2 and seleccion[3]==4 ):
        fondo = tk.Label(ventana, image=r52).place(x=0, y=0)
    if (seleccion[1]==2 and seleccion[2]==3 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r53).place(x=0, y=0)
    if (seleccion[1]==2 and seleccion[2]==4 and seleccion[3]==4 ):
        fondo = tk.Label(ventana, image=r54).place(x=0, y=0)
    if (seleccion[1]==2 and seleccion[2]==5 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r55).place(x=0, y=0)

    if (seleccion[1]==3 and seleccion[2]==1 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r56).place(x=0, y=0)
    if (seleccion[1]==3 and seleccion[2]==2 and seleccion[3]==4 ):
        fondo = tk.Label(ventana, image=r57).place(x=0, y=0)
    if (seleccion[1]==3 and seleccion[2]==3 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r58).place(x=0, y=0)
    if (seleccion[1]==3 and seleccion[2]==4 and seleccion[3]==4 ):
        fondo = tk.Label(ventana, image=r59).place(x=0, y=0)
    if (seleccion[1]==3 and seleccion[2]==5 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r60).place(x=0, y=0)

    if (seleccion[1]==4 and seleccion[2]==1 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r61).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==2 and seleccion[3]==4 ):
        fondo = tk.Label(ventana, image=r62).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==3 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r63).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==4 and seleccion[3]==4 ):
        fondo = tk.Label(ventana, image=r64).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==5 and seleccion[3]==4  ):
        fondo = tk.Label(ventana, image=r65).place(x=0, y=0)
    
    if (seleccion[1]==5 and seleccion[2]==1 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r71).place(x=0, y=0)
    if (seleccion[1]==5 and seleccion[2]==2 and seleccion[3]==1 ):
        fondo = tk.Label(ventana, image=r72).place(x=0, y=0)
    if (seleccion[1]==5 and seleccion[2]==3 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r73).place(x=0, y=0)
    if (seleccion[1]==5 and seleccion[2]==4 and seleccion[3]==1 ):
        fondo = tk.Label(ventana, image=r74).place(x=0, y=0)
    if (seleccion[1]==5 and seleccion[2]==5 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r75).place(x=0, y=0)
    
    if (seleccion[1]==6 and seleccion[2]==1 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r76).place(x=0, y=0)
    if (seleccion[1]==6 and seleccion[2]==2 and seleccion[3]==1 ):
        fondo = tk.Label(ventana, image=r77).place(x=0, y=0)
    if (seleccion[1]==6 and seleccion[2]==3 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r78).place(x=0, y=0)
    if (seleccion[1]==6 and seleccion[2]==4 and seleccion[3]==1 ):
        fondo = tk.Label(ventana, image=r79).place(x=0, y=0)
    if (seleccion[1]==6 and seleccion[2]==5 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r80).place(x=0, y=0)

    if (seleccion[1]==2 and seleccion[2]==1 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r81).place(x=0, y=0)
    if (seleccion[1]==2 and seleccion[2]==2 and seleccion[3]==1 ):
        fondo = tk.Label(ventana, image=r82).place(x=0, y=0)
    if (seleccion[1]==2 and seleccion[2]==3 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r83).place(x=0, y=0)
    if (seleccion[1]==2 and seleccion[2]==4 and seleccion[3]==1 ):
        fondo = tk.Label(ventana, image=r84).place(x=0, y=0)
    if (seleccion[1]==2 and seleccion[2]==5 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r85).place(x=0, y=0)

    if (seleccion[1]==3 and seleccion[2]==1 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r86).place(x=0, y=0)
    if (seleccion[1]==3 and seleccion[2]==2 and seleccion[3]==1 ):
        fondo = tk.Label(ventana, image=r87).place(x=0, y=0)
    if (seleccion[1]==3 and seleccion[2]==3 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r88).place(x=0, y=0)
    if (seleccion[1]==3 and seleccion[2]==4 and seleccion[3]==1 ):
        fondo = tk.Label(ventana, image=r89).place(x=0, y=0)
    if (seleccion[1]==3 and seleccion[2]==5 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r90).place(x=0, y=0)

    if (seleccion[1]==4 and seleccion[2]==1 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r91).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==2 and seleccion[3]==1 ):
        fondo = tk.Label(ventana, image=r92).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==3 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r93).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==4 and seleccion[3]==1 ):
        fondo = tk.Label(ventana, image=r94).place(x=0, y=0)
    if (seleccion[1]==4 and seleccion[2]==5 and seleccion[3]==1  ):
        fondo = tk.Label(ventana, image=r95).place(x=0, y=0)

    if (seleccion[1]==1 and seleccion[2]==1 and seleccion[3]==2  ):
        fondo = tk.Label(ventana, image=r96).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==2 and seleccion[3]==2 ):
        fondo = tk.Label(ventana, image=r97).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==3 and seleccion[3]==2  ):
        fondo = tk.Label(ventana, image=r98).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==4 and seleccion[3]==2 ):
        fondo = tk.Label(ventana, image=r99).place(x=0, y=0)
    if (seleccion[1]==1 and seleccion[2]==5 and seleccion[3]==2  ):
        fondo = tk.Label(ventana, image=r99).place(x=0, y=0)
    
      
    boton = tk.Button(ventana,image=siguiente1, command=final, width=240, borderwidth=0, cursor="circle",text="Anterior")
    boton.place(x=100, y=440, height=60)

def final ():
    fondo = tk.Label(ventana, image=despedida).place(x=0, y=0)
    boton = tk.Button(ventana,image=inicioboton, command=MainMenu, width=240, borderwidth=0, cursor="circle",text="Anterior")
    boton.place(x=125, y=432, height=60)
    


MainMenu()
ventana.mainloop()