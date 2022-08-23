# RPG_A01705403

Proyecto TC1028 de Pensamiento Computacional de Samir Baidon Pardo A01705403

# RPG

## Contexto

Un RPG son las siglas para Role Playing Game, es un género de los videojuegos que te permite personalizar a tu personaje, ir en aventuras y subir de nivel para poder derrotar enemigos más poderosos, todo con el fin de explorar un gran mundo repleto de personajes, objetos y enemigos por doquier y tu como el jugador es tu misión sobrevivir, algunos ejemplos son:
- The Legend of Zelda
- Fire Emblem
- Final Fantasy
- Dragon Quest
- Omori
- Pokémon
- Undertale
- Earthbound

## Explicación código

En el programa se usan varias matemáticas para poder determinar:
- Vida
- Nivel
- Daño
- Estadisticas

Para poder determinar estas variables se pueden usar sumas y restas simples, junto con multiplicaciones, es cuestión de guardarlos en variables con nombre y luego crear funciones, las cuales dependiendo de lo que sucedad aumentaran o bajaran estas variables, por ejemplo si un enemigo te ataca, creamos una función para ataque que baje la vida del jugador dependiendo de cuanto daño puede hacer el enemigo.

Para poder generar enemigos en el mapa podemos usar un generador de números random, podemos poner por ejemplo que si el número es par entonces se aparece un enemigo y si es inpar no, algo que se conecte al movimiento del jugador, y para el movimiento del jugador lo que se puede hacer es que se le pida seleccionar una tecla:
- W - Frente
- A - Izquierda
- S - Atrás
- D - Derecha

Y luego hacemos que se ponga un texto que le diga al jugador cuanto ha avanzado, esto tomando en cuenta sus estadísticas de velocidad, y luego al avanzar ahí tambien corremos la función de generar un enemigo random para que el jugador lo derrote.

## Algoritmo
El algoritmo sería primero preguntarle al usuario que quiere hacer ,y luego en base a lo que haya hecho, y luego si se mueve y hay algo se le dira al usuario que puede o debe interactuar con dicho elemento, por ejemplo si hay un enemigo se inicia una fase de combate, si hay una tienda se le dice al usuario que puede comprar en la tienda, sería algo así:

  - 1ºEl usuario escoge entre opciones del menu
      /*Si el usuario usa un objeto: Se le aumentan las estadisticas según el objeto
      /*Si el usuario se mueve:
        /*Se le dice al usuario que hay alrededor
          /*Si hay un enemigo: Inicia fase de combate
          /*Si hay un objeto: Se le dice al usuario obtuvo un objeto
          /*Si hay una tienda: Se le dice al usuario que puede comprar
     /*Si el usuario cambia vestimenta: Se le aumentan las estadisticas según su vestuario
     /*Si el usuario quiere guardar: Se guardan sus variables y se termina el juego hasta que lo vuelva a usar
  
  - 2ºEl usuario muere: Se le regresa a la vida desde el último punto guardado


## Resumen

En general es un proyecto largo y que necesitará muchas funciones, matemáticas y texto, pero es algo posile, es algo que se puede medir y que se puede crear algoritmos para cada parte, se puede desglozar y tomar parte por parte, e incluso podría servir como codigo base para en un futuro agregarle gráficos.


