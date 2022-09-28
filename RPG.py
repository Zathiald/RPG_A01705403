from time import sleep #Importamos la libreria de tiempo para usar la función de sleep

import sys #Importamos la librería de sys, donde usaremos la función de flush

import random #Importamos la función para poder generar un número random
#Metodo para generar un numero random obtenido de https://j2logo.com/python/generar-numeros-aleatorios-en-python/

#--------------------------------------------FUNCIÓN PARA TEXTO--------------------------------------------------------------------------------------------------
def text(texto,speed):#Hacemos una función para hacer que el texto aparezca fluido 
    for c in texto: #Establecemos que por cada letra del texto
        print(c,end='') #Se da un espacio por letra
        sys.stdout.flush() #Extraemos la función flush de sys para hacer que el texto aparezca corrido
        sleep(speed) #Imprimimos una letra cada 0.1 segundos, podemos cambiar para imprimir el texto más lento

class color: #Valores para colores obtenidos de https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
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
#------------------------------------------GUARDAR Y CREAR VARIABLES-----------------------------------------------------------------------------------------------------------------------------------   

#---Inventario
anillos=[] #Creamos una variable externa para poder guardar anillo
medallons=[] #Creamos una variable externa para poder guardar medallon
cascos=[] #Creamos una variable externa para poder guardar cascos
espadas=[]
manzanas=[]
botas=[]
martillos=[]
brazaletes=[]
super_pocions=[]
pocions=[] #Creamos una variable externa para poder guardar pociones
ballestas=[] #Ballesta penetradora
peluches=[]
sombreros=[] #Sombrero fiu fiu
aks=[]
granadas=[]
cangureras=[]
afros=[]
rayos=[]


#---Stats
vida= 5.0 #Se guarda la variable de vida
velocidad = 4.0 #Se guarda la variable de velocidad
fuerza = 3.5 #Se guarda la variable de fuerza
nivel = 1.0 #Se guarda el nivel
exp = 0.0 #Se guarda la experiencia
dinero = 0.0 #Se guarda el dinero
co_x=0.0
co_y=0.0   
   
def stats(): #Creamos una función que presentara las stats cada vez que la llamamos

    name_text=("Nombre: ",name,'\n')
    text(name_text,0.5)

    vida_text=("Vida: ",vida,'\n') #Se presenta la vida
    text(vida_text,0.5)

    velocidad_text=("Velocidad: ",velocidad,'\n') #Se presenta la velocidad
    text(velocidad_text,0.5)

    fuerza_text=("Fuerza: ",fuerza,'\n') #Se presenta la fuerza
    text(fuerza_text,0.5)
    
    nivel_text=("Nivel: ",nivel,'\n') #Se presenta su nivel
    text(nivel_text,0.5)

    exp_text=("Exp: ",exp,'\n') #Se presenta su exp
    text(exp_text,0.5)
    
    dinero_text=("Dinero: ",dinero,'\n') #Se presenta su exp
    text(dinero_text,0.5)
    
    coord_text=("Coordenadas: ",co_x,",",co_y,'\n') #Se presenta su exp
    text(coord_text,0.5)
 
def tut():
    text_intro=("Bienvenido al Mundo de Palgia, un lugar lleno de misterios y peligros, aventuras y amenazas\n")
    text(text_intro,0.03)

    text9=("Estos son tus stats iniciales\n") #Se le presenta al jugador sus stats iniciales
    text(text9,0.03)
        
    stats() #Llamamos a la función de stats para mostrarselas al jugador

    text10=("Si en algún momento quieres ver tus stats presiona S al inicio de cada turno\n") #Se le dice al usuario que al presionar S puede ver sus stats
    text(text10,0.03)

    text11=("Para moverte presiona las teclas W,A,S,D y te moveras en esa dirección\n") #Se le dice al usuario como hacer para seleccionar dirección de movimiento
    text(text11,0.03)

    text12=("Según tu velocidad es cuantos cuadros podras moverte por turno y también cuanta chance tienes para atacar a tu enemigo\n") #Se le dice al usuario cuanto se movera según su velocidad
    text(text12,0.03)

    text13=("Mientras más velocidad más chance de atacar\n") #Se le da un ejemplo de la velocidad
    text(text13,0.03)

    text14=("Para escoger moverte al inicio de cada turno presiona M\n") #Se le dice al usuario como hacer para moverse
    text(text14,0.03)

    text15=("Al escoger la opción de moverte, hay una posibilidad de que aparezca un enemigo, pueblo u objeto en tu camino\n") #Se le dice al usuario como hacer para moverse
    text(text15,0.03)

    text16=("Por toda Palgia hay varios objetos místicos, usalos con sabiduría para obtener ventaja en combate\n") #Se le dice al usuario como hacer para moverse
    text(text16,0.03)

    text17=("Pero cuidado, que algunos objetos estan embrujados y te podrían bajar los stats\n") #Se le dice al usuario como hacer para moverse
    text(text17,0.03)

    text18=("Para ver y escoger un objeto al inicio de cada turno presiona I\n") #Se le dice al usuario como hacer para moverse
    text(text18,0.03)

    text19=("Ahora que estas familiarizado con las acciones básicas\n") #Se le dice al usuario como hacer para moverse
    text(text19,0.03)

#--------------------------------------------INGRESO JUGADOR--------------------------------------------------------------------------------------------------

#Metodo para hacer aparecer el texto lentamente obtenido de https://es.stackoverflow.com/questions/25901/como-imprimir-una-cadena-de-texto-con-pausas-entre-cada-letra-impresa-en-python
text1 = ("Como te llamas héroe o heroína: ") #Se le pide al usuario su nombre
text(text1,0.03)

name=str(input())

text2=("Bienvenid@ ",str(name),'\n') #Se le saluda al usuario
text(text2,0.5)

text3=("Estas a punto de embarcarte en una aventura\n") #Se le da al usuario una bienvenida a la aventura
text(text3,0.03)

text4=("¿Estás listo?\n") #Se le pregunta si esta listo para el viaje
text(text4,0.03)

#Metodo obtenido en https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number, donde explica como hacer un loop infinito con comparadores
while True: #Especificamos que mientras sea verdadero
    print("Y-si") #Mostramos las opciones disponibles, ya sean y o n
    print("N-no")
    opcion=str(input()) #Creamos una variable para la selección
    if opcion == "y" or opcion == "Y": #Establecemos que pasa si escogen si
        text5=("Muy bien,¡COMENCEMOS!\n") #Damos este mensaje
        text(text5,0.05)
        break #Seguimos el código
    elif opcion == "n" or opcion == "N": #Establecemos que pasa si escogen no
        text6=("Vaya,pues ni modo,¡HORA DE EXPLORAR!\n") #Damos este mensaje
        text(text6,0.05)
        break #Seguimos el código
    else: #Establecemos que pasa si no se escoge entre si y no
        text7=("Escoge bien\n") #Damos este mensaje
        text(text7,0.05)
        continue #Reiniciamos el loop
    
text_tu=("Pero antes, quieres ver el tutorial?\n")
text(text_tu,0.03)
while True: #Especificamos que mientras sea verdadero
    print("Y-si") #Mostramos las opciones disponibles, ya sean y o n
    print("N-no")
    op_tu=str(input())#Creamos una variable para la selección
    if op_tu == "y" or op_tu == "Y": #Establecemos que pasa si escogen si
        text5=("Okey, vamos al tutorial\n") #Damos este mensaje
        text(text5,0.05)
        tut() #Seguimos el código
        break
    elif op_tu == "n" or op_tu == "N": #Establecemos que pasa si escogen no
        text6=("Ah un aventurero,¡HORA DE AVENTURA!(TM)\n") #Damos este mensaje
        text(text6,0.05)
        text_intro=("Bienvenido al Mundo de Palgia, un lugar lleno de misterios y peligros, aventuras y amenazas\n")
        text(text_intro,0.03)
        break#Seguimos el código
    else: #Establecemos que pasa si no se escoge entre si y no
        text7=("Escoge bien\n") #Damos este mensaje
        text(text7,0.05)
        continue #Reiniciamos el loop

#---------------------------------------FUNCIONES PRINCIPALES-----------------------------------------------------------------------------------------------------

def Infernosnare(): #Hacemos una función para el cuarto boss
    enem("Infernosnare",20,23,25,15,20)

def Acidtaur(): #Hacemos una función para los Acidtaurs
    enem("Acidtaur",8,7.5,10,7,8.5)

def Netherling(): #Hacemos una función para los Netherlings
    enem("Netherling",7.5,7,9.5,6.5,8)

def Slagbrood(): #Hacemos una función para los Slagbroods
    enem("Slagbrood",7,6.5,9.5,6,7.5)

def Shadowling(): #Hacemos una función para el tercer boss
    enem("Shadowling",15,17,20,10,15)

def Chaosseker(): #Hacemos una función para los Chaossekers
    enem("Chaosseker",6.5,6,9,5.5,7)

def Slagghoul(): #Hacemos una función para los Slagghouls
    enem("Slagghoul",5,5.5,8.5,5,6.5)

def Gallmorph(): #Hacemos una función para los Gallmorphs
    enem("Galmorph",4.5,5.5,8,4.5,6)

def Nightmask(): #Hacemos una función para el segundo boss
    text_nightmask=("Un caballero...pero algo no esta bien con el,creo creo que esta poseído\n")
    text(text_nightmask,0.03)
    enem("Nightmask",10,12,15,7,8)

def Dreadbug(): #Hacemos una función para los Dreadbug
    enem("Dreadbug",4.5,5,7.5,4,5.5)

def Warpfiend():#Hacemos una función para los Warpfiend
    enem("Warpfiend",4,4,7,6.5,3.5,5)

def Sorrowvine(): #Hacemos una función para los Sorrowvine
    enem("Sorrowvine",3.5,3.5,6.5,3,4.5)

def Uraelth(): #Hacemos una función para el primer boss
    text_uraelth=("Parece ser que te has topado con un dragón, y este tiene hambre de aventurer@\n")
    text(text_uraelth,0.03)
    enem("Uraelth",5.5,7,10,5,5)

def Baqus(): #Hacemos una función para los baqus
    enem("Baqus",3.5,3,6,2.5,4)

def Bokoblin():#Hacemos una función para los bokoblins
    enem("Bokoblin",2,2.5,5.5,2,3.5)

def Diriol(): #Hacemos una función para los diriol
    enem("Diriol",1,2,5,1,2)

def subir_nivel():
    global vida 
    global velocidad
    global fuerza
    global nivel
    global exp
    if nivel==1 and exp>=10: #Establecemos que pasa si el usuario consigue 10 de experiencia
        nivel =nivel+1 #Le sumamos 1 a su nivel
        vida = vida+10 #Le agregamos 2 a la vida 
        velocidad = velocidad+7 #Le agregamos 2 a la velocidad
        fuerza = fuerza+5 #Le agregamos 2 a la fuerza
        text_subir=(color.BOLD,"¡Has subido de nivel! ¡FELICIDADES!, pero cuidado, ahora habra enemigos más poderosos\n",color.BOLD,color.END) #Le mostramos un mensaje de felicitación
        text(text_subir,0.05)
        stats()
    if nivel==2 and exp>=25:
        nivel = nivel+1
        vida = vida+20
        velocidad = velocidad + 10
        fuerza = fuerza + 10
        text_subir=(color.BOLD,"¡Has subido de nivel! ¡FELICIDADES!, pero cuidado, ahora habra enemigos más poderosos\n",color.BOLD,color.END) #Le mostramos un mensaje de felicitación
        text(text_subir,0.05)
        stats()
    if nivel==3 and exp>=50:
        nivel = nivel+1
        vida = vida+30
        velocidad = velocidad + 15
        fuerza = fuerza + 15
        text_subir=(color.BOLD,"¡Has subido de nivel! ¡FELICIDADES!, pero cuidado, ahora habra enemigos más poderosos\n",color.BOLD,color.END) #Le mostramos un mensaje de felicitación
        text(text_subir,0.05)
        stats()

def enem(name_enem,fuerza_enem,velocidad_enem,vida_enem,exp_enem,dinero_enem): #Hacemos una función por enemigo para alterar simplementa el nombre,fuerzas,velocidad y vida

    name_enem= str(name_enem)
    fuerza_enem = float(fuerza_enem) #Declaramos la fuerza de este enemigo
    velocidad_enem = float(velocidad_enem) #Declaramos la velocidad de este enemigo
    vida_enem = float(vida_enem) #Declaramos la vida de este enemigo
    exp_enem = float(exp_enem) #Declaramos la experiencia que da este enemigo
    dinero_enem = float(dinero_enem) #Declaramos cuanto dinero da este enemigo

    #Metodo para declarar global variable obtenido de https://bobbyhadz.com/blog/python-unboundlocalerror-local-variable-name-referenced-before-assignment#:~:text=The%20Python%20"UnboundLocalError%3A%20Local%20variable,function%20definition%2C%20e.g.%20global%20my_var%20.
    global vida 
    global velocidad
    global fuerza
    global nivel
    global exp
    global dinero
    vida_=vida

    text_enem=("Los stats de este enemigo son: \n") #Mostramos los stats de el enemigo
    text(text_enem,0.05)

    nom_enem_t=("Nombre: ",name_enem,'\n') #Se presenta su vida
    text(nom_enem_t,0.5)

    velocidad_enem_t=("Velocidad: ",velocidad_enem,'\n') #Se presenta su velocidad
    text(velocidad_enem_t,0.5)

    fuerza_enem_t=("Fuerza: ",fuerza_enem,'\n') #Se presenta su fuerza
    text(fuerza_enem_t,0.5)
    
    vida_enem_t=("Vida: ",vida_enem,'\n') #Se presenta la fuerza
    text(vida_enem_t,0.5)

    while True: #Creamos un loop para la secuencia de ataque
        text_atac=("Presiona X para atacar \n") #Le decimos al usuario que presione X para atacar
        text(text_atac,0.05)
        text_atac=("Presiona I para abrir inventario \n") #Le decimos al usuario que presione X para atacar
        text(text_atac,0.05)
        
        atac=str(input()) #Registramos el ataque

        if atac=="I" or atac=="i":
            inv()
            continue

        if atac=="X" or atac=="x": #Declaramos que pasa si el usuario presiona X

            if velocidad<velocidad_enem: #Declaramos que pasa si la velocidad de el enemigo es mayor a la nuestra
                atak=random.randint(0,1) #Generamos un número random, para que sucedad la posibilidad de que falle el ataque
                #Declaramos que la variable sera un número integer random, de entre 0 a 1, es decir 50% probabilidad de que falle

                if atak==0: #Declaramos que pasa si el número random es 0
                    enem_ataque(fuerza_enem)
                    continue
   
                if atak==1: #Declaramos que pasa si el número random es 1
                    vida_enem=vida_enem-fuerza #Si el número random es 1, le quitamos vida al enemigo

                    text_atacar=("¡Has atacado al enemigo!\n") #Le decimos al usuario que ha logrado atacar al enemigo
                    text(text_atacar,0.05)

                    text_vida_e=("Su vida ahora es ",vida_enem,'\n') #Mostramos la nueva vida del enemigo
                    text(text_vida_e,0.05)

                    if vida_enem==0 or vida_enem<0: #Si la vida del enemigo es igual o menor a 0, le decimos al usuario que gano
                        text_win=(color.BOLD,color.BLUE,"¡LO LOGRASTE!\n",color.BOLD,color.BLUE,color.END) #Le mostramos el mensaje de victoria al usuario
                        text(text_win,0.05)
                        exp=exp+exp_enem #Le sumamos experiencia al usuario
                        dinero=dinero+dinero_enem
                        stats() #Le mostramos sus stats de nuevo
                        if nivel==1 and exp>=7: #Establecemos que pasa si el usuario consigue 10 de experiencia
                          subir_nivel()
                        break #Seguimos el código y mostramos de nuevo el menú

                    if vida_enem>0: #Declaramos que pasa si la vida del enemigo es mayor a 0
                        continue #Reiniciamos el loop

            elif velocidad>velocidad_enem or velocidad==velocidad_enem: #Declaramos que pasa si nuestra velocidad mayor a la del enemigo
                atak=random.randint(0,3) #Generamos un número random, para que sucedad la posibilidad de que falle el ataque
                #Declaramos que la variable sera un número integer random, de entre 0 a 3, es decir 25% probabilidad de que falle

                if atak==0: #Declaramos que pasa si el número random es 0
                    enem_ataque(fuerza_enem)
                    continue
   
                if atak==1 or 2 or 3: #Declaramos que pasa si el número random es 1,2,3
                    vida_enem=vida_enem-fuerza #Si el número random es 1,2,3 , le quitamos vida al enemigo

                    text_atacar=("¡Has atacado al enemigo!\n") #Le decimos al usuario que ha logrado atacar al enemigo
                    text(text_atacar,0.05)

                    text_vida_e=("Su vida ahora es ",vida_enem,'\n') #Mostramos la nueva vida del enemigo
                    text(text_vida_e,0.05)

                    if vida_enem==0 or vida_enem<0: #Si la vida del enemigo es igual o menor a 0, le decimos al usuario que gano
                        text_win=(color.BOLD,color.BLUE,"¡LO LOGRASTE!\n",color.BOLD,color.BLUE,color.END) #Le mostramos el mensaje de victoria al usuario
                        text(text_win,0.05)
                        exp=exp+exp_enem #Le sumamos experiencia al usuario
                        dinero=dinero+dinero_enem
                        stats() #Le mostramos sus stats de nuevo
                        if nivel==1 and exp>=7: #Establecemos que pasa si el usuario consigue 10 de experiencia
                            subir_nivel()
                        break #Seguimos el código y mostramos de nuevo el menú

                    if vida_enem>0: #Declaramos que pasa si la vida del enemigo es mayor a 0
                        continue #Reiniciamos el loop

        else: #Declaramos que pasa si el usuario no presiona X o I o E
            vida=vida-fuerza_enem #Si el número random es 0, le quitamos vida al enemigo
            text_atacado=(color.BOLD,"¡NO ATACASTE!",color.BOLD,color.END,"Ahora el enemigo te ha atacado\n") #Le decimos al usuario que su vida fallo
            text(text_atacado,0.05)

            text_vida_u=("Tu vida ahora es ",vida,'\n') #Le mostramos su nueva vida
            text(text_vida_u,0.05)
                
            if vida>0: #Si la vida del usuario es mayor a 0, puede atacar de nuevo
                continue

            if vida==0 or vida<0: #Si la vida del usuario es menor o igual a 0, le mostramos un mensaje de Game Over
                text_lose=(color.BOLD,color.RED,"¡GAME OVER!\n",color.BOLD,color.RED,color.END) #Le mostramos al usuario un mensaje de game over
                text(text_lose,1.0)
                exit() #Terminamos el código si se nos acaba la vida
                
def enem_ataque(fuerza_mal):
    global vida

    while True:
        vida=vida-fuerza_mal #Si el número random es 0, le quitamos vida al enemigo
        text_atacado=("¡FALLASTE!. Ahora el enemigo te ha atacado\n") #Le decimos al usuario que su vida fallo
        text(text_atacado,0.05)

        text_vida_u=("Tu vida ahora es ",vida,'\n') #Le mostramos su nueva vida
        text(text_vida_u,0.05)
                
        if vida>0: #Si la vida del usuario es mayor a 0, puede atacar de nuevo
            break

        if vida==0 or vida<0: #Si la vida del usuario es menor o igual a 0, le mostramos un mensaje de Game Over
            text_lose=(color.BOLD,color.RED,"¡GAME OVER!\n",color.BOLD,color.RED,color.END) #Le mostramos al usuario un mensaje de game over
            text(text_lose,1.0)
            exit() #Terminamos el código si se nos acaba la vida

def ataque(): #Declaramos que pasa si hay un enemigo
    global nivel
    text_enemigo=("¡Oh no! un enemigo ha aparecido\n") #Mostramos un mensaje de que ha aparecido un enemigo
    text(text_enemigo,0.05)
    if nivel==1:
        enem_r=random.randint(0,2)
        if enem_r==0:
            Diriol()
        if enem_r==1:
            Bokoblin()
        if enem_r==2:
            Baqus()
        if nivel==2:
            Uraelth()
    if nivel==2:
        enem_r=random.randint(0,5)
        if enem_r==0:
            Diriol()
        if enem_r==1:
            Bokoblin()
        if enem_r==2:
            Baqus()
        if enem_r==3:
            Sorrowvine()
        if enem_r==4:
            Warpfiend()
        if enem_r==5:
            Dreadbug()
        if nivel==3:
            Nightmask()
    if nivel==3:
        enem_r=random.randint(0,8)
        if enem_r==0:
            Diriol()
        if enem_r==1:
            Bokoblin()
        if enem_r==2:
            Baqus()
        if enem_r==3:
            Sorrowvine()
        if enem_r==4:
            Warpfiend()
        if enem_r==5:
            Dreadbug()
        if enem_r==6:
            Gallmorph()
        if enem_r==7:
            Slagghoul()
        if enem_r==8:
            Chaosseker()
        if nivel==4:
            Shadowling()
    if nivel==4:
        enem_r=random.randint(0,11)
        if enem_r==0:
            Diriol()
        if enem_r==1:
            Bokoblin()
        if enem_r==2:
            Baqus()
        if enem_r==3:
            Sorrowvine()
        if enem_r==4:
            Warpfiend()
        if enem_r==5:
            Dreadbug()
        if enem_r==6:
            Gallmorph()
        if enem_r==7:
            Slagghoul()
        if enem_r==8:
            Chaosseker()
        if enem_r==9:
            Slagbrood()
        if enem_r==10:
            Netherling()
        if enem_r==11:
            Acidtaur()
        if nivel==5:
            Infernosnare()



    menu() #Regresamos al menú

def menu(): #Creamos una función que nos permitira presentar el menú al principio de cada turno

    while True: #Iniciamos un loop dentro de el menú
        text_menu=("Que quieres hacer:\n") #Se le pregunta al usuario que quiere hacer
        text(text_menu,0.03)

        text_mover=("M - Moverte\n") #Se muestra la opción de moverse
        text(text_mover,0.03)

        text_stats=("S - Stats\n") #Se muestra la opción de ver stats
        text(text_stats,0.03)

        text_inv=("I - Inventario\n") #Se muestra la opción de ver inventario
        text(text_inv,0.03)

        opc=str(input()) #Tomamos la decisión del usuario

        while True:
            if opc=="S" or opc=="s": #Declaramos que pasa si escoge S
                stats() #Llamamos a la función de ver stats
                menu() #Regresamos al menú
            elif opc=="M" or opc=="m": #Declaramos que pasa si escoge M
                mover() #Llamamos a la función de moverse
                menu()
            elif opc=="I" or opc=="i": #Declaramos que pasa si escoge I
                inv() #Llamamos a la función de inventario
                menu()
            else: #Declaramos que pasa si el usuario no escoge bien
                text20=("Por favor escoge una de las opciones disponibles\n") #Se muestra un mensaje de que escoga bien
                text(text20,0.05)
                menu() #Llamamos al menú

def mover(): #Definimos la función del movimiento
    global dinero
    global co_x
    global co_y

    while True: #Creamos un loop para escoger una dirección

        text_movin=("A donde te quieres mover:\n") #Se le pregunta al usuario a donde se quiere mover 
        text(text_movin,0.03)

        text_norte=("W - Norte\n") #Le decimos que W es para norte
        text(text_norte,0.03)

        text_oeste=("A - Oeste\n") #Le decimos que A es para oeste
        text(text_oeste,0.03)

        text_sur=("S - Sur\n") #Le decimos que S es para sur
        text(text_sur,0.03)

        text_este=("D - Este\n") #Le decimos que D es para este
        text(text_este,0.03)

        dir=str(input()) #Tomamos la función de dirreción

        def text_dir():
            global co_x
            global co_y
            global velocidad
            if dir=="W" or dir=="w":
                co_y=co_y+velocidad
                text_mov=("Te has movido ",velocidad," cuadros al Norte \n") #Si el usuario escogio W le decimos que se movio, segun la velocidad, eso al norte
                text(text_mov,0.03)
                text_coord=("Coordenadas: ",co_x,",",co_y,'\n') #Se presenta su exp
                text(text_coord,0.03)

            if dir=="A" or dir=="a":
                co_x=co_x-velocidad
                text_mov=("Te has movido ",velocidad," cuadros al Oeste \n") #Si el usuario escogio A le decimos que se movio, segun la velocidad, eso al oeste
                text(text_mov,0.03)
                text_coord=("Coordenadas: ",co_x,",",co_y,'\n') #Se presenta su exp
                text(text_coord,0.03)

            if dir=="S" or dir=="s":
                co_y=co_y-velocidad
                text_mov=("Te has movido ",velocidad," cuadros al Sur \n") #Si el usuario escogio S le decimos que se movio, segun la velocidad, eso al sur
                text(text_mov,0.03)
                text_coord=("Coordenadas: ",co_x,",",co_y,'\n') #Se presenta su exp
                text(text_coord,0.03)

            if dir=="D" or dir=="d":
                co_x=co_x+velocidad
                text_mov=("Te has movido ",velocidad," cuadros al Este \n") #Si el usuario escogio D le decimos que se movio, segun la velocidad, eso al este
                text(text_mov,0.03)
                text_coord=("Coordenadas: ",co_x,",",co_y,'\n') #Se presenta su exp
                text(text_coord,0.03)


        if dir!= "W" and dir != "w" and dir != "A" and dir != "a" and dir != "S" and dir != "s" and dir != "D" and dir != "d": #Declaramos que pasa si el usuario no escoge la dirección correcta
            text_mov_cor=("Esa no es una direccion, escoge bien\n") #Le decimos que no es una dirección correcta
            text(text_mov_cor,0.03)
            continue #Reiniciamos el loop
        
        else: #Si el usuario escoge una direcciónn correcta
            text_dir()
            if co_x==150 and co_y==200:
                text_niña=("Oh una niñita,parece ser perdio su peluche\n")
                text(text_niña,0.03)

                if int(len(peluches))==1:
                    text_dar=("Quieres darle el peluche que compraste?\n")
                    text(text_dar,0.03)
                    while dar!="D" or dar!="d" or dar!="N" or dar!="n":
                        print("D - Darle el peluche")
                        print("N - No darle nada")
                        dar=input()
                        if dar=="D" or dar=="d":
                            peluches.remove("Peluche")
                            text_feliz=("Oh la niña se ve super alegre y parece ser te ha dado, un un lanzagranadas?, eehhh mejor no cuestiones, quien sabe por donde ha estado esa niña\n")
                            text(text_feliz,0.03)
                            granadas.append("Lanzagranadas")
                            break
                        if dar=="N" or dar=="n":
                            text_triste=("Mira nomás lo que hiciste, ahora la niña esta triste y llorando, te sientes feliz contigo?\n")
                            text(text_triste)
                            break
                        else:
                            text_ilegal=("No creo que eso sea legal\n")
                            text(text_ilegal,0.03)
                            continue
                else:
                    text_nada=("Mmm,no parece ser que tengas nada para darle, mejor regresar a explorar\n")
                    text(text_nada,0.03)
                    break
            else:
                turno=random.randint(0,3) #Generamos un número random
            #Declaramos que la variable sera un número integer random, de entre 0 a 3
            
                if turno==0: #Declaramos que pasa si el número random es 0
                    text_nada=("Vaya parece que no hay nada por aquí, oh pero si encontraste una moneda\n") #Le decimos al usuario que no hay nada alrededor
                    text(text_nada,0.03)
                    dinero= dinero + 1
                    menu() #LLamamos la función de el menú
                    
                if turno==1: #Declaramos que pasa si el número random es 1
                    ataque() #Si el número random es 1, llamamos a la función de ataque

                if turno==2: #Declaramos que pasa si el número random es 2
                    tienda()
            
                if turno==3: #Declaramos que pasa si el numero random es 3
                    obj() #Llamamos a la función de objeto
                    menu() #Regresamos al menú

def inv(): #Creamos una función para acceder al inventario
        text_inv=("Escoge que quieres usar de tu inventario\n") #Le decimos al usuario que aquí podra ver su inventario
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
 
        while True:
                
            if int(len(anillos))==0 and int(len(medallons))==0 and int(len(cascos))==0 and int(len(manzanas))==0 and int(len(espadas)) and int(len(pocions)) and int(len(botas)) and int(len(martillos)) and int(len(super_pocions)) and int(len(brazaletes)) and int(len(peluches)) and int(len()):
                text_nada_in=("Oh vaya, parece que no tienes nada en tu inventario\n")
                text(text_nada_in,0.03)
                break
            
            else:
                
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
        
                obj_inv=str(input())
            
                if obj_inv=="A" or obj_inv=="a":
                    if int(len(anillos))<=0:
                        text_n_a=("Ya no tienes aniilos disponibles,escoge algo más\n")
                        text(text_n_a,0.03)
                        continue

                    else:
                        if nivel==1 and fuerza>=20:
                            text_no_a=("Ya has llegado al limite de fuerza")
                            text(text_no_a,0.03)
                            continue
                        if nivel==2 and fuerza>=30:
                            text_no_a=("Ya has llegado al limite de fuerza")
                            text(text_no_a,0.03)
                            continue
                        if nivel==3 and fuerza>=40:
                            text_no_a=("Ya has llegado al limite de fuerza")
                            text(text_no_a,0.03)
                            continue
                        if nivel==4 and fuerza>=50:
                            text_no_a=("Ya has llegado al limite de fuerza")
                            text(text_no_a,0.03)
                            continue

                        else:
                            text_ainv=("Has obtenido 1 de fuerza\n")
                            text(text_ainv,0.03)
                            fuerza=fuerza+1
                            anillos.remove("Anillo de poder") #Metodo para remover objeto de una lista obtenido de https://uniwebsidad.com/libros/python/capitulo-7/metodos-de-eliminacion 
                            stats()
                            continue
                
                if obj_inv=="M" or obj_inv=="m":
                    if int(len(medallons))<=0:
                        text_n_m=("Ya no tienes medallones disponibles,escoge algo más\n")
                        text(text_n_m,0.03)
                        continue
                
                    else:
                        if nivel==1 and velocidad>=15:
                            text_no_m=("Ya has llegado al limite de velocidad")
                            text(text_no_m,0.03)
                            continue
                        if nivel==2 and velocidad>=25:
                            text_no_m=("Ya has llegado al limite de velocidad")
                            text(text_no_m,0.03)
                            continue
                        if nivel==3 and velocidad>=35:
                            text_no_m=("Ya has llegado al limite de velocidad")
                            text(text_no_m,0.03)
                            continue
                        if nivel==4 and velocidad>=45:
                            text_no_m=("Ya has llegado al limite de velocidad")
                            text(text_no_m,0.03)
                            continue

                        
                        else:
                            text_minv=("Has obtenido 1.5 de velocidad\n")
                            text(text_minv,0.03)
                            velocidad=velocidad+1.5
                            medallons.remove("Medallon de velocidad")
                            stats()
                            continue
                    
                if obj_inv=="C" or obj_inv=="c":
                    if int(len(cascos))<=0:
                        text_n_c=("Ya no tienes cascos disponibles,escoge algo más\n")
                        text(text_n_c,0.03)
                        continue
            
                    else:
                        if nivel==1 and fuerza>=20:
                            text_no_a=("Ya has llegado al limite de fuerza")
                            text(text_no_a,0.03)
                            continue
                        if nivel==2 and fuerza>=30:
                            text_no_a=("Ya has llegado al limite de fuerza")
                            text(text_no_a,0.03)
                            continue
                        if nivel==3 and fuerza>=40:
                            text_no_a=("Ya has llegado al limite de fuerza")
                            text(text_no_a,0.03)
                            continue
                        if nivel==4 and fuerza>=50:
                            text_no_a=("Ya has llegado al limite de fuerza")
                            text(text_no_a,0.03)
                            continue
                            
                        else:
                            text_cinv=("Has usado el casco, has obtenido 3.5 de fuerza, pero has perdido 4 de velocidad\n")
                            text(text_cinv,0.03)
                            fuerza=fuerza+3.5
                            velocidad=velocidad-4
                            cascos.remove("Casco encantado")
                            stats()
                            continue
                    
                if obj_inv=="W" or obj_inv=="w":
                    if int(len(manzanas))<=0:
                        text_n_ma=("Ya no tienes manzanas disponibles,escoge algo más\n")
                        text(text_n_ma,0.03)
                        continue
                
                    else:
                        if nivel==1 and vida>=20:
                            text_no_p=("Ya has llegado al limite de vida\n")
                            text(text_no_p,0.03)
                            continue

                        elif nivel==2 and vida>=45:
                            text_no_p=("Ya has llegado al limite de vida\n")
                            text(text_no_p,0.03)
                            continue
                        elif nivel==3 and vida>=65:
                            text_no_p=("Ya has llegado al limite de vida\n")
                            text(text_no_p,0.03)
                            continue
                        elif nivel==4 and vida>=90:
                            text_no_sp=("Ya has llegado al limite de vida\n")
                            text(text_no_sp,0.03)
                            continue
                        else:
                            text_cinv=("Has usado una manzana, has obtenido 1 de vida\n")
                            text(text_cinv,0.03)
                            vida=vida+1 
                            manzanas.remove("Manzana")
                            stats()
                            continue
#------OBJ NIVEL 1                    
                if int(len(espadas))==1 and obj_inv=="E" or obj_inv=="e":
                    text_a=("G - Guardar\n")
                    text(text_a,0.03)
                    text_m=("A - Agarrrar\n")
                    text(text_m,0.03)
                    text_c=("E - Escoger algo más\n")
                    text(text_c,0.03)
                    
                    while True:
                        opc_esp=str(input())
                        if opc_esp=="G" or opc_esp=="g":
                            text_g_espada=("Has guardado tu espada\n")
                            text(text_g_espada,0.03)
                            fuerza=fuerza-5
                            stats()
                            continue
                        if opc_esp=="A" or opc_esp=="a":
                            if int(len(martillos))==1:
                                text_a_espada=("Has escogido tu espada\n")
                                text(text_a_espada,0.03)
                                fuerza=fuerza-7
                                fuerza=fuerza+5
                                stats()
                                continue
                            if int(len(aks))==1:
                                text_a_espada=("Has escogido tu espada\n")
                                text(text_a_espada,0.03)
                                fuerza=fuerza-10
                                fuerza=fuerza+5
                                stats()
                                continue
                            if int(len(cangureras))==1:
                                text_a_espada=("Has escogido tu espada\n")
                                text(text_a_espada,0.03)
                                fuerza=fuerza-15
                                fuerza=fuerza+5
                                stats()
                                continue
                            elif int(len(martillos))==1 and int(len(aks))==1:
                                text_a_espada=("Has escogido tu espada\n")
                                text(text_a_espada,0.03)
                                fuerza=fuerza-10
                                fuerza=fuerza-7
                                fuerza=fuerza+5
                                stats()
                                continue
                            elif int(len(martillos))==1 and int(len(cangureras))==1:
                                text_a_espada=("Has escogido tu espada\n")
                                text(text_a_espada,0.03)
                                fuerza=fuerza-15
                                fuerza=fuerza-7
                                fuerza=fuerza+5
                                stats()
                                continue
                            elif int(len(cangureras))==1 and int(len(aks))==1:
                                text_a_espada=("Has escogido tu espada\n")
                                text(text_a_espada,0.03)
                                fuerza=fuerza-10
                                fuerza=fuerza-15
                                fuerza=fuerza+5
                                stats()
                                continue
                            elif int(len(martillos))==1 and int(len(aks))==1 and int(len(martillos))==1:
                                text_a_espada=("Has escogido tu espada\n")
                                text(text_a_espada,0.03)
                                fuerza=fuerza-15
                                fuerza=fuerza-10
                                fuerza=fuerza-7
                                fuerza=fuerza+5
                                stats()
                                continue
                            else:
                                text_n_espada=("Has escogido tu espada\n")
                                text(text_n_espada,0.03)
                                fuerza=fuerza+5
                                stats()
                                continue
                        if opc_esp=="E" or opc_esp=="e":
                            text_e=("Vuelve a tu inventario y escoge algo más")
                            text(text_e,0.03)
                            break
                        else:
                            text_no=("Esa no es una opción valida")
                            text(text_no,0.03)
                            continue
                                
                if int(len(pocions))>0 and obj_inv=="P" or obj_inv=="p":
                    if int(len(pocions))<=0:
                        text_n_p=("Ya no tienes pociones disponibles,escoge algo más\n")
                        text(text_n_p,0.03)
                        continue
                
                    else:
                        if nivel==1 and vida>=20:
                            text_no_p=("Ya has llegado al limite de vida\n")
                            text(text_no_p,0.03)
                            continue

                        elif nivel==2 and vida>=45:
                            text_no_p=("Ya has llegado al limite de vida\n")
                            text(text_no_p,0.03)
                            continue
                        elif nivel==3 and vida>=65:
                            text_no_p=("Ya has llegado al limite de vida\n")
                            text(text_no_p,0.03)
                            continue
                        elif nivel==4 and vida>=90:
                            text_no_sp=("Ya has llegado al limite de vida\n")
                            text(text_no_sp,0.03)
                            continue
                        else:
                            text_cinv=("Has usado una poción, has obtenido 3 de vida\n")
                            text(text_cinv,0.03)
                            vida=vida+3  
                            pocions.remove("Pocion")
                            stats()
                            continue
                    
                if int(len(botas))==1 and obj_inv=="B" or obj_inv=="b":         
                    text_a=("G - Guardar\n")
                    text(text_a,0.03)
                    text_m=("A - Agarrrar\n")
                    text(text_m,0.03)
                    text_c=("E - Escoger algo más\n")
                    text(text_c,0.03)
                    
                    while True:
                        opc_bot=str(input())
                        if opc_bot=="G" or opc_bot=="g":
                            text_g_botas=("Has guardado tus botas\n")
                            text(text_g_botas,0.03)
                            velocidad=velocidad-4
                            stats()
                            continue
                        if opc_bot=="A" or opc_bot=="a":
                            if int(len(brazaletes))==1:
                                text_a_botas=("Has escogido tus botas\n")
                                text(text_a_botas,0.03)
                                velocidad=velocidad-6
                                velocidad=velocidad+4
                                stats()
                                continue
                            if int(len(sombreros))==1:
                                text_a_botas=("Has escogido tus botas\n")
                                text(text_a_botas,0.03)
                                velocidad=velocidad-8
                                velocidad=velocidad+4
                                stats()
                                continue
                            if int(len(rayos))==1:
                                text_a_botas=("Has escogido tus botas\n")
                                text(text_a_botas,0.03)
                                velocidad=velocidad-15
                                velocidad=velocidad+4
                                stats()
                                continue
                            elif int(len(brazaletes))==1 and int(len(sombreros))==1:
                                text_a_botas=("Has escogido tus botas\n")
                                text(text_a_botas,0.03)
                                velocidad=velocidad-8
                                velocidad=velocidad-6
                                velocidad=velocidad+4
                                stats()
                                continue
                            elif int(len(brazaletes))==1 and int(len(rayos))==1:
                                text_a_botas=("Has escogido tus botas\n")
                                text(text_a_botas,0.03)
                                velocidad=velocidad-8
                                velocidad=velocidad-15
                                velocidad=velocidad+4
                                stats()
                                continue
                            elif int(len(rayos))==1 and int(len(sombreros))==1:
                                text_a_botas=("Has escogido tus botas\n")
                                text(text_a_botas,0.03)
                                velocidad=velocidad-15
                                velocidad=velocidad-8
                                velocidad=velocidad+4
                                stats()
                                continue
                            elif int(len(brazaletes)) and int(len(rayos))==1 and int(len(sombreros))==1:
                                text_a_botas=("Has escogido tus botas\n")
                                text(text_a_botas,0.03)
                                velocidad=velocidad-15
                                velocidad=velocidad-8
                                velocidad=velocidad-6
                                velocidad=velocidad+4
                                stats()
                                continue
                            else:
                                text_n_botas=("Has escogido tus botas\n")
                                text(text_n_botas,0.03)
                                velocidad=velocidad+4
                                continue
                            
                        if opc_bot=="E" or opc_bot=="e":
                            text_e=("Vuelve a tu inventario y escoge algo más")
                            text(text_e,0.03)
                            continue
                        else:
                            text_no=("Esa no es una opción valida")
                            text(text_no,0.03)
                            continue
#-----------OBJ NIVEL 2
                if int(len(martillos))==1 and obj_inv=="MA" or obj_inv=="ma":
                    text_a=("G - Guardar\n")
                    text(text_a,0.03)
                    text_m=("A - Agarrrar\n")
                    text(text_m,0.03)
                    text_c=("E - Escoger algo más\n")
                    text(text_c,0.03)
                    
                    while True:
                        opc_m=str(input())
                        if opc_m=="G" or opc_m=="g":
                            text_g_martillo=("Has guardado tu martillo\n")
                            text(text_g_martillo,0.03)
                            fuerza=fuerza-7
                            stats()
                            continue
                        if opc_m=="A" or opc_m=="a":
                            if int(len(espadas))==1:
                                text_a_martillo=("Has escogido tu martillo\n")
                                text(text_a_martillo,0.03)
                                fuerza=fuerza-5
                                fuerza=fuerza+7
                                stats()
                                continue
                            if int(len(aks))==1:
                                text_a_martillo=("Has escogido tu martillo\n")
                                text(text_a_martillo,0.03)
                                fuerza=fuerza-10
                                fuerza=fuerza+7
                                stats()
                                continue
                            if int(len(cangureras))==1:
                                text_a_martillo=("Has escogido tu martillo\n")
                                text(text_a_martillo,0.03)
                                fuerza=fuerza-15
                                fuerza=fuerza+7
                                stats()
                                continue
                            elif int(len(espadas))==1 and int(len(aks))==1:
                                text_a_martillo=("Has escogido tu martillo\n")
                                text(text_a_martillo,0.03)
                                fuerza=fuerza-10
                                fuerza=fuerza-5
                                fuerza=fuerza+7
                                stats()
                                break
                            elif int(len(espadas))==1 and int(len(cangureras))==1:
                                text_a_martillo=("Has escogido tu martillo\n")
                                text(text_a_martillo,0.03)
                                fuerza=fuerza-15
                                fuerza=fuerza-5
                                fuerza=fuerza+7
                                stats()
                                break
                            elif int(len(cangureras))==1 and int(len(aks))==1:
                                text_a_martillo=("Has escogido tu martillo\n")
                                text(text_a_martillo,0.03)
                                fuerza=fuerza-15
                                fuerza=fuerza-10
                                fuerza=fuerza+7
                                stats()
                                break
                            elif int(len(cangureras))==1 and int(len(aks))==1 and int(len(espadas))==1:
                                text_a_martillo=("Has escogido tu martillo\n")
                                text(text_a_martillo,0.03)
                                fuerza=fuerza-15
                                fuerza=fuerza-10
                                fuerza=fuerza-5
                                fuerza=fuerza+7
                                stats()
                                continue
                            else:
                                text_n_martillo=("Has escogido tu martillo\n")
                                text(text_n_martillo,0.03)
                                fuerza=fuerza+7
                                stats()
                                continue
                        if opc_m=="E" or opc_m=="e":
                            text_e=("Vuelve a tu inventario y escoge algo más")
                            text(text_e,0.03)
                            break
                        else:
                            text_no=("Esa no es una opción valida")
                            text(text_no,0.03)
                            continue
                                
                if int(len(super_pocions))>0 and (obj_inv=="SP" or obj_inv=="sp"):
                    if int(len(super_pocions))<=0:
                        text_n_sp=("Ya no tienes super pociones disponibles,escoge algo más\n")
                        text(text_n_sp,0.03)
                        continue
                
                    else:
                        if nivel==1 and vida>=20:
                            text_no_sp=("Ya has llegado al limite de vida\n")
                            text(text_no_sp,0.03)
                            continue

                        elif nivel==2 and vida>=45:
                            text_no_sp=("Ya has llegado al limite de vida\n")
                            text(text_no_sp,0.03)
                            continue

                        elif nivel==3 and vida>=65:
                            text_no_sp=("Ya has llegado al limite de vida\n")
                            text(text_no_sp,0.03)
                            continue

                        elif nivel==4 and vida>=90:
                            text_no_sp=("Ya has llegado al limite de vida\n")
                            text(text_no_sp,0.03)
                            continue

                        else:
                            text_cinv=("Has usado una super poción, has obtenido 5 de vida\n")
                            text(text_cinv,0.03)
                            vida=vida+5 
                            super_pocions.remove("Super Pocion")
                            stats()
                            continue
                    
                if int(len(brazaletes))==1 and obj_inv=="BR" or obj_inv=="br":         
                    text_a=("G - Guardar\n")
                    text(text_a,0.03)
                    text_m=("A - Agarrrar\n")
                    text(text_m,0.03)
                    text_c=("E - Escoger algo más\n")
                    text(text_c,0.03)
                    
                    while True:
                        opc_br=str(input())
                        if opc_br=="G" or opc_br=="g":
                            text_g_bra=("Has guardado tus brazaletes\n")
                            text(text_g_bra,0.03)
                            velocidad=velocidad-6
                            stats()
                            continue
                        if opc_br=="A" or opc_br=="a":
                            if int(len(botas))==1:
                                text_a_bra=("Has escogido tus brazaletes\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-4
                                velocidad=velocidad+6
                                stats()
                                continue
                            if int(len(sombreros))==1:
                                text_a_bra=("Has escogido tus brazaletes\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-8
                                velocidad=velocidad+6
                                stats()
                                continue
                            if int(len(rayos))==1:
                                text_a_bra=("Has escogido tus brazaletes\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-15
                                velocidad=velocidad+6
                                stats()
                                continue
                            elif int(len(botas))==1 and int(len(sombreros))==1:
                                text_a_bra=("Has escogido tus brazaletes\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-8
                                velocidad=velocidad-4
                                velocidad=velocidad+6
                                stats()
                                continue
                            elif int(len(botas))==1 and int(len(rayos))==1:
                                text_a_bra=("Has escogido tus brazaletes\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-15
                                velocidad=velocidad-4
                                velocidad=velocidad+6
                                stats()
                                continue
                            elif int(len(sombreros))==1 and int(len(rayos))==1:
                                text_a_bra=("Has escogido tus brazaletes\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-15
                                velocidad=velocidad-8
                                velocidad=velocidad+6
                                stats()
                                continue
                            elif int(len(sombreros))==1 and int(len(sombreros)) and int(len(rayos))==1:
                                text_a_bra=("Has escogido tus brazaletes\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-15
                                velocidad=velocidad-8
                                velocidad=velocidad-4
                                velocidad=velocidad+6
                                stats()
                                continue
                            else:
                                text_a_bra=("Has escogido tus brazaletes\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad+6
                                continue
                            
                        if opc_br=="E" or opc_br=="e":
                            text_e=("Vuelve a tu inventario y escoge algo más")
                            text(text_e,0.03)
                            continue
                        else:
                            text_no=("Esa no es una opción valida")
                            text(text_no,0.03)
                            continue      
#----------OBJ NIVEL 3
                if int(len(peluches))==1 and obj_inv=="PE" or obj_inv=="pe":
                    text_pel=("Es un peluche bonito, pero no puedes hacer mucho con el\n")
                    text(text_pel,0.03)

                if int(len(sombreros))>0 and (obj_inv=="S" or obj_inv=="s"):
                    text_a=("G - Guardar\n")
                    text(text_a,0.03)
                    text_m=("A - Agarrrar\n")
                    text(text_m,0.03)
                    text_c=("E - Escoger algo más\n")
                    text(text_c,0.03)
                    
                    while True:
                        opc_som=str(input())
                        if opc_som=="G" or opc_som=="g":
                            text_g_bra=("Has guardado tu sombrero\n")
                            text(text_g_bra,0.03)
                            velocidad=velocidad-8
                            stats()
                            continue
                        if opc_som=="A" or opc_som=="a":
                            if int(len(botas))==1:
                                text_a_bra=("Has escogido tu sombrero\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-4
                                velocidad=velocidad+8
                                stats()
                                continue
                            if int(len(brazaletes))==1:
                                text_a_bra=("Has escogido tu sombrero\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-6
                                velocidad=velocidad+8
                                stats()
                                continue
                            if int(len(rayos))==1:
                                text_a_bra=("Has escogido tu sombrero\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-15
                                velocidad=velocidad+8
                                stats()
                                continue
                            elif int(len(botas))==1 and int(len(brazaletes))==1:
                                text_a_bra=("Has escogido tu sombrero\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-6
                                velocidad=velocidad-4
                                velocidad=velocidad+8
                                stats()
                                continue
                            elif int(len(botas))==1 and int(len(rayos))==1:
                                text_a_bra=("Has escogido tu sombrero\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-15
                                velocidad=velocidad-4
                                velocidad=velocidad+8
                                stats()
                                continue
                            elif int(len(brazaletes))==1 and int(len(rayos))==1:
                                text_a_bra=("Has escogido tu sombrero\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-15
                                velocidad=velocidad-6
                                velocidad=velocidad+8
                                stats()
                                continue
                            elif int(len(sombreros))==1 and int(len(brazaletes)) and int(len(rayos))==1:
                                text_a_bra=("Has escogido tu sombrero\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-15
                                velocidad=velocidad-6
                                velocidad=velocidad-4
                                velocidad=velocidad+8
                                stats()
                                continue
                            else:
                                text_a_bra=("Has escogido tu sombrero\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad+8
                                continue
                            
                        if opc_som=="E" or opc_som=="e":
                            text_e=("Vuelve a tu inventario y escoge algo más")
                            text(text_e,0.03)
                            continue
                        else:
                            text_no=("Esa no es una opción valida")
                            text(text_no,0.03)
                            continue      
                    
                if int(len(aks))==1 and obj_inv=="AK" or obj_inv=="ak":         
                    text_a=("G - Guardar\n")
                    text(text_a,0.03)
                    text_m=("A - Agarrrar\n")
                    text(text_m,0.03)
                    text_c=("E - Escoger algo más\n")
                    text(text_c,0.03)
                    
                    while True:
                        opc_ak=str(input())
                        if opc_ak=="G" or opc_ak=="g":
                            text_g_ak=("Has guardado tu AK-47\n")
                            text(text_g_ak,0.03)
                            fuerza=fuerza-10
                            stats()
                            continue
                        if opc_ak=="A" or opc_ak=="a":
                            if int(len(martillos))==1:
                                text_a_ak=("Has escogido tu AK-47\n")
                                text(text_a_ak,0.03)
                                fuerza=fuerza-7
                                fuerza=fuerza+10
                                stats()
                                continue
                            if int(len(espadas))==1:
                                text_a_ak=("Has escogido tu AK-47\n")
                                text(text_a_ak,0.03)
                                fuerza=fuerza-5
                                fuerza=fuerza+10
                                stats()
                                continue
                            if int(len(cangureras))==1:
                                text_a_ak=("Has escogido tu AK-47\n")
                                text(text_a_ak,0.03)
                                fuerza=fuerza-15
                                fuerza=fuerza+10
                                stats()
                                continue
                            elif int(len(espadas))==1 and int(len(martillos))==1:
                                text_a_ak=("Has escogido tu AK-47\n")
                                text(text_a_ak,0.03)
                                fuerza=fuerza-7
                                fuerza=fuerza-5
                                fuerza=fuerza+10
                                stats()
                                continue
                            elif int(len(espadas))==1 and int(len(cangureras))==1:
                                text_a_ak=("Has escogido tu AK-47\n")
                                text(text_a_ak,0.03)
                                fuerza=fuerza-15
                                fuerza=fuerza-5
                                fuerza=fuerza+10
                                stats()
                                continue
                            elif int(len(cangureras))==1 and int(len(martillos))==1:
                                text_a_ak=("Has escogido tu AK-47\n")
                                text(text_a_ak,0.03)
                                fuerza=fuerza-15
                                fuerza=fuerza-7
                                fuerza=fuerza+10
                                stats()
                                continue
                            elif int(len(espadas))==1 and int(len(martillos))==1 and int(len(espadas))==1:
                                text_a_ak=("Has escogido tu AK-47\n")
                                text(text_a_ak,0.03)
                                fuerza=fuerza-15
                                fuerza=fuerza-7
                                fuerza=fuerza-5
                                fuerza=fuerza+10
                                stats()
                                continue
                            else:
                                text_a_ak=("Has escogido tu AK-47\n")
                                text(text_a_ak,0.03)
                                fuerza=fuerza+10
                                continue
                            
                        if opc_ak=="E" or opc_ak=="e":
                            text_e=("Vuelve a tu inventario y escoge algo más")
                            text(text_e,0.03)
                            continue
                        else:
                            text_no=("Esa no es una opción valida")
                            text(text_no,0.03)
                            continue      
                          
               
#-----------OBJ NIVEL 4
                if int(len(cangureras))==1 and obj_inv=="MA" or obj_inv=="ma":
                    text_a=("G - Guardar\n")
                    text(text_a,0.03)
                    text_m=("A - Agarrrar\n")
                    text(text_m,0.03)
                    text_c=("E - Escoger algo más\n")
                    text(text_c,0.03)
                    
                    while True:
                        opc_bat=str(input())
                        if opc_bat=="G" or opc_bat=="g":
                            text_g_bat=("Has guardado tu baticangurera\n")
                            text(text_g_bat,0.03)
                            fuerza=fuerza-15
                            stats()
                            continue
                        if opc_bat=="A" or opc_bat=="a":
                            if int(len(espadas))==1:
                                text_a_bat=("Has escogido tu baticangurera\n")
                                text(text_a_bat,0.03)
                                fuerza=fuerza-5
                                fuerza=fuerza+15
                                stats()
                                continue
                            if int(len(martillos))==1:
                                text_a_bat=("Has escogido tu baticangurera\n")
                                text(text_a_bat,0.03)
                                fuerza=fuerza-7
                                fuerza=fuerza+15
                                stats()
                                continue
                            if int(len(aks))==1:
                                text_a_bat=("Has escogido tu baticangurera\n")
                                text(text_a_bat,0.03)
                                fuerza=fuerza-10
                                fuerza=fuerza+15
                                stats()
                                continue
                            elif int(len(espadas))==1 and int(len(aks))==1:
                                text_a_bat=("Has escogido tu baticangurera\n")
                                text(text_a_bat,0.03)
                                fuerza=fuerza-10
                                fuerza=fuerza-5
                                fuerza=fuerza+15
                                stats()
                                continue
                            elif int(len(espadas))==1 and int(len(martillos))==1:
                                text_a_bat=("Has escogido tu baticangurera\n")
                                text(text_a_bat,0.03)
                                fuerza=fuerza-7
                                fuerza=fuerza-5
                                fuerza=fuerza+15
                                stats()
                                continue
                            elif int(len(martillos))==1 and int(len(aks))==1:
                                text_a_bat=("Has escogido tu baticangurera\n")
                                text(text_a_bat,0.03)
                                fuerza=fuerza-10
                                fuerza=fuerza-7
                                fuerza=fuerza+15
                                stats()
                                continue
                            elif int(len(espadas))==1 and int(len(martillos))==1 and int(len(aks))==1:
                                text_a_bat=("Has escogido tu baticangurera\n")
                                text(text_a_bat,0.03)
                                fuerza=fuerza-10
                                fuerza=fuerza-7
                                fuerza=fuerza-5
                                fuerza=fuerza+15
                                stats()
                                continue
                            else:
                                text_n_bat=("Has escogido tu baticangurera\n")
                                text(text_n_bat,0.03)
                                fuerza=fuerza+15
                                stats()
                                continue
                        if opc_bat=="E" or opc_bat=="e":
                            text_e=("Vuelve a tu inventario y escoge algo más")
                            text(text_e,0.03)
                            break
                        else:
                            text_no=("Esa no es una opción valida")
                            text(text_no,0.03)
                            continue
                
                if int(len(rayos))>0 and (obj_inv=="R" or obj_inv=="r"):
                    text_a=("G - Guardar\n")
                    text(text_a,0.03)
                    text_m=("A - Agarrrar\n")
                    text(text_m,0.03)
                    text_c=("E - Escoger algo más\n")
                    text(text_c,0.03)
                    
                    while True:
                        opc_ray=str(input())
                        if opc_ray=="G" or opc_ray=="g":
                            text_g_bra=("Has guardado tu rayo\n")
                            text(text_g_bra,0.03)
                            velocidad=velocidad-15
                            stats()
                            continue
                        if opc_ray=="A" or opc_ray=="a":
                            if int(len(botas))==1:
                                text_a_bra=("Has escogido tu rayo\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-4
                                velocidad=velocidad+15
                                stats()
                                continue
                            if int(len(brazaletes))==1:
                                text_a_bra=("Has escogido tu rayo\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-6
                                velocidad=velocidad+15
                                stats()
                                continue
                            if int(len(sombreros))==1:
                                text_a_bra=("Has escogido tu rayo\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-8
                                velocidad=velocidad+15
                                stats()
                                continue
                            elif int(len(botas))==1 and int(len(brazaletes))==1:
                                text_a_bra=("Has escogido tu rayo\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-6
                                velocidad=velocidad-4
                                velocidad=velocidad+15
                                stats()
                                continue
                            elif int(len(botas))==1 and int(len(sombreros))==1:
                                text_a_bra=("Has escogido tu rayo\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-8
                                velocidad=velocidad-4
                                velocidad=velocidad+15
                                stats()
                                continue
                            elif int(len(brazaletes))==1 and int(len(sombreros))==1:
                                text_a_bra=("Has escogido tu rayo\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-8
                                velocidad=velocidad-6
                                velocidad=velocidad+15
                                stats()
                                continue
                            elif int(len(sombreros))==1 and int(len(brazaletes)) and int(len(sombreros))==1:
                                text_a_bra=("Has escogido tu rayo\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad-8
                                velocidad=velocidad-6
                                velocidad=velocidad-4
                                velocidad=velocidad+15
                                stats()
                                continue
                            else:
                                text_a_bra=("Has escogido tu rayo\n")
                                text(text_a_bra,0.03)
                                velocidad=velocidad+15
                                continue
                            
                        if opc_ray=="E" or opc_ray=="e":
                            text_e=("Vuelve a tu inventario y escoge algo más")
                            text(text_e,0.03)
                            continue
                        else:
                            text_no=("Esa no es una opción valida")
                            text(text_no,0.03)
                            continue     

                if int(len(afros))==1 and (obj_inv=="AF" or obj_inv=="af"):
                    if int(len(afros))<=0:
                        text_n_sp=("Ya no tienes afros disponibles,escoge algo más\n")
                        text(text_n_sp,0.03)
                        continue
                    else:
                        if nivel==1 and vida>=20:
                            text_no_sp=("Ya has llegado al limite de vida\n")
                            text(text_no_sp,0.03)
                            continue

                        elif nivel==2 and vida>=45:
                            text_no_sp=("Ya has llegado al limite de vida\n")
                            text(text_no_sp,0.03)
                            continue

                        elif nivel==3 and vida>=65:
                            text_no_sp=("Ya has llegado al limite de vida\n")
                            text(text_no_sp,0.03)
                            continue

                        elif nivel==4 and vida>=90:
                            text_no_sp=("Ya has llegado al limite de vida\n")
                            text(text_no_sp,0.03)
                            continue

                        else:
                            text_cinv=("Te has puesto un afro, has obtenido 12 de vida\n")
                            text(text_cinv,0.03)
                            vida=vida+12
                            afros.remove("Afro")
                            stats()
                            continue    

                if obj_inv=="S" or obj_inv=="s":
                    text_salir=("Regresa a tu aventura\n")
                    text(text_salir,0.03)
                    break

                else:
                    text_bien=("Disculpa pero no tienes eso en tu inventario, escoge algo más\n")
                    text(text_bien,0.03)
                    continue

def obj(): #Creamos una función que genera objetos random
    obj=random.randint(0,3) 
    global invent
    if obj==0:
        text_anillopoder=("¡HAS ENCONTRADO UN ANILLO DE PODER!, usalo con sabiduría\n")
        text(text_anillopoder,0.03)
        anillos.append('Anillo de poder')

    if obj==1:
        text_medallonvida=("¡HAS ENCONTRADO UN MEDALLON DE VELOCIDAD!, usalo con sabiduría\n")
        text(text_medallonvida,0.03)
        medallons.append('Medallon de velocidad')

    if obj==2:
        text_cascoencantado=("Has encontrado un casco encantado, te dice que ofrece poder, pero cuidado, que tiene magia oscura\n")
        text(text_cascoencantado,0.03)
        cascos.append('Casco encantado')

    if obj==3:
        text_pocion=("¡HAS ENCONTRADO UNA MANZANA!, yummy\n")
        text(text_pocion,0.03)
        manzanas.append('Manzana')
        
def tienda():
    text_pueblo=("Un pueblo,parece ser puedes obtener cosas aquí\n") #Si el número es 2, aparece un pueblo en el camino
    text(text_pueblo,0.03)
    text_bien=("Bienvenido aventurero, esto hay en la tienda hoy\n")
    text(text_bien,0.03)
    global espadas
    global manzanas
    global botas
    global dinero
    global martillos
    global super_pocions
    global brazaletes
    global nivel
#---------------------FUNCIONES PARA TIENDA
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


    def op_tien_1():
        global dinero
        while True:
            text_dinero=("Dinero: ",dinero,'\n')
            text(text_dinero,0.05)
            op_store=str(input())
            if op_store=="EF" or op_store=="ef":
                if dinero>=10:
                    text_esp_inv=("La espada poderosa se ha agregado a tu inventario\n")
                    text(text_esp_inv,0.03)
                    espadas.append("Espada de fuego")
                    dinero=dinero-10
                    continue
                            
                elif int(len(espadas))==1:
                    text_esp_full=("Ya tienes esta espada en tu inventario, porque no intentas escoger algo más\n")
                    text(text_esp_full,0.03)
                    continue
                            
                if dinero<10:
                    text_falta=("Lo siento no tienes el dinero necesario\n")
                    text(text_falta,0.03)
                    continue
                            
            if op_store=="P" or op_store=="p":
                if dinero>=2:
                    text_p_inv=("Has comprado una pocion, se ha guardado en tu inventario\n")
                    text(text_p_inv,0.03)
                    pocions.append("Pocion")
                    dinero=dinero-2
                    continue
                            
                elif int(len(pocions))==5:
                    text_p_full=("Ya tienes suficiente pociones no crees?\n")
                    text(text_p_full,0.03)
                    continue
                            
                if dinero<2:
                    text_falta=("Lo siento no tienes el dinero necesario\n")
                    text(text_falta,0.03)
                    continue
                        
            if op_store=="BF" or op_store=="bf":
                if dinero>=5:
                    text_b_inv=("Las botas flameantes se han agregado a tu inventario\n")
                    text(text_b_inv,0.03)
                    botas.append("Botas flameantes")
                    dinero=dinero-5
                    continue
                            
                elif int(len(botas))==1:
                    text_bot_full=("Ya tienes estas botas en tu inventario, porque no intentas escoger algo más\n")
                    text(text_bot_full,0.03)
                    continue
                            
                if dinero<5:
                    text_falta=("Lo siento no tienes el dinero necesario\n")
                    text(text_falta,0.03)
                    continue

            if op_store=="S" or op_store=="s":
                text_salir=("Veamos que más hay\n")
                text(text_salir,0.03)
                break

            else:
                text_bien=("Disculpa pero eso no esta disponible, escoge algo más\n")
                text(text_bien,0.03)
                continue 

    def op_tien_2():
        global dinero
        while True:
            text_dinero=("Dinero: ",dinero,'\n')
            text(text_dinero,0.05)
            op_store=str(input())
            if op_store=="MT" or op_store=="mt":
                    if dinero>=15:
                        text_esp_inv=("El martillo de trueno se ha agregado a tu inventario\n")
                        text(text_esp_inv,0.03)
                        martillos.append("Martillo de trueno")
                        dinero=dinero-15
                        continue
                    elif int(len(martillos))==1:
                        text_esp_full=("Ya tienes este martillo en tu inventario, porque no intentas escoger algo más\n")
                        text(text_esp_full,0.03)
                        continue
                    if dinero<15:
                        text_falta=("Lo siento no tienes el dinero necesario\n")
                        text(text_falta,0.03)
                        continue
                            
            if op_store=="SP" or op_store=="sp":
                    if dinero>=5:
                        text_p_inv=("Has comprado una super pocion, se ha guardado en tu inventario\n")
                        text(text_p_inv,0.03)
                        super_pocions.append("Super Pocion")
                        dinero=dinero-2
                        continue
                    elif int(len(super_pocions))==3:
                        text_p_full=("Ya tienes suficiente super pociones no crees?\n")
                        text(text_p_full,0.03)
                        continue
                    if dinero<5:
                        text_falta=("Lo siento no tienes el dinero necesario\n")
                        text(text_falta,0.03)
                        continue
                        
            if op_store=="BR" or op_store=="br":
                    if dinero>=10:
                        text_b_inv=("El brazalete de relampago se ha agregado a tu inventario\n")
                        text(text_b_inv,0.03)
                        brazaletes.append("Brazalete de relampago")
                        dinero=dinero-10
                        continue
                    elif int(len(brazaletes))==1:
                        text_bot_full=("Ya tienes este brazalete en tu inventario, porque no intentas escoger algo más\n")
                        text(text_bot_full,0.03)
                        continue
                    if dinero<10:
                        text_falta=("Lo siento no tienes el dinero necesario\n")
                        text(text_falta,0.03)
                        continue

            if op_store=="S" or op_store=="s":
                text_salir=("Veamos que más hay\n")
                text(text_salir,0.03)
                break

            else:
                text_bien=("Disculpa pero eso no esta disponible, escoge algo más\n")
                text(text_bien,0.03)
                continue

    def op_tien_3():
        while True:
            text_dinero=("Dinero: ",dinero,'\n')
            text(text_dinero,0.05)
            op_store=str(input())

            if op_store=="PE" or op_store=="pe":
                if dinero>=25:
                    text_esp_inv=("El peluche se ha agregado a tu inventario\n")
                    text(text_esp_inv,0.03)
                    peluches.append("Peluche")
                    dinero=dinero-20
                    continue
                elif int(len(peluches))==1:
                    text_esp_full=("Ya tienes este peluche en tu inventario, porque no intentas escoger algo más\n")
                    text(text_esp_full,0.03)
                    continue
                if dinero<20:
                    text_falta=("Lo siento no tienes el dinero necesario\n")
                    text(text_falta,0.03)
                    continue
                            
            if op_store=="SO" or op_store=="so":
                if dinero>=25:
                    text_p_inv=("Has comprado un sombrero, se ha guardado en tu inventario, te ves fiu fiu\n")
                    text(text_p_inv,0.03)
                    sombreros.append("Sombrero")
                    dinero=dinero-25
                    continue

                elif int(len(sombreros))==3:
                    text_p_full=("Ya tienes suficientes sombreros no crees?\n")
                    text(text_p_full,0.03)
                    continue

                if dinero<25:
                    text_falta=("Lo siento no tienes el dinero necesario\n")
                    text(text_falta,0.03)
                    continue
                        
                if op_store=="A" or op_store=="a":
                    if dinero>=45:
                        text_b_inv=("El AK-47 se ha agregado a tu inventario\n")
                        text(text_b_inv,0.03)
                        aks.append("AK-47")
                        dinero=dinero-10
                        continue
                    elif int(len(aks))==1:
                        text_bot_full=("Ya tienes este AK-47, porque no intentas escoger algo más\n")
                        text(text_bot_full,0.03)
                        continue
                    if dinero<45:
                        text_falta=("Lo siento no tienes el dinero necesario\n")
                        text(text_falta,0.03)
                        continue
                if op_store=="S" or op_store=="s":
                    text_salir=("Veamos que más hay\n")
                    text(text_salir,0.03)
                    break
                else:
                    text_bien=("Disculpa pero eso no esta disponible, escoge algo más\n")
                    text(text_bien,0.03)
                    continue

    def op_tien_4():
        while True:
            text_dinero=("Dinero: ",dinero,'\n')
            text(text_dinero,0.05)
            op_store=str(input())
            if op_store=="C" or op_store=="c":
                if dinero>=30:
                    text_esp_inv=("La baticangurera se ha agregado a tu inventario,ahora estas bati-vestido\n")
                    text(text_esp_inv,0.03)
                    cangureras.append("Cangurera")
                    dinero=dinero-30
                    continue
                elif int(len(cangureras))==1:
                    text_esp_full=("Ya tienes este baticinturon en tu inventario, porque no intentas escoger algo más\n")
                    text(text_esp_full,0.03)
                    continue
                if dinero<30:
                    text_falta=("Lo siento no tienes el dinero necesario\n")
                    text(text_falta,0.03)
                    continue
                            
            if op_store=="AF" or op_store=="af":
                if dinero>=40:
                    text_p_inv=("Has comprado un afro, se ha guardado en tu inventario, ahora estas en la onda\n")
                    text(text_p_inv,0.03)
                    afros.append("Afro")
                    dinero=dinero-40
                    continue

                elif int(len(afros))==1:
                    text_p_full=("Ya tienes suficientes afros no crees?\n")
                    text(text_p_full,0.03)
                    continue

                if dinero<40:
                    text_falta=("Lo siento no tienes el dinero necesario\n")
                    text(text_falta,0.03)
                    continue
              
                if op_store=="R" or op_store=="r":
                    if dinero>=50:
                        text_b_inv=("El Rayo de Mcqueen se ha agregado a tu inventario, ahora..eres....veloz\n")
                        text(text_b_inv,0.03)
                        rayos.append("Rayo")
                        dinero=dinero-50
                        continue
                    elif int(len(rayos))==1:
                        text_bot_full=("Ya tienes este rayo mcqueenesco, porque no intentas escoger algo más\n")
                        text(text_bot_full,0.03)
                        continue
                    if dinero<50:
                        text_falta=("Lo siento no tienes el dinero necesario\n")
                        text(text_falta,0.03)
                        continue
                if op_store=="S" or op_store=="s":
                    text_salir=("Veamos que más hay\n")
                    text(text_salir,0.03)
                    break
                else:
                    text_bien=("Disculpa pero eso no esta disponible, escoge algo más\n")
                    text(text_bien,0.03)
                    continue
#------NIVEL 1
    if nivel==1:
        while True:
            text_t_1()
            text_s=("S-Salir\n")
            text(text_s,0.03)
            if dinero<=0:
                text_nada=("Vaya parece ser que no tienes nada de dinero, mejor sal a explorar\n")
                text(text_nada,0.03)
                menu()
            else:
                op_tien_1()          
#-------NIVEL 2               
    if nivel==2:    
            if dinero<=0:
                text_nada=("Vaya parece ser que no tienes nada de dinero, mejor sal a explorar\n")
                text(text_nada,0.03)    
            else:
                while True:
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
                        op_tien_1()
                        continue
                    if tienda_op=="2":
                        text_t_2()
                        text_s=("S-Salir\n")
                        text(text_s,0.03) 
                        op_tien_2()
                        continue
                    if tienda_op=="S" or tienda_op=="s":
                        text_salir=("Regresa a tu aventura\n")
                        text(text_salir,0.03)
                        menu()
                    else:
                        text_no=("Lo siento pero ese departamento no me suena")
                        text(text_no,0.03)
                        continue
#------------NIVEL 3
    if nivel==3:
            if dinero<=0:
                text_nada=("Vaya parece ser que no tienes nada de dinero, mejor sal a explorar\n")
                text(text_nada,0.03) 
            else:
                while True:
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
                        op_tien_1()
                        continue
                    if tienda_op=="2":
                        text_t_2()
                        text_s=("S-Salir\n")
                        text(text_s,0.03) 
                        op_tien_2()
                        continue
                    if tienda_op=="3":
                        text_t_3()
                        text_s=("S-Salir\n")
                        text(text_s,0.03) 
                        op_tien_3()
                        continue
                    if tienda_op=="S" or tienda_op=="s":
                        text_salir=("Regresa a tu aventura\n")
                        text(text_salir,0.03)
                        menu()
                    else:
                        text_no=("Lo siento pero ese departamento no me suena")
                        text(text_no,0.03)
                        continue
#------------NIVEL 4
    if nivel==4:
            if dinero<=0:
                text_nada=("Vaya parece ser que no tienes nada de dinero, mejor sal a explorar")
                text(text_nada,0.03)         
            else:
                while True:
                    num_tienda=("Cuál tienda quieres escoger")
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
                        op_tien_1()
                        continue
                    if tienda_op=="2":
                        text_t_2()
                        text_s=("S-Salir\n")
                        text(text_s,0.03) 
                        op_tien_2()
                        continue
                    if tienda_op=="3":
                        text_t_3()
                        text_s=("S-Salir\n")
                        text(text_s,0.03) 
                        op_tien_3()
                        continue
                    if tienda_op=="4":
                        text_t_4()
                        text_s=("S-Salir\n")
                        text(text_s,0.03) 
                        op_tien_4()
                        continue
                    if tienda_op=="S" or tienda_op=="s":
                        text_salir=("Regresa a tu aventura\n")
                        text(text_salir,0.03)
                        menu()
                    else:
                        text_no=("Lo siento pero ese departamento no me suena")
                        text(text_no,0.03)
                        continue  
menu() #Ponemos al menú afuera, para después regresar al menu de turno 

