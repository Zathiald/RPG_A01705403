from time import sleep #Importamos la libreria de tiempo para usar la función de sleep

import sys #Importamos la librería de sys, donde usaremos la función de flush

import random #Importamos la función para poder generar un número random
#Metodo para generar un numero random obtenido de https://j2logo.com/python/generar-numeros-aleatorios-en-python/

#--------------------------------------------INGRESO JUGADOR--------------------------------------------------------------------------------------------------
def text(texto,speed):#Hacemos una función para hacer que el texto aparezca fluido 
    for c in texto: #Establecemos que por cada letra del texto
        print(c,end='') #Se da un espacio por letra
        sys.stdout.flush() #Extraemos la función flush de sys para hacer que el texto aparezca corrido
        sleep(speed) #Imprimimos una letra cada 0.1 segundos, podemos cambiar para imprimir el texto más lento 

#Metodo para hacer aparecer el texto lentamente obtenido de https://es.stackoverflow.com/questions/25901/como-imprimir-una-cadena-de-texto-con-pausas-entre-cada-letra-impresa-en-python
text1 = ("Como te llamas héroe o heroína: ") #Se le pide al usuario su nombre
text(text1,0.05)

name=str(input())

text2=("Bienvenid@ ",str(name),'\n') #Se le saluda al usuario
text(text2,0.5)

text3=("Estas a punto de embarcarte en una aventura\n") #Se le da al usuario una bienvenida a la aventura
text(text3,0.05)

text4=("¿Estás listo?\n") #Se le pregunta si esta listo para el viaje
text(text4,0.05)

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
#------------------------------------------BIENVENIDA-----------------------------------------------------------------------------------------------------------------------------------   
text8=("Bienvenido al mundo de Palgia, un extenso lugar lleno de enemigos y aliados, amenazas y experiencias\n") #Se le introudce al heroé al mundo del juego
text(text8,0.05)

vida= 10 #Se guarda la variable de vida
velocidad = 5 #Se guarda la variable de velocidad
fuerza = 5 #Se guarda la variable de fuerza
nivel = 1 #Se guarda el nivel
exp = 0 #Se guarda la experiencia

def stats(): #Creamos una función que presentara las stats cada vez que la llamamos

    name_text=("Nombre: ",name,'\n')
    text(name_text,0.05)

    vida_text=("Vida: ",vida,'\n') #Se presenta la vida
    text(vida_text,0.05)

    velocidad_text=("Velocidad: ",velocidad,'\n') #Se presenta la velocidad
    text(velocidad_text,0.05)

    fuerza_text=("Fuerza: ",fuerza,'\n') #Se presenta la fuerza
    text(fuerza_text,0.05)
    
    nivel_text=("Nivel: ",nivel,'\n') #Se presenta su nivel
    text(nivel_text,0.05)

    exp_text=("Exp: ",exp,'\n') #Se presenta su exp
    text(exp_text,0.05)
    
text9=("Estos son tus stats iniciales\n") #Se le presenta al jugador sus stats iniciales
text(text9,0.05)
    
stats() #Llamamos a la función de stats para mostrarselas al jugador

text10=("Si en algún momento quieres ver tus stats presiona S al inicio de cada turno\n") #Se le dice al usuario que al presionar S puede ver sus stats
text(text10,0.05)

text11=("Para moverte presiona las teclas W,A,S,D y te moveras en esa dirección\n") #Se le dice al usuario como hacer para seleccionar dirección de movimiento
text(text11,0.05)

text12=("Según tu velocidad es cuantos cuadros podras moverte por turno\n") #Se le dice al usuario cuanto se movera según su velocidad
text(text12,0.05)

text13=("Por ejemplo ahora tienes 5 de velocidad, así que te mueves 5 cuadros por turno\n") #Se le da un ejemplo de la velocidad
text(text13,0.05)

text14=("Para escoger moverte al inicio de cada turno presiona M\n") #Se le dice al usuario como hacer para moverse
text(text14,0.05)

text15=("Al escoger la opción de moverte, hay una posibilidad de que aparezca un enemigo, pueblo u objeto en tu camino\n") #Se le dice al usuario como hacer para moverse
text(text15,0.05)

text16=("Por toda Palgia hay varios objetos místicos, usalos con sabiduría para obtener ventaja en combate\n") #Se le dice al usuario como hacer para moverse
text(text16,0.05)

text17=("Pero cuidado, que algunos objetos estan embrujados y te podrían bajar los stats\n") #Se le dice al usuario como hacer para moverse
text(text17,0.05)

text18=("Para ver y escoger un objeto al inicio de cada turno presiona I\n") #Se le dice al usuario como hacer para moverse
text(text18,0.05)

text19=("Ahora que estas familiarizado con las acciones básicas\n") #Se le dice al usuario como hacer para moverse
text(text19,0.05)
#---------------------------------------FUNCIONES PRINCIPALES-----------------------------------------------------------------------------------------------------
def diriol(): #Hacemos una función por enemigo para alterar simplementa las fuerzas,velocidad y vida

    fuerza_diriol = 1 #Declaramos la fuerza de este enemigo
    velocidad_diriol = 6 #Declaramos la velocidad de este enemigo
    vida_diriol = 7 #Declaramos la vida de este enemigo

    #Metodo para declarar global variable obtenido de https://bobbyhadz.com/blog/python-unboundlocalerror-local-variable-name-referenced-before-assignment#:~:text=The%20Python%20"UnboundLocalError%3A%20Local%20variable,function%20definition%2C%20e.g.%20global%20my_var%20.
    global vida 
    global velocidad
    global fuerza
    global nivel
    global exp

    text_enem=("Los stats de este enemigo son: \n") #Mostramos los stats de el enemigo
    text(text_enem,0.05)

    nom_diriol_t=("Nombre: Diriol \n") #Se presenta su vida
    text(nom_diriol_t,0.05)

    velocidad_diriol_t=("Velocidad: ",velocidad_diriol,'\n') #Se presenta su velocidad
    text(velocidad_diriol_t,0.05)

    fuerza_diriol_t=("Fuerza: ",fuerza_diriol,'\n') #Se presenta su fuerza
    text(fuerza_diriol_t,0.05)
    
    vida_diriol_t=("Nivel: ",vida_diriol,'\n') #Se presenta la fuerza
    text(vida_diriol_t,0.05)

    while True: #Creamos un loop para la secuencia de ataque
        text_atac=("Presiona X para atacar \n") #Le decimos al usuario que presione X para atacar
        text(text_atac,0.05)

        atac=str(input()) #Registramos el ataque

        if atac!="X" and atac!="x": #Declaramos que pasa si el usuario no presiona X

            vida=vida-fuerza_diriol #Si el usuario no presiona X, entonces se le quita vida

            text_atacado=("¡NO ATACASTE!. Ahora el enemigo te ha atacado\n") #Damos un mensaje de que no ataco
            text(text_atacado,0.05)

            text_vida_u=("Tu vida ahora es ",vida,'\n') #Mostramos la vida al usuario
            text(text_vida_u,0.05)
            
            if vida>0: #Si la vida del usuario es mayor a 0, puede atacar de nuevo
                continue

            if vida==0 or vida<0: #Si la vida del usuario es menor o igual a 0, le mostramos un mensaje de Game Over
                text_lose=("¡GAME OVER!\n") #Le mostramos al usuario un mensaje de game over
                text(text_lose,1.0)
                exit()

        if atac=="X" or atac=="x": #Declaramos que pasa si el usuario presiona X

            atak=random.randint(0,1) #Generamos un número random, para que sucedad la posibilidad de que falle el ataque
            #Declaramos que la variable sera un número integer random, de entre 0 a 1

            if atak==1: #Declaramos que pasa si el número random es 1
                vida=vida-fuerza_diriol #Si el número random es 1, le quitamos vida al enemigo
                text_atacado=("¡FALLASTE!. Ahora el enemigo te ha atacado\n") #Le decimos al usuario que su vida fallo
                text(text_atacado,0.05)

                text_vida_u=("Tu vida ahora es ",vida,'\n') #Le mostramos su nueva vida
                text(text_vida_u,0.05)
            
                if vida>0: #Si la vida del usuario es mayor a 0, puede atacar de nuevo
                    continue

                if vida==0 or vida<0: #Si la vida del usuario es menor o igual a 0, le mostramos un mensaje de Game Over
                    text_lose=("¡GAME OVER!\n") #Le mostramos al usuario un mensaje de game over
                    text(text_lose,1.0)
                    exit() #Terminamos el código si se nos acaba la vida
   
            if atak==0: #Declaramos que pasa si el número random es 0
                vida_diriol=vida_diriol-fuerza #Si el número random es 0, le quitamos vida al enemigo

                text_atacar=("¡Has atacado al enemigo!\n") #Le decimos al usuario que ha logrado atacar al enemigo
                text(text_atacar,0.05)

                text_vida_d=("Su vida ahora es ",vida_diriol,'\n') #Mostramos la nueva vida del enemigo
                text(text_vida_d,0.05)

                if vida_diriol==0 or vida_diriol<0: #Si la vida del enemigo es igual o menor a 0, le decimos al usuario que gano
                    text_lose=("¡LO LOGRASTE!\n") #Le mostramos el mensaje de victoria al usuario
                    text(text_lose,0.05)
                    exp=exp+1 #Le sumamos experiencia al usuario
                    stats() #Le mostramos sus stats de nuevo
                    if exp==5: #Establecemos que pasa si el usuario consigue 10 de experiencia
                        nivel =nivel+1 #Le sumamos 1 a su nivel
                        vida = vida+2 #Le agregamos 2 a la vida 
                        velocidad = velocidad+2 #Le agregamos 2 a la velocidad
                        fuerza = fuerza+2 #Le agregamos 2 a la fuerza
                        text_subir=("¡Has subido de nivel! ¡FELICIDADES!\n") #Le mostramos un mensaje de felicitación
                        text(text_subir,0.05)
                        stats()
                    break #Seguimos el código y mostramos de nuevo el menú

                if vida_diriol>0: #Declaramos que pasa si la vida del enemigo es mayor a 0
                    continue #Reiniciamos el loop

def ataque(): #Declaramos que pasa si hay un enemigo
    text_enemigo=("¡Oh no! un enemigo ha aparecido\n") #Mostramos un mensaje de que ha aparecido un enemigo
    text(text_enemigo,0.05)
    diriol() #Llamamos la función del enemigo
    menu() #Regresamos al menú

def menu(): #Creamos una función que nos permitira presentar el menú al principio de cada turno

    while True: #Iniciamos un loop dentro de el menú
        text_menu=("Que quieres hacer:\n") #Se le pregunta al usuario que quiere hacer
        text(text_menu,0.05)

        text_mover=("M - Moverte\n") #Se muestra la opción de moverse
        text(text_mover,0.05)

        text_stats=("S - Stats\n") #Se muestra la opción de ver stats
        text(text_stats,0.05)

        text_inv=("I - Inventario\n") #Se muestra la opción de ver inventario
        text(text_inv,0.05)

        opc=str(input()) #Tomamos la decisión del usuario

        while True:
            if opc=="S" or opc=="s": #Declaramos que pasa si escoge S
                stats() #Llamamos a la función de ver stats
                menu() #Regresamos al menú
            if opc=="M" or opc=="m": #Declaramos que pasa si escoge M
                mover() #Llamamos a la función de moverse
            if opc=="I" or opc=="i": #Declaramos que pasa si escoge I
                inv() #Llamamos a la función de inventario 
            else: #Declaramos que pasa si el usuario no escoge bien
                text20=("Por favor escoge una de las opciones disponibles\n") #Se muestra un mensaje de que escoga bien
                text(text20,0.05)
                menu() #Llamamos al menú

def mover(): #Definimos la función del movimiento

    while True: #Creamos un loop para escoger una dirección

        text_movin=("A donde te quieres mover:\n") #Se le pregunta al usuario a donde se quiere mover 
        text(text_movin,0.05)

        text_norte=("W - Norte\n") #Le decimos que W es para norte
        text(text_norte,0.05)

        text_oeste=("A - Oeste\n") #Le decimos que A es para oeste
        text(text_oeste,0.05)

        text_sur=("S - Sur\n") #Le decimos que S es para sur
        text(text_sur,0.05)

        text_este=("D - Este\n") #Le decimos que D es para este
        text(text_este,0.05)

        dir=str(input()) #Tomamos la función de dirreción

        if dir!= "W" and dir != "w" and dir != "A" and dir != "a" and dir != "S" and dir != "s" and dir != "D" and dir != "d": #Declaramos que pasa si el usuario no escoge la dirección correcta
            text_mov_cor=("Esa no es una direccion, escoge bien\n") #Le decimos que no es una dirección correcta
            text(text_mov_cor,0.05)
            continue #Reiniciamos el loop
        
        else: #Si el usuario escoge una direcciónn correcta
            turno=random.randint(0,3) #Generamos un número random
            #Declaramos que la variable sera un número integer random, de entre 0 a 3

        def text_dir():
            if dir=="W" or dir=="w":
                text_mov=("Te has movido ",velocidad," cuadros al Norte \n") #Si el usuario escogio W le decimos que se movio, segun la velocidad, eso al norte
                text(text_mov,0.05)

            if dir=="A" or dir=="a":
                text_mov=("Te has movido ",velocidad," cuadros al Oeste \n") #Si el usuario escogio A le decimos que se movio, segun la velocidad, eso al oeste
                text(text_mov,0.05)

            if dir=="S" or dir=="s":
                text_mov=("Te has movido ",velocidad," cuadros al Sur \n") #Si el usuario escogio S le decimos que se movio, segun la velocidad, eso al sur
                text(text_mov,0.05)

            if dir=="D" or dir=="d":
                text_mov=("Te has movido ",velocidad," cuadros al Este \n") #Si el usuario escogio D le decimos que se movio, segun la velocidad, eso al este
                text(text_mov,0.05)
            
        if turno==0: #Declaramos que pasa si el número random es 0
            text_dir()
            text_nada=("Vaya parece que no hay nada por aquí\n") #Le decimos al usuario que no hay nada alrededor
            text(text_nada,0.05)
            menu() #LLamamos la función de el menú
            
        if turno==1: #Declaramos que pasa si el número random es 1
            text_dir()
            ataque() #Si el número random es 1, llamamos a la función de ataque

        if turno==2: #Declaramos que pasa si el número random es 2
            text_dir()
            text_pueblo=("Un pueblo,parece ser puedes obtener cosas aquí\n") #Si el número es 2, aparece un pueblo en el camino
            text(text_pueblo,0.05)
            menu() #LLamaos al menú
    
        if turno==3: #Declaramos que pasa si el numero random es 3
            text_dir()
            text_obj=("Has encontrado un artefacto\n") #Si el número random es 3, el jugador encuentra un objeto
            text(text_obj,0.05)
            menu() #Regresamos al menú
          
def inv(): #Creamos una función para acceder al inventario
    text_inv=("Aquí veras tu inventario\n") #Le decimos al usuario que aquí podra ver su inventario
    text(text_inv,0.05)
    menu() #Regresamos al menu

menu() #Ponemos al menú afuera, para después regresar al menu de turno



