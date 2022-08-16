# RPG_A01705403

Proyecto TC1028 de Pensamiento Computacional de Samir Baidon Pardo A01705403

# RPG

### Contexto

Un RPG son las siglas para Role Playing Game, es un genero de los videojuegos que te permite personalizar a tu personaje, ir en aventuras y suir de nivel para poder derrotar enemigos más poderosos, todo con el fin de explorar un gran mundo repleto de personajes, objetos y enemigos por doquier y tu como el jugador es tu misión sobrevivir

### Explicación código

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

