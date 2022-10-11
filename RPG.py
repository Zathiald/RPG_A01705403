"""
Proyecto RPG
Role Playing Game(RPG)
El programa le da al usuario multiples opciones de movimiento,
combate e inventario, para que sienta que esta en una aventura. 
"""

"""Importar la libreria de tiempo para usar la función de sleep"""
from time import sleep 

"""Importar la librería de sys, donde usaremos la función de flush"""
import sys 

"""Importamos la función para poder generar un número random
Metodo para generar un numero random obtenido de https://j2logo.com/python/generar-numeros-aleatorios-en-python/"""
import random 

#--------------------------------------------FUNCIÓN PARA TEXTO--------------------------------------------------------------------------------------------------
"""Metodo para hacer aparecer el texto lentamente obtenido de https://es.stackoverflow.com/questions/25901/como-imprimir-una-cadena-de-texto-con-pausas-entre-cada-letra-impresa-en-python"""
def text(texto,speed):
    """
    (uso de biblioteca, uso de funciones)
    recibe: string de texto,velocidad de texto
    imprime cada letra segun la velocidad
    devuelve: texto impreso según la velocidad
    """
    for c in texto: 
        print(c,end='') 
        sys.stdout.flush() 
        sleep(speed) 

"""Valores para colores obtenidos de https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal"""
class color: 
    PURPLE = '\033[95m' 
    CYAN = '\033[96m' 
    DARKCYAN = '\033[36m' 
    BLUE = '\033[94m' 
    GREEN = '\033[92m' 
    YELLOW = '\033[93m' 
    RED = '\033[91m' 
    BOLD = '\033[1m' 
    UNDERLINE = '\033[4m' 
    END = '\033[0m'   
"""------------------------------------------GUARDAR Y CREAR VARIABLES-----------------------------------------------------------------------------------------------------------------------------------"""   

"""---Inventario"""
anillos=[]
medallons=[] 
cascos=[] 
espadas=[]
manzanas=[]
botas=[]
martillos=[]
brazaletes=[]
super_pocions=[]
pocions=[] 
peluches=[]
sombreros=[] 
aks=[]
granadas=[]
cangureras=[]
afros=[]
rayos=[]
invent=[anillos,medallons,cascos,espadas,manzanas,botas,martillos,brazaletes,super_pocions,pocions,peluches,sombreros,aks,granadas,cangureras,afros,rayos]


"""---Stats"""
vida= float
velocidad = float
fuerza = float 
nivel = float
exp = float 
dinero = float 
co_x=float
co_y=float
vida= 5.0 
velocidad = 4.0 
fuerza = 3.5 
nivel = 2.0 
exp = 0.0 
dinero = 100.0 
co_x=0.0
co_y=0.0 
stat=[vida,velocidad,fuerza,nivel,exp,dinero,co_x,co_y]  

"""---Stats enemigos"""
name_enem= str
fuerza_enem = float 
velocidad_enem = float
vida_enem = float
exp_enem = float
dinero_enem = float 
enem_stats=[name_enem,fuerza_enem,velocidad_enem,vida_enem,exp_enem,dinero_enem]
   
def stats(): 
    """
    (uso de variables, uso de funciones)
    recibe: valor de nombre,vida,velocidad,fuerza,nivel,exp,dinero
    imprime cada variable
    devuelve: texto impreso de cada variable
    """
    name_text=("Nombre: ",name,'\n')
    text(name_text,0.5)

    vida_text=("Vida: ",vida,'\n') 
    text(vida_text,0.5)

    velocidad_text=("Velocidad: ",velocidad,'\n')
    text(velocidad_text,0.5)

    fuerza_text=("Fuerza: ",fuerza,'\n') 
    text(fuerza_text,0.5)
    
    nivel_text=("Nivel: ",nivel,'\n') 
    text(nivel_text,0.5)

    exp_text=("Exp: ",exp,'\n') 
    text(exp_text,0.5)
    
    dinero_text=("Dinero: ",dinero,'\n') 
    text(dinero_text,0.5)
    
    coord_text=("Coordenadas: ",co_x,",",co_y,'\n') 
    text(coord_text,0.5)
 
def tut():
    """
    (uso de funciones,uso de texto)
    recibe: nada
    devuelve: texto impreso de tutorial
    Se guarda en función para hacer el tutorial opcional
    """
    text_intro=("Bienvenido al Mundo de Palgia, un lugar lleno de misterios y peligros, aventuras y amenazas\n")
    text(text_intro,0.03)

    text9=("Estos son tus stats iniciales\n") 
    text(text9,0.03)
        
    stats() 

    text10=("Si en algún momento quieres ver tus stats presiona S al inicio de cada turno\n") 
    text(text10,0.03)

    text11=("Para moverte presiona las teclas W,A,S,D y te moveras en esa dirección\n")
    text(text11,0.03)

    text12=("Según tu velocidad es cuantos cuadros podras moverte por turno y también cuanta chance tienes para atacar a tu enemigo\n") 
    text(text12,0.03)

    text13=("Mientras más velocidad más chance de atacar\n")
    text(text13,0.03)

    text14=("Para escoger moverte al inicio de cada turno presiona M\n") 
    text(text14,0.03)

    text15=("Al escoger la opción de moverte, hay una posibilidad de que aparezca un enemigo, pueblo u objeto en tu camino\n") 
    text(text15,0.03)

    text16=("Por toda Palgia hay varios objetos místicos, usalos con sabiduría para obtener ventaja en combate\n") 
    text(text16,0.03)

    text17=("Pero cuidado, que algunos objetos estan embrujados y te podrían bajar los stats\n") 
    text(text17,0.03)

    text18=("Para ver y escoger un objeto al inicio de cada turno presiona I\n") 
    text(text18,0.03)

    text19=("Ahora que estas familiarizado con las acciones básicas\n") 
    text(text19,0.03)

#--------------------------------------------INGRESO JUGADOR--------------------------------------------------------------------------------------------------
text1 = ("Como te llamas héroe o heroína: ") 
text(text1,0.03)

name=str(input())

text2=("Bienvenid@ ",str(name),'\n')
text(text2,0.5)

text3=("Estas a punto de embarcarte en una aventura\n") 
text(text3,0.03)

text4=("¿Estás listo?\n") 
text(text4,0.03)

print("Y-si") 
print("N-no")
opcion=str(input())
while opcion!="Y" and opcion!="y" and opcion!="N" and opcion!="n": 
    text7=("Escoge bien\n") 
    text(text7,0.05)
    opcion=str(input())
if opcion == "y" or opcion == "Y": 
    text5=("Muy bien,¡COMENCEMOS!\n") 
    text(text5,0.05)
elif opcion == "n" or opcion == "N": 
    text6=("Vaya,pues ni modo,¡HORA DE EXPLORAR!\n") 
    text(text6,0.05)

text_tu=("Pero antes, quieres ver el tutorial?\n")
text(text_tu,0.03)
print("Y-si") 
print("N-no")
op_tu=str(input())
while op_tu!="Y" and op_tu!="y" and op_tu!="N" and op_tu!="n": 
    text7=("Escoge bien\n") 
    text(text7,0.05)
    op_tu=str(input())
if op_tu == "y" or op_tu == "Y": 
    text5=("Okey, vamos al tutorial\n") 
    text(text5,0.05)
    tut() 
elif op_tu == "n" or op_tu == "N": 
    text6=("Ah un aventurero,¡HORA DE AVENTURA!(TM)\n") 
    text(text6,0.05)
    text_intro=("Bienvenido al Mundo de Palgia, un lugar lleno de misterios y peligros, aventuras y amenazas\n")
    text(text_intro,0.03)

#---------------------------------------FUNCIONES PRINCIPALES-----------------------------------------------------------------------------------------------------
"""
    (uso de variables, uso de funciones,uso de texto)
    recibe: valor de nombre,vida,velocidad,fuerza,nivel,exp,dinero del enemigo
    le asigna cada variable a la funcion de enem
    devuelve: funcion de enemigo con variables diferentes
    Se repite la función con cada enemigo,esto para diferenciarlos
    Para los jefes se pone texto especial antes de llamar a la función
    """
def infernosnare(): 
    text_infernosnare=("Una bestia del mismisimo infierno!!!!\n")
    text(text_infernosnare,0.03)
    enem("Infernosnare",20,23,25,15,20)

def acidtaur(): 
    enem("Acidtaur",8,7.5,10,7,8.5)

def netherling(): 
    enem("Netherling",7.5,7,9.5,6.5,8)

def slagbrood(): 
    enem("Slagbrood",7,6.5,9.5,6,7.5)

def shadowling(): 
    text_shadowling=("Una bestia oscura se ha levantado desde las sombras, y viene por ti\n")
    text(text_shadowling,0.03)
    enem("Shadowling",15,17,20,10,15)

def chaosseker(): 
    enem("Chaosseker",6.5,6,9,5.5,7)

def slagghoul(): 
    enem("Slagghoul",5,5.5,8.5,5,6.5)

def gallmorph(): 
    enem("Galmorph",4.5,5.5,8,4.5,6)

def nightmask(): 
    text_nightmask=("Un caballero...pero algo no esta bien con el\n")
    text(text_nightmask,0.03)
    enem("Uraelth",10,8,15,7,10)

def dreadbug(): 
    enem("Dreadbug",4.5,5,7.5,4,5.5)

def warpfiend():
    enem("Warpfiend",4,7,6.5,3.5,5)

def sorrowvine(): 
    enem("Sorrowvine",3.5,3.5,6.5,3,4.5)

def uraelth(): 
    text_uraelth=("Parece ser que te has topado con un dragón, y este tiene hambre de aventurer@\n")
    text(text_uraelth,0.03)
    enem("Uraelth",5.5,7,10,5,5)

def baqus():
    enem("Baqus",3.5,3,6,2.5,4)

def bokoblin():
    enem("Bokoblin",2,2.5,5.5,2,3.5)

def diriol():
    enem("Diriol",1,2,5,1,2)

def subir_nivel():
    """
    (uso de variables, uso de funciones, uso de condiciones)
    recibe: valor de vida,velocidad,fuerza,nivel,exp
    segun el nivel y experiencia se sube el nivel
    segun el nivel que se sube, se sube tambien la vida,nivel,velocidad y fuerza
    devuelve: funcion de enemigo con variables diferentes
    """
    global vida 
    global velocidad
    global fuerza
    global nivel
    global exp
    if nivel==1 and exp>=10: 
        nivel=nivel+1 
        vida=vida+10 
        velocidad=velocidad+7 
        fuerza=fuerza+5
        text_subir=(color.BOLD,"¡Has subido de nivel! ¡FELICIDADES!, pero cuidado, ahora habra enemigos más poderosos\n",color.BOLD,color.END) 
        text(text_subir,0.05)
    if nivel==2 and exp>=25:
        nivel=nivel+1
        vida=vida+20
        velocidad=velocidad + 10
        fuerza=fuerza + 10
        text_subir=(color.BOLD,"¡Has subido de nivel! ¡FELICIDADES!, pero cuidado, ahora habra enemigos más poderosos\n",color.BOLD,color.END) 
        text(text_subir,0.05)
    if nivel==3 and exp>=50:
        nivel=nivel+1
        vida=vida+30
        velocidad=velocidad + 15
        fuerza=fuerza + 15
        text_subir=(color.BOLD,"¡Has subido de nivel! ¡FELICIDADES!, pero cuidado, ahora habra enemigos más poderosos\n",color.BOLD,color.END) 
        text(text_subir,0.05)

def enem(name_enem,fuerza_enem,velocidad_enem,vida_enem,exp_enem,dinero_enem): 
    """
    (uso de variables, uso de funciones,uso de ciclos,uso de condicionesmuso de input)
    recibe: valor de nombre,vida,velocidad,fuerza,nivel,exp,dinero del enemigo y del usuario
    imprime cada uno de los stats del enemigo
    le pide al usuario escoger entre atacar y ver el inventario 
    actualiza los stats del enemigo y del usuario dependiendo de las acciones tomadas
    devuelve: nuevos stats del usuario
    """
    global vida 
    global velocidad
    global fuerza
    global nivel
    global exp
    global dinero
    text_enem=("Los stats de este enemigo son: \n") 
    text(text_enem,0.05)

    nom_enem_t=("Nombre: ",name_enem,'\n')
    text(nom_enem_t,0.5)

    velocidad_enem_t=("Velocidad: ",velocidad_enem,'\n')
    text(velocidad_enem_t,0.5)

    fuerza_enem_t=("Fuerza: ",fuerza_enem,'\n') 
    text(fuerza_enem_t,0.5)
    
    vida_enem_t=("Vida: ",vida_enem,'\n') 
    text(vida_enem_t,0.5)

    while vida_enem>0:
        text_atac=("Presiona X para atacar \n") 
        text(text_atac,0.05)
        text_atac=("Presiona I para abrir inventario \n") 
        text(text_atac,0.05)
        atac=str(input()) 
        if atac=="I" or atac=="i":
            inv()
            text_atac=("Presiona X para atacar \n") 
            text(text_atac,0.05)
            text_atac=("Presiona I para abrir inventario \n") 
            text(text_atac,0.05)
            atac=str(input()) 
        if atac=="X" or atac=="x":
            if velocidad<velocidad_enem:
                atak=random.randint(0,1) 
                if atak==0:
                    enem_ataque(fuerza_enem)
                    text_atac=("Presiona X para atacar \n") 
                    text(text_atac,0.05)
                    text_atac=("Presiona I para abrir inventario \n") 
                    text(text_atac,0.05)
                    atac=str(input())

                if atak==1: 
                    vida_enem=vida_enem-fuerza 
                    text_atacar=("¡Has atacado al enemigo!\n") 
                    text(text_atacar,0.05)
                    text_vida_e=("Su vida ahora es ",vida_enem,'\n') 
                    text(text_vida_e,0.05)

                    if vida_enem==0 or vida_enem<0: 
                        text_win=(color.BOLD,color.BLUE,"¡LO LOGRASTE!\n",color.BOLD,color.BLUE,color.END) 
                        text(text_win,0.05)
                        exp_=exp+exp_enem
                        exp=exp_ 
                        dinero_=dinero+dinero_enem
                        dinero=dinero_
                        stats()
                        if nivel==1 and exp>=7: 
                            subir_nivel()
                        elif nivel==2 and exp>=25:
                            subir_nivel()
                        elif nivel==3 and exp>=50:
                            subir_nivel()
                        
            elif velocidad>velocidad_enem or velocidad==velocidad_enem: 
                atak=random.randint(0,3) 

                if atak==0: 
                    enem_ataque(fuerza_enem)
                    text_atac=("Presiona X para atacar \n") 
                    text(text_atac,0.05)
                    text_atac=("Presiona I para abrir inventario \n") 
                    text(text_atac,0.05)
                    atac=str(input())
        
                if atak==1 or 2 or 3: 
                    vida_enem=vida_enem-fuerza 

                    text_atacar=("¡Has atacado al enemigo!\n") 
                    text(text_atacar,0.05)

                    text_vida_e=("Su vida ahora es ",vida_enem,'\n') 
                    text(text_vida_e,0.05)

                    if vida_enem==0 or vida_enem<0: 
                        text_win=(color.BOLD,color.BLUE,"¡LO LOGRASTE!\n",color.BOLD,color.BLUE,color.END)
                        text(text_win,0.05)
                        exp=exp+exp_enem 
                        dinero=dinero+dinero_enem
                        stats()
                        if nivel==1 and exp>=7: 
                            subir_nivel()
                        elif nivel==2 and exp>=25:
                            subir_nivel()
                        elif nivel==3 and exp>=50:
                            subir_nivel(nivel,vida,velocidad,fuerza)

        else: 
            vida=vida-fuerza_enem 
            text_atacado=(color.BOLD,"¡NO ATACASTE!",color.BOLD,color.END,"Ahora el enemigo te ha atacado\n")
            text(text_atacado,0.05)

            text_vida_u=("Tu vida ahora es ",vida,'\n') 
            text(text_vida_u,0.05)
                
            if vida==0 or vida<0: 
                text_lose=(color.BOLD,color.RED,"¡GAME OVER!\n",color.BOLD,color.RED,color.END) 
                text(text_lose,1.0)
                exit()
                    
def enem_ataque(fuerza_enem):
    """
    (uso de variables, uso de funciones,uso de condicionales)
    recibe: valor de fuerza del enemigo y vida del usuario
    le quita a la vida del usuario el valor de la fuerza del enemigo
    analiza cuanta vida le queda al usuario
    devuelve: 
    si al usuario le queda vida, regresa a la función de atacar al enemigo
    si al usuario se le acaba la vida, se le muestra un mensaje de game over y se acaba el código
    """
    global vida
    vida=vida-fuerza_enem
    text_atacado=("¡FALLASTE!. Ahora el enemigo te ha atacado\n") 
    text(text_atacado,0.05)

    text_vida_u=("Tu vida ahora es ",vida,'\n') 
    text(text_vida_u,0.05)
                
    if vida>0: 
        return

    if vida==0 or vida<0: 
        text_lose=(color.BOLD,color.RED,"¡GAME OVER!\n",color.BOLD,color.RED,color.END) 
        text(text_lose,1.0)
        exit() 

def ataque(): 
    """
    (uso de variables, uso de funciones,uso de condicionales)
    recibe: valor de nivel del usuario
    analiza cual es el nivel del usuario
    dependiendo del nivel llama un número random para generar un usuario
    devuelve: funcion de enemigo dependiendo del número random
    """
    global nivel
    text_enemigo=("¡Oh no! un enemigo ha aparecido\n") 
    text(text_enemigo,0.05)
    if nivel==1:
        enem_r=random.randint(0,2)
        if enem_r==0:
            diriol()
        if enem_r==1:
            bokoblin()
        if enem_r==2:
            baqus()
        if nivel==2:
            uraelth()
    if nivel==2:
        enem_r=random.randint(0,5)
        if enem_r==0:
            diriol()
        if enem_r==1:
            bokoblin()
        if enem_r==2:
            baqus()
        if enem_r==3:
            sorrowvine()
        if enem_r==4:
            warpfiend()
        if enem_r==5:
            dreadbug()
        if nivel==3:
            nightmask()
    if nivel==3:
        enem_r=random.randint(0,8)
        if enem_r==0:
            diriol()
        if enem_r==1:
            bokoblin()
        if enem_r==2:
            baqus()
        if enem_r==3:
            sorrowvine()
        if enem_r==4:
            warpfiend()
        if enem_r==5:
            dreadbug()
        if enem_r==6:
            gallmorph()
        if enem_r==7:
            slagghoul()
        if enem_r==8:
            chaosseker()
        if nivel==4:
            shadowling()
    if nivel==4:
        enem_r=random.randint(0,11)
        if enem_r==0:
            diriol()
        if enem_r==1:
            bokoblin()
        if enem_r==2:
            baqus()
        if enem_r==3:
            sorrowvine()
        if enem_r==4:
            warpfiend()
        if enem_r==5:
            dreadbug()
        if enem_r==6:
            gallmorph()
        if enem_r==7:
            slagghoul()
        if enem_r==8:
            chaosseker()
        if enem_r==9:
            slagbrood()
        if enem_r==10:
            netherling()
        if enem_r==11:
            acidtaur()
        if nivel==5:
            infernosnare()
    menu() 

def menu(): 
    """
    (uso de input, uso de funciones,uso de ciclo,uso de condicionales)
    recibe: input del usuario
    le muestra al usuario sus opciones
    el usuario ingresa que quiere hacer
    *si la opcion no esta disponible se le pide al usuario ingresar una opcion de nuevo
    devuelve: funcion dependiendo de accion del usuario
    """
    text_menu=("Que quieres hacer:\n") 
    text(text_menu,0.03)

    text_mover=("M - Moverte\n") 
    text(text_mover,0.03)

    text_stats=("S - Stats\n") 
    text(text_stats,0.03)

    text_inv=("I - Inventario\n") 
    text(text_inv,0.03)

    opc=str(input()) 

    while opc!="S" and opc!="s" and opc!="M" and opc!="m" and opc!="I" and opc!="i":
        text20=("Por favor escoge una de las opciones disponibles\n") 
        text(text20,0.05)
        opc=str(input()) 

    if opc=="S" or opc=="s": 
        stats() 
        menu() 
    if opc=="M" or opc=="m": 
        mover()
        menu()
    if opc=="I" or opc=="i": 
        inv()
        menu()

def mover(): 
    """
    (uso de variables, uso de funciones,uso de input, uso de ciclos,uso de condicionales)
    recibe: valor de dinero del usuario
    se le muestra al usuario a donde se puede mover y se le pide un input
    se muestra un texto de a donde se movio
    se genera un numero random,según ese número se llama a una función
    devuelve: funcion dependiendo del número random
    """
    global dinero
    text_movin=("A donde te quieres mover:\n") 
    text(text_movin,0.03)

    text_norte=("W - Norte\n") 
    text(text_norte,0.03)

    text_oeste=("A - Oeste\n") 
    text(text_oeste,0.03)

    text_sur=("S - Sur\n")
    text(text_sur,0.03)

    text_este=("D - Este\n") 
    text(text_este,0.03)

    dir=str(input()) 

    def text_dir(dir):
        """
    (uso de variables, uso de funciones,uso de condicionales, uso de ciclos)
    recibe: valor de velocidad y coordenadas del usuario,input de dirección
    se analiza el input que puso el usuario
    se muestra un texto de a donde se movio,con velocidad y coordenadas
    *si el usuario escogio un input erroneo se le muestra un mensaje de escoger bien y se reinicia la función
    devuelve: texto de movimiento del
    """
        global co_y
        global co_x
        global velocidad
        if dir=="W" or dir=="w":
            co_y=co_y+velocidad
            text_mov=("Te has movido ",velocidad," cuadros al Norte \n") 
            text(text_mov,0.03)
            text_coord=("Coordenadas: ",co_x,",",co_y,'\n') 
            text(text_coord,0.03)

        if dir=="A" or dir=="a":
            co_x=co_x-velocidad
            text_mov=("Te has movido ",velocidad," cuadros al Oeste \n") 
            text(text_mov,0.03)
            text_coord=("Coordenadas: ",co_x,",",co_y,'\n') 
            text(text_coord,0.03)

        if dir=="S" or dir=="s":
            co_y=co_y-velocidad
            text_mov=("Te has movido ",velocidad," cuadros al Sur \n") 
            text(text_mov,0.03)
            text_coord=("Coordenadas: ",co_x,",",co_y,'\n') 
            text(text_coord,0.03)

        if dir=="D" or dir=="d":
            co_x=co_x+velocidad
            text_mov=("Te has movido ",velocidad," cuadros al Este \n") 
            text(text_mov,0.03)
            text_coord=("Coordenadas: ",co_x,",",co_y,'\n') 
            text(text_coord,0.03)

        while dir!="W" and dir!="w" and dir!="A" and dir!="a" and dir!="S" and dir!="s" and dir!="D" and dir!="d":
            text_mov_cor=("Esa no es una direccion, escoge bien\n") 
            text(text_mov_cor,0.03)
            mover()

    text_dir(dir)
    turno=random.randint(0,3) 
            
    if turno==0: 
        text_nada=("Vaya parece que no hay nada por aquí, oh pero si encontraste una moneda\n") 
        text(text_nada,0.03)
        dinero=dinero+1.0
                    
    if turno==1: 
        ataque() 

    if turno==2: 
        text_pueblo=("Un pueblo,parece ser puedes obtener cosas aquí\n") 
        text(text_pueblo,0.03)
        text_bien=("Bienvenido aventurero, esto hay en la tienda hoy\n")
        text(text_bien,0.03)
        tienda()
            
    if turno==3: 
        obj() 
        menu()

    if co_x==150 and co_y==200:
        text_niña=("Oh una niñita,parece ser perdio su peluche\n")
        text(text_niña,0.03)
        if int(len(peluches))==1:
            text_dar=("Quieres darle el peluche que compraste?\n")
            text(text_dar,0.03)
            print("D - Darle el peluche")
            print("N - No darle nada")
            dar=input()
            while dar!="D" or dar!="d" or dar!="N" or dar!="n":
                text_ilegal=("No creo que eso sea legal\n")
                text(text_ilegal,0.03)
                dar=input()        
            if dar=="D" or dar=="d":
                peluches.remove("1")
                text_feliz=("Oh la niña se ve super alegre y parece ser te ha dado, un un lanzagranadas?, eehhh mejor no cuestiones, quien sabe por donde ha estado esa niña\n")
                text(text_feliz,0.03)
                granadas.append('1')
            if dar=="N" or dar=="n":
                text_triste=("Mira nomás lo que hiciste, ahora la niña esta triste y llorando, te sientes feliz contigo?\n")
                text(text_triste)
        else:
            text_nada=("Mmm,no parece ser que tengas nada para darle, mejor regresar a explorar\n")
            text(text_nada,0.03)

def inv(): 
    """
    (uso de variables, uso de funciones,uso de input,uso de condicionales)
    recibe: valor de listas de objetosmvida,velocidad y fuerza del usuario
    se le muestra al usuario que opciones tiene disponible de inventario
    *si el usuario no tiene nada, se le regresa al menú
    se actualizan los datos según el objeto que selecciono el usuario
    devuelve: inventario y stats actualizadas del usuario
    """
    """Metodo para remover objeto de una lista obtenido de https://uniwebsidad.com/libros/python/capitulo-7/metodos-de-eliminacion"""

    text_inv=("Escoge que quieres usar de tu inventario\n") 
    text(text_inv,0.03)
    global anillos
    global medallons
    global cascos
    global pocions
    global espadas
    global fuerza
    global vida
    global velocidad
    global manzanas
    global martillos
    global super_pocions
    global brazaletes
            
    def texto_inve():
        text_ani=("Anillos - ",int(len(anillos)),'\n')
        text(text_ani,0.05)
        text_meda=("Medallon - ",int(len(medallons)),'\n')
        text(text_meda,0.05)
        text_casc=("Casco - ",int(len(cascos)),'\n')
        text(text_casc,0.05)
        text_man=("Manzana - ",int(len(manzanas)),'\n')
        text(text_man,0.05)
            
        if int(len(espadas))==1:
            text_esp=("Espada de fuego\n")
            text(text_esp,0.05)    
            
        if int(len(pocions))>0:
            text_pot=("Pocion - ",int(len(pocions)),'\n')
            text(text_pot,0.05)
            
        if int(len(botas))==1:
            text_bot=("Botas de velocidad\n")
            text(text_bot,0.05) 

        if int(len(martillos))==1:
            text_mar=("Martillo de trueno\n")
            text(text_mar,0.05) 

        if int(len(super_pocions))>0:
            text_sp=("Super Pocion -",int(len(super_pocions)),'\n')
            text(text_sp,0.05) 

        if int(len(brazaletes))==1:
            text_br=("Brazalete de relampago\n")
            text(text_br,0.05) 

        if int(len(peluches))==1:
            text_pel=("Peluche\n")
            text(text_pel,0.05)

        if int(len(sombreros))>0:
            text_som=("Sombrero - ",int(len(sombreros)),'\n')
            text(text_som,0.05)

        if int(len(aks))==1:
            text_ak=("AK-47\n")
            text(text_ak,0.05) 

        if int(len(cangureras))==1:
            text_can=("Baticangurera\n")
            text(text_can,0.05)
            
        if int(len(afros))==1:
            text_afr=("Afro\n")
            text(text_afr,0.05)
            
        if int(len(rayos))==1:
            text_rayo=("Rayo de Mcqueen\n")
            text(text_rayo,0.05)
                        
        text_a=("A - Anillo de poder\n")
        text(text_a,0.03)
        text_m=("M - Medallon de velocidad\n")
        text(text_m,0.03)
        text_c=("C - Casco encantado\n")
        text(text_c,0.03)
        text_w=("W - Manzana\n")
        text(text_w,0.03)
            
        if int(len(espadas))==1:  
            text_e=("E - Espada de fuego\n")
            text(text_e,0.03)
            
        if int(len(pocions))>0:
            text_p=("P -Pocion\n")
            text(text_p,0.03)
                
        if int(len(botas))==1:  
            text_bot=("B - Botas flameantes\n")
            text(text_bot,0.03)
                
        if int(len(martillos))==1:  
            text_mar=("MA - Martillo de trueno\n")
            text(text_mar,0.03)
            
        if int(len(super_pocions))>0:
            text_sp=("SP -Super Pocion\n")
            text(text_sp,0.03)
                
        if int(len(brazaletes))==1:  
            text_br=("BR - Brazalete de relampago\n")
            text(text_br,0.03)

        if int(len(peluches))==1:
            text_pel=("PE - Peluche\n")
            text(text_pel,0.05) 
            
        if int(len(sombreros))>0:
            text_som=("S - Sombrero")
            text(text_som,0.05)

        if int(len(aks))==1:
            text_ak=("AK - AK-47\n")
            text(text_ak,0.05) 
            
        if int(len(cangureras))==1:
            text_can=("BT - Baticangurera")
            text(text_can,0.05)
            
        if int(len(afros))==1:
            text_afr=("AF - Afro")
            text(text_afr,0.05)
            
        if int(len(rayos))==1:
            text_rayo=("R - Rayo de Mcqueen")
            text(text_rayo,0.05)
                
        text_s=("S-Salir\n")
        text(text_s,0.03)

    if int(len(anillos))==0 and int(len(medallons))==0 and int(len(cascos))==0 and int(len(manzanas))==0 and int(len(espadas))==0 and int(len(pocions))==0 and int(len(botas))==0 and int(len(martillos))==0 and int(len(super_pocions))==0 and int(len(brazaletes))==0 and int(len(peluches))==0 and int(len(sombreros))==0 and int(len(aks))==0 and int(len(granadas))==0 and int(len(cangureras))==0 and int(len(afros))==0 and int(len(rayos))==0:
        text_nada_in=("Oh vaya, parece que no tienes nada en tu inventario\n")
        text(text_nada_in,0.03)
    
    else: 
        texto_inve()
        obj_inv=str(input())
        
        if obj_inv=="A" or obj_inv=="a":
            if int(len(anillos))<=0:
                text_n_a=("Ya no tienes aniilos disponibles,escoge algo más\n")
                text(text_n_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==1 and fuerza>=20:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==2 and fuerza>=30:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==3 and fuerza>=40:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==4 and fuerza>=50:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())
            else:
                text_ainv=("Has obtenido 1 de fuerza\n")
                text(text_ainv,0.03)
                fuerza=fuerza+1
                anillos.remove("1") 
                stats()
                texto_inve()
                obj_inv=str(input())
            
        if obj_inv=="M" or obj_inv=="m":
            if int(len(medallons))==0:
                text_n_m=("Ya no tienes medallones disponibles,escoge algo más\n")
                text(text_n_m,0.03)
                texto_inve()
                obj_inv=str(input())
            
            if nivel==1 and velocidad>=15:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==2 and velocidad>=25:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==3 and velocidad>=35:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==4 and velocidad>=45:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            else:
                text_minv=("Has obtenido 1.5 de velocidad\n")
                text(text_minv,0.03)
                velocidad=velocidad+1.5
                medallons.remove("1")
                stats()
                texto_inve()
                obj_inv=str(input())
                
        if obj_inv=="C" or obj_inv=="c":
            if int(len(cascos))<=0:
                text_n_c=("Ya no tienes cascos disponibles,escoge algo más\n")
                text(text_n_c,0.03)
                texto_inve()
                obj_inv=str(input())
    
            if nivel==1 and fuerza>=20:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==2 and fuerza>=30:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==3 and fuerza>=40:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==4 and fuerza>=50:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())
            else:
                text_cinv=("Has usado el casco, has obtenido 3.5 de fuerza, pero has perdido 4 de velocidad\n")
                text(text_cinv,0.03)
                fuerza=fuerza+3.5
                velocidad=velocidad-4
                cascos.remove("1")
                stats()
                texto_inve()
                obj_inv=str(input())
                    
        if obj_inv=="W" or obj_inv=="w":
            if int(len(manzanas))<=0:
                text_n_ma=("Ya no tienes manzanas disponibles,escoge algo más\n")
                text(text_n_ma,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==1 and vida>=20:
                text_no_p=("Ya has llegado al limite de vida\n")
                text(text_no_p,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==2 and vida>=45:
                text_no_p=("Ya has llegado al limite de vida\n")
                text(text_no_p,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==3 and vida>=65:
                text_no_p=("Ya has llegado al limite de vida\n")
                text(text_no_p,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==4 and vida>=90:
                text_no_sp=("Ya has llegado al limite de vida\n")
                text(text_no_sp,0.03)
                texto_inve()
                obj_inv=str(input())

            else:
                text_cinv=("Has usado una manzana, has obtenido 1 de vida\n")
                text(text_cinv,0.03)
                vida=vida+1 
                manzanas.remove("1")
                stats()
                texto_inve()
                obj_inv=str(input())
#------OBJ NIVEL 1                    
        if int(len(espadas))==1 and obj_inv=="E" or obj_inv=="e":
            if nivel==1 and fuerza>=20:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==2 and fuerza>=30:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==3 and fuerza>=40:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==4 and fuerza>=50:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())
            else:
                text_n_espada=("Has escogido tu espada\n")
                text(text_n_espada,0.03)
                fuerza=fuerza+5
                espadas.remove("1")
                stats()
                texto_inve()
                obj_inv=str(input())
                            
        if int(len(pocions))>0 and obj_inv=="P" or obj_inv=="p":
            if int(len(pocions))<=0:
                text_n_p=("Ya no tienes pociones disponibles,escoge algo más\n")
                text(text_n_p,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==1 and vida>=20:
                text_no_p=("Ya has llegado al limite de vida\n")
                text(text_no_p,0.03)
                texto_inve()
                obj_inv=str(input())
                
            elif nivel==2 and vida>=45:
                text_no_p=("Ya has llegado al limite de vida\n")
                text(text_no_p,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==3 and vida>=65:
                text_no_p=("Ya has llegado al limite de vida\n")
                text(text_no_p,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==4 and vida>=90:
                text_no_sp=("Ya has llegado al limite de vida\n")
                text(text_no_sp,0.03)
                texto_inve()
                obj_inv=str(input())

            else:
                text_cinv=("Has usado una poción, has obtenido 3 de vida\n")
                text(text_cinv,0.03)
                vida=vida+3  
                pocions.remove("1")
                stats()
                texto_inve()
                obj_inv=str(input())
                
        if int(len(botas))==1 and obj_inv=="B" or obj_inv=="b":         
            if nivel==1 and velocidad>=15:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==2 and velocidad>=25:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==3 and velocidad>=35:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==4 and velocidad>=45:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            else:
                text_n_botas=("Has escogido tus botas\n")
                text(text_n_botas,0.03)
                velocidad=velocidad+4
                botas.remove("1")
                stats()
                texto_inve()
                obj_inv=str(input())
                
#-----------OBJ NIVEL 2
        if int(len(martillos))==1 and obj_inv=="MA" or obj_inv=="ma":
            if nivel==1 and fuerza>=20:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==2 and fuerza>=30:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==3 and fuerza>=40:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==4 and fuerza>=50:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            else:
                text_n_martillo=("Has escogido tu martillo\n")
                text(text_n_martillo,0.03)
                fuerza=fuerza+7
                martillos.remove("1")
                stats()
                texto_inve()
                obj_inv=str(input())
                            
        if int(len(super_pocions))>0 and (obj_inv=="SP" or obj_inv=="sp"):
            if int(len(super_pocions))<=0:
                text_n_sp=("Ya no tienes super pociones disponibles,escoge algo más\n")
                text(text_n_sp,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==1 and vida>=20:
                text_no_sp=("Ya has llegado al limite de vida\n")
                text(text_no_sp,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==2 and vida>=45:
                text_no_sp=("Ya has llegado al limite de vida\n")
                text(text_no_sp,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==3 and vida>=65:
                text_no_sp=("Ya has llegado al limite de vida\n")
                text(text_no_sp,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==4 and vida>=90:
                text_no_sp=("Ya has llegado al limite de vida\n")
                text(text_no_sp,0.03)
                texto_inve()
                obj_inv=str(input())

            else:
                text_cinv=("Has usado una super poción, has obtenido 5 de vida\n")
                text(text_cinv,0.03)
                vida=vida+5 
                super_pocions.remove("1")
                stats()
                texto_inve()
                obj_inv=str(input())
                
        if int(len(brazaletes))==1 and obj_inv=="BR" or obj_inv=="br":         
            if nivel==1 and velocidad>=15:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==2 and velocidad>=25:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==3 and velocidad>=35:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==4 and velocidad>=45:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            else:
                text_a_bra=("Has escogido tus brazaletes\n")
                text(text_a_bra,0.03)
                velocidad=velocidad+6
                brazaletes.remove("1")
                stats()
                texto_inve()
                obj_inv=str(input())
                                        
#----------OBJ NIVEL 3
        if int(len(peluches))==1 and obj_inv=="PE" or obj_inv=="pe":
            text_pel=("Es un peluche bonito, pero no puedes hacer mucho con el\n")
            text(text_pel,0.03)
            texto_inve()
            obj_inv=str(input())

        if int(len(sombreros))>0 and (obj_inv=="S" or obj_inv=="s"):
            if nivel==1 and velocidad>=15:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==2 and velocidad>=25:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==3 and velocidad>=35:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==4 and velocidad>=45:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            else: 
                text_a_bra=("Has escogido tu sombrero\n")
                text(text_a_bra,0.03)
                velocidad=velocidad+8
                sombreros.remove("1")
                stats()
                texto_inve()
                obj_inv=str(input())
                                    

        if int(len(aks))==1 and obj_inv=="AK" or obj_inv=="ak":         
            if nivel==1 and fuerza>=20:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==2 and fuerza>=30:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==3 and fuerza>=40:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==4 and fuerza>=50:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            else:
                text_a_ak=("Has escogido tu AK-47\n")
                text(text_a_ak,0.03)
                fuerza=fuerza+10
                aks.remove("1")
                stats()
                texto_inve()
                obj_inv=str(input())
                                 
            
#-----------OBJ NIVEL 4
        if int(len(cangureras))==1 and obj_inv=="MA" or obj_inv=="ma":
            if nivel==1 and fuerza>=20:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==2 and fuerza>=30:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==3 and fuerza>=40:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==4 and fuerza>=50:
                text_no_a=("Ya has llegado al limite de fuerza")
                text(text_no_a,0.03)
                texto_inve()
                obj_inv=str(input())

            else:
                text_n_bat=("Has escogido tu baticangurera\n")
                text(text_n_bat,0.03)
                fuerza=fuerza+15
                cangureras.remove("1")
                stats()
                texto_inve()
                obj_inv=str(input())
            
        if int(len(rayos))>0 and (obj_inv=="R" or obj_inv=="r"):
            if nivel==1 and velocidad>=15:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==2 and velocidad>=25:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==3 and velocidad>=35:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            if nivel==4 and velocidad>=45:
                text_no_m=("Ya has llegado al limite de velocidad")
                text(text_no_m,0.03)
                texto_inve()
                obj_inv=str(input())

            else:
                text_a_bra=("Has escogido tu rayo\n")
                text(text_a_bra,0.03)
                velocidad=velocidad+15
                rayos.remove("1")
                texto_inve()
                obj_inv=str(input())
                        
        if int(len(afros))==1 and (obj_inv=="AF" or obj_inv=="af"):
            if int(len(afros))<=0:
                text_n_sp=("Ya no tienes afros disponibles,escoge algo más\n")
                text(text_n_sp,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==1 and vida>=20:
                text_no_sp=("Ya has llegado al limite de vida\n")
                text(text_no_sp,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==2 and vida>=45:
                text_no_sp=("Ya has llegado al limite de vida\n")
                text(text_no_sp,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==3 and vida>=65:
                text_no_sp=("Ya has llegado al limite de vida\n")
                text(text_no_sp,0.03)
                texto_inve()
                obj_inv=str(input())

            elif nivel==4 and vida>=90:
                text_no_sp=("Ya has llegado al limite de vida\n")
                text(text_no_sp,0.03)
                texto_inve()
                obj_inv=str(input())

            else:
                text_cinv=("Te has puesto un afro, has obtenido 12 de vida\n")
                text(text_cinv,0.03)
                vida=vida+12
                afros.remove("1")
                stats()
                texto_inve()
                obj_inv=str(input())

        if obj_inv=="S" or obj_inv=="s":
            text_salir=("Regresa a tu aventura\n")
            text(text_salir,0.03)

        else:
            text_bien=("Disculpa pero no tienes eso en tu inventario, escoge algo más\n")
            text(text_bien,0.03)
            texto_inve()
            obj_inv=str(input())

def obj():
    """
    (uso de variables, uso de funciones,uso de condicionales)
    recibe: listas de objetos
    se genera un número random del 0 al 3
    se le da al usuario un objeto según el número random
    devuelve: lista actualizada según el objeto generado
    """
    obj=random.randint(0,3) 
    global invent
    if obj==0:
        text_anillopoder=("¡HAS ENCONTRADO UN ANILLO DE PODER!, usalo con sabiduría\n")
        text(text_anillopoder,0.03)
        anillos.append('1')

    if obj==1:
        text_medallonvida=("¡HAS ENCONTRADO UN MEDALLON DE VELOCIDAD!, usalo con sabiduría\n")
        text(text_medallonvida,0.03)
        medallons.append('1')

    if obj==2:
        text_cascoencantado=("Has encontrado un casco encantado, te dice que ofrece poder, pero cuidado, que tiene magia oscura\n")
        text(text_cascoencantado,0.03)
        cascos.append('1')

    if obj==3:
        text_pocion=("¡HAS ENCONTRADO UNA MANZANA!, yummy\n")
        text(text_pocion,0.03)
        manzanas.append('1')
        
def tienda():
    """
    (uso de variables, uso de funciones,uso de input, uso de ciclos,uso de condicionales)
    recibe: valor de dinero y listas de objeto del usuario
    se le muestra al usuario lo que tiene disponible en la tienda
    *si su nivel es mayor a 1, se le  pide al usuario seleccionar una tienda
    se le pide al usuario seleccionar que objeto quiere comprar
    se actualiza el inventario y dinero según las decisiones del usuario
    devuelve: listas de objeto actualizadas
    """
    global dinero
    global nivel
    global espadas
    global pocions
    global botas
    global martillos
    global super_pocions
    global brazaletes
    global peluches
    global sombreros
    global aks
    global cangureras
    global afros
    global rayos
#---------------------FUNCIONES PARA TIENDA
    """
    (uso de funciones,uso de texto,uso de variables)
    recibe: valor de dinero
    se le muestra al usuario texto en donde sale que hay disponible en la tienda
    devuelve: texto de la tienda
    se repite la función para cada tienda, solo con objetos distintos
    """
    def text_t_1():
        text_dinero=("Dinero: ",dinero,'\n')
        text(text_dinero,0.05)
        text_espada=("EF - Espada de fuego (10 monedas)\n")
        text(text_espada,0.03)
        text_manzana=("P - Pocion (2 monedas)\n")
        text(text_manzana,0.03)
        text_botas=("BF - Botas flameantes (5 monedas)\n")
        text(text_botas,0.03)

    def text_t_2():
        text_espada=("MT - Martillo de trueno (15 monedas)\n")
        text(text_espada,0.03)
        text_manzana=("SP - Super Pocion (5 monedas)\n")
        text(text_manzana,0.03)
        text_botas=("BR - Brazalete de relampago (10 monedas)\n")
        text(text_botas,0.03)

    def text_t_3():
        text_espada=("PE - Peluche (20 monedas)\n")
        text(text_espada,0.03)
        text_manzana=("SO - Sombrero (25 monedas)\n")
        text(text_manzana,0.03)
        text_botas=("A - AK-47 (45 monedas)\n")
        text(text_botas,0.03)

    def text_t_4():
        text_espada=("C - Baticangurera (30 monedas)\n")
        text(text_espada,0.03)
        text_manzana=("AF - Afro (40 monedas)\n")
        text(text_manzana,0.03)
        text_botas=("R - Rayo de Mcqueen(Kachow) (50 monedas)\n")
        text(text_botas,0.03)

    """
    (uso de variables, uso de funciones,uso de input, uso de ciclos,uso de condicionales)
    recibe: valor de dinero del usuario
    se le muestra al usuario el dinero que tiene y se le pide seleccionar que quiere comprar
    se actualiza el dinero y lista de objeto según que compro el usuario
    devuelve: dinero e inventario actualizado
    se crean multiples funciones iguales para cada tienda de cada nivel
    """
    def op_tien_1():
        global dinero
        text_dinero=("Dinero: ",dinero,'\n')
        text(text_dinero,0.05)
        op_store=str(input())
        if op_store=="EF" or op_store=="ef":
            if int(len(espadas))==1:
                text_esp_full=("Ya tienes esta espada en tu inventario, porque no intentas escoger algo más\n")
                text(text_esp_full,0.03)
                tienda()

            elif dinero>=10:
                text_esp_inv=("La espada poderosa se ha agregado a tu inventario\n")
                text(text_esp_inv,0.03)
                espadas.append("1")
                dinero=dinero-10
                tienda()
                            
            elif dinero<10:
                text_falta=("Lo siento no tienes el dinero necesario\n")
                text(text_falta,0.03)
                tienda()
                            
        if op_store=="P" or op_store=="p":
            if int(len(pocions))==5:
                text_p_full=("Ya tienes suficiente pociones no crees?\n")
                text(text_p_full,0.03)
                tienda()
                                
            elif dinero>=2:
                text_p_inv=("Has comprado una pocion, se ha guardado en tu inventario\n")
                text(text_p_inv,0.03)
                pocions.append("1")
                dinero=dinero-2
                tienda()
                                                       
            elif dinero<2:
                text_falta=("Lo siento no tienes el dinero necesario\n")
                text(text_falta,0.03)
                tienda()
                        
        if op_store=="BF" or op_store=="bf":
            if int(len(botas))==1:
                text_bot_full=("Ya tienes estas botas en tu inventario, porque no intentas escoger algo más\n")
                text(text_bot_full,0.03)
                tienda()

            elif dinero>=5:
                text_b_inv=("Las botas flameantes se han agregado a tu inventario\n")
                text(text_b_inv,0.03)
                botas.append("1")
                dinero=dinero-5
                tienda()

            elif dinero<5:
                text_falta=("Lo siento no tienes el dinero necesario\n")
                text(text_falta,0.03)
                tienda()

        if op_store=="S" or op_store=="s":
            text_salir=("Vuelve a tu aventura\n")
            text(text_salir,0.03)
            menu()
  
        while op_store!="BF" and op_store=="bf" and op_store!="P" and op_store!="p" and op_store!="EF" and op_store!="ef" and op_store!="S" and op_store!="s":
            text_bien=("Disculpa pero eso no esta disponible, escoge algo más\n")
            text(text_bien,0.03)
            op_tien_1()

    def op_tiend_1():
        global dinero
        text_dinero=("Dinero: ",dinero,'\n')
        text(text_dinero,0.05)
        op_store=str(input())
        if op_store=="EF" or op_store=="ef":
            if int(len(espadas))==1:
                text_esp_full=("Ya tienes esta espada en tu inventario, porque no intentas escoger algo más\n")
                text(text_esp_full,0.03)
                op_tiend_1()  

            elif dinero>=10:
                text_esp_inv=("La espada poderosa se ha agregado a tu inventario\n")
                text(text_esp_inv,0.03)
                espadas.append("1")
                dinero=dinero-10
                op_tiend_1()     
     
            elif dinero<10:
                text_falta=("Lo siento no tienes el dinero necesario\n")
                text(text_falta,0.03)
                op_tiend_1()       
        if op_store=="P" or op_store=="p":
            if int(len(pocions))==5:
                text_p_full=("Ya tienes suficiente pociones no crees?\n")
                text(text_p_full,0.03)
                op_tiend_1() 

            elif dinero>=2:
                text_p_inv=("Has comprado una pocion, se ha guardado en tu inventario\n")
                text(text_p_inv,0.03)
                pocions.append("1")
                dinero=dinero-2
                op_tiend_1()           
            elif dinero<2:
                text_falta=("Lo siento no tienes el dinero necesario\n")
                text(text_falta,0.03)
                op_tiend_1()    
        if op_store=="BF" or op_store=="bf":
            if int(len(botas))==1:
                text_bot_full=("Ya tienes estas botas en tu inventario, porque no intentas escoger algo más\n")
                text(text_bot_full,0.03)
                op_tiend_1()  
            elif dinero>=5:
                text_b_inv=("Las botas flameantes se han agregado a tu inventario\n")
                text(text_b_inv,0.03)
                botas.append("1")
                dinero=dinero-5
                op_tiend_1()     
            elif dinero<5:
                text_falta=("Lo siento no tienes el dinero necesario\n")
                text(text_falta,0.03)
                op_tiend_1()
        if op_store=="S" or op_store=="s":
            text_salir=("Veamos que más hay\n")
            text(text_salir,0.03)
            tienda()

        while op_store!="BF" and op_store=="bf" and op_store!="P" and op_store!="p" and op_store!="EF" and op_store!="ef" and op_store!="S" and op_store!="s":
            text_bien=("Disculpa pero eso no esta disponible, escoge algo más\n")
            text(text_bien,0.03)
            op_tiend_1()

    def op_tien_2():
        global dinero
        text_dinero=("Dinero: ",dinero,'\n')
        text(text_dinero,0.05)
        op_store=str(input())
        if op_store=="MT" or op_store=="mt":
            if int(len(martillos))==1:
                text_esp_full=("Ya tienes este martillo en tu inventario, porque no intentas escoger algo más\n")
                text(text_esp_full,0.03)
                op_tien_2()
            elif dinero>=15:
                text_esp_inv=("El martillo de trueno se ha agregado a tu inventario\n")
                text(text_esp_inv,0.03)
                martillos.append("1")
                dinero=dinero-15
                op_tien_2()
            elif dinero<15:
                text_falta=("Lo siento no tienes el dinero necesario\n")
                text(text_falta,0.03)
                op_tien_2()
                        
        if op_store=="SP" or op_store=="sp":
            if int(len(super_pocions))==3:
                text_p_full=("Ya tienes suficiente super pociones no crees?\n")
                text(text_p_full,0.03)
                op_tien_2()

            elif dinero>=5:
                text_p_inv=("Has comprado una super pocion, se ha guardado en tu inventario\n")
                text(text_p_inv,0.03)
                super_pocions.append("1")
                dinero=dinero-2
                op_tien_2()
        
            elif dinero<5:
                text_falta=("Lo siento no tienes el dinero necesario\n")
                text(text_falta,0.03)
                op_tien_2()
                  
        if op_store=="BR" or op_store=="br":
            if int(len(brazaletes))==1:
                text_bot_full=("Ya tienes este brazalete en tu inventario, porque no intentas escoger algo más\n")
                text(text_bot_full,0.03)
                op_tien_2()
            elif dinero>=10:
                text_b_inv=("El brazalete de relampago se ha agregado a tu inventario\n")
                text(text_b_inv,0.03)
                brazaletes.append("1")
                dinero=dinero-10
                op_tien_2()
            elif dinero<10:
                text_falta=("Lo siento no tienes el dinero necesario\n")
                text(text_falta,0.03)
                op_tien_2()

        if op_store=="S" or op_store=="s":
            text_salir=("Veamos que más hay\n")
            text(text_salir,0.03)
            tienda()

        while op_store!="S" and op_store=="s" and op_store!="BR" and op_store!="br" and op_store!="SP" and op_store!="sp" and op_store!="MT" and op_store!="mt":
            text_bien=("Disculpa pero eso no esta disponible, escoge algo más\n")
            text(text_bien,0.03)
            op_tien_2()
            

    def op_tien_3():
        while dinero>0:
            text_dinero=("Dinero: ",dinero,'\n')
            text(text_dinero,0.05)
            op_store=str(input())
            if op_store=="PE" or op_store=="pe":
                if int(len(peluches))==1:
                    text_esp_full=("Ya tienes este peluche en tu inventario, porque no intentas escoger algo más\n")
                    text(text_esp_full,0.03)
                    op_tien_3()
                elif dinero>=25:
                    text_esp_inv=("El peluche se ha agregado a tu inventario\n")
                    text(text_esp_inv,0.03)
                    peluches.append("1")
                    dinero=dinero-20
                    op_tien_3()
                elif dinero<20:
                    text_falta=("Lo siento no tienes el dinero necesario\n")
                    text(text_falta,0.03)
                    op_tien_3()
                    
            if op_store=="SO" or op_store=="so":
                if int(len(sombreros))==3:
                    text_p_full=("Ya tienes suficientes sombreros no crees?\n")
                    text(text_p_full,0.03)
                    op_tien_3()
                elif dinero>=25:
                    text_p_inv=("Has comprado un sombrero, se ha guardado en tu inventario, te ves fiu fiu\n")
                    text(text_p_inv,0.03)
                    sombreros.append("1")
                    dinero=dinero-25
                    op_tien_3()
                elif dinero<25:
                    text_falta=("Lo siento no tienes el dinero necesario\n")
                    text(text_falta,0.03)
                    op_tien_3()
                        
            if op_store=="A" or op_store=="a":
                if int(len(aks))==1:
                    text_bot_full=("Ya tienes este AK-47, porque no intentas escoger algo más\n")
                    text(text_bot_full,0.03)
                    op_tien_3()
                elif dinero>=45:
                    text_b_inv=("El AK-47 se ha agregado a tu inventario\n")
                    text(text_b_inv,0.03)
                    aks.append("1")
                    dinero=dinero-10
                    op_tien_3()
                elif dinero<45:
                    text_falta=("Lo siento no tienes el dinero necesario\n")
                    text(text_falta,0.03)
                    op_tien_3()
            if op_store=="S" or op_store=="s":
                text_salir=("Veamos que más hay\n")
                text(text_salir,0.03)
                tienda()

            while op_store!="PE" and op_store=="pe" and op_store!="SO" and op_store!="so" and op_store!="A" and op_store!="a" and op_store!="S" and op_store!="s":
                text_bien=("Disculpa pero eso no esta disponible, escoge algo más\n")
                text(text_bien,0.03)
                op_tien_3()

    def op_tien_4():
        text_dinero=("Dinero: ",dinero,'\n')
        text(text_dinero,0.05)
        op_store=str(input())
        if op_store=="C" or op_store=="c":
            if int(len(cangureras))==1:
                text_esp_full=("Ya tienes este baticinturon en tu inventario, porque no intentas escoger algo más\n")
                text(text_esp_full,0.03)
                op_tien_4()
            elif dinero>=30:
                text_esp_inv=("La baticangurera se ha agregado a tu inventario,ahora estas bati-vestido\n")
                text(text_esp_inv,0.03)
                cangureras.append("1")
                dinero=dinero-30
                op_tien_4()
            elif dinero<30:
                text_falta=("Lo siento no tienes el dinero necesario\n")
                text(text_falta,0.03)
                op_tien_4()
                        
        if op_store=="AF" or op_store=="af":
            if int(len(afros))==1:
                text_p_full=("Ya tienes suficientes afros no crees?\n")
                text(text_p_full,0.03)
                op_tien_4()
            elif dinero>=40:
                text_p_inv=("Has comprado un afro, se ha guardado en tu inventario, ahora estas en la onda\n")
                text(text_p_inv,0.03)
                afros.append("1")
                dinero=dinero-40
                op_tien_4()
            elif dinero<40:
                text_falta=("Lo siento no tienes el dinero necesario\n")
                text(text_falta,0.03)
                op_tien_4()
            
        if op_store=="R" or op_store=="r":
            if int(len(rayos))==1:
                text_bot_full=("Ya tienes este rayo mcqueenesco, porque no intentas escoger algo más\n")
                text(text_bot_full,0.03)
                op_tien_4()
            elif dinero>=50:
                text_b_inv=("El Rayo de Mcqueen se ha agregado a tu inventario, ahora..eres....veloz\n")
                text(text_b_inv,0.03)
                rayos.append("1")
                dinero=dinero-50
                op_tien_4()
            elif dinero<50:
                text_falta=("Lo siento no tienes el dinero necesario\n")
                text(text_falta,0.03)
                op_tien_4()

        if op_store=="S" or op_store=="s":
            text_salir=("Veamos que más hay\n")
            text(text_salir,0.03)
            tienda()

        while op_store!="C" and op_store=="c" and op_store!="Af" and op_store!="af" and op_store!="R" and op_store!="r" and op_store!="S" and op_store!="s":
            text_bien=("Disculpa pero eso no esta disponible, escoge algo más\n")
            text(text_bien,0.03)
            op_tien_2()

#------NIVEL 1
    if nivel==1:
        text_t_1()
        text_s=("S-Salir\n")
        text(text_s,0.03)
        while dinero<=0:
            text_nada=("Vaya parece ser que no tienes nada de dinero, mejor sal a explorar\n")
            text(text_nada,0.03)
            menu()
        else:
            op_tien_1()
            menu()          
#-------NIVEL 2               
    if nivel==2: 
        while dinero<=0:   
            text_nada=("Vaya parece ser que no tienes nada de dinero, mejor sal a explorar\n")
            text(text_nada,0.03) 
            menu()   
        else:
            num_tienda=("Cuál tienda quieres escoger\n")
            text(num_tienda,0.03)
            t_1=("1 - Tienda Nivel 1\n")
            text(t_1,0.03)
            t_2=("2 - Tienda Nivel 2\n")                    
            text(t_2,0.03)
            text_s=("S-Salir\n")
            text(text_s,0.03) 
            tienda_op=str(input())
            if tienda_op=="1":
                text_t_1() 
                text_s=("S-Salir\n")
                text(text_s,0.03)  
                op_tiend_1()
            if tienda_op=="2":
                text_t_2()
                text_s=("S-Salir\n")
                text(text_s,0.03) 
                op_tien_2()
            if tienda_op=="S" or tienda_op=="s":
                text_salir=("Regresa a tu aventura\n")
                text(text_salir,0.03)
                menu()
            else:
                text_no=("Lo siento pero ese departamento no me suena\n")
                text(text_no,0.03)
                tienda()
#------------NIVEL 3
    if nivel==3:
            if dinero<=0:
                text_nada=("Vaya parece ser que no tienes nada de dinero, mejor sal a explorar\n")
                text(text_nada,0.03) 
            else:
                num_tienda=("Cuál tienda quieres escoger\n")
                text(num_tienda,0.03)
                t_1=("1 - Tienda Nivel 1")
                text(t_1,0.03)
                t_2=("2 - Tienda Nivel 2")
                text(t_2,0.03)
                t_3=("3 - Tienda Nivel 3")
                text(t_3,0.03)
                text_s=("S-Salir\n")
                text(text_s,0.03) 
                tienda_op=str(input())
                if tienda_op=="1":
                    text_t_1() 
                    text_s=("S-Salir\n")
                    text(text_s,0.03)  
                    op_tiend_1()
                if tienda_op=="2":
                    text_t_2()
                    text_s=("S-Salir\n")
                    text(text_s,0.03) 
                    op_tien_2()
                if tienda_op=="3":
                    text_t_3()
                    text_s=("S-Salir\n")
                    text(text_s,0.03) 
                    op_tien_3()
                if tienda_op=="S" or tienda_op=="s":
                    text_salir=("Regresa a tu aventura\n")
                    text(text_salir,0.03)
                    menu()
                else:
                    text_no=("Lo siento pero ese departamento no me suena\n")
                    text(text_no,0.03)
                    tienda()
#------------NIVEL 4
    if nivel==4:
            if dinero<=0:
                text_nada=("Vaya parece ser que no tienes nada de dinero, mejor sal a explorar\n")
                text(text_nada,0.03)         
            else:
                num_tienda=("Cuál tienda quieres escoger\n")
                text(num_tienda,0.03)
                t_1=("1 - Tienda Nivel 1")
                text(t_1,0.03)
                t_2=("2 - Tienda Nivel 2")
                text(t_2,0.03)
                t_3=("3 - Tienda Nivel 3")
                text(t_3,0.03)
                t_4=("4 - Tienda Nivel 4")
                text(t_4,0.03)
                text_s=("S-Salir\n")
                text(text_s,0.03) 
                tienda_op=str(input())
                if tienda_op=="1":
                    text_t_1() 
                    text_s=("S-Salir\n")
                    text(text_s,0.03)  
                    op_tiend_1()
                if tienda_op=="2":
                    text_t_2()
                    text_s=("S-Salir\n")
                    text(text_s,0.03) 
                    op_tien_2()
                if tienda_op=="3":
                    text_t_3()
                    text_s=("S-Salir\n")
                    text(text_s,0.03) 
                    op_tien_3()
                if tienda_op=="4":
                    text_t_4()
                    text_s=("S-Salir\n")
                    text(text_s,0.03) 
                    op_tien_4()
                if tienda_op=="S" or tienda_op=="s":
                    text_salir=("Regresa a tu aventura\n")
                    text(text_salir,0.03)
                    menu()
                else:
                    text_no=("Lo siento pero ese departamento no me suena\n")
                    text(text_no,0.03)
                    tienda() 
menu() 