Bienvenido a Proyecto Dispositivos
Este proyecto fue hecho con mucha pasión y entusiasmo :,D

1. INFORMACIÓN SOBRE EL PROYECTO
    El proyecto contiene 9 módulos, cada uno con una función especial y clave con la cual se puede ejecutar este programa.
    
    a. CU 
        Este módulo es el orquestador de toda la operación, pues llama a cada módulo y sus métodos cuando es necesario, así como generar las primeras cargas de datos necesarios en los registros.
    
    b. ROM
        Este módulo se encarga de leer y guardar los datos importantes encontrados en BIOS.yaml, así como Instruction.txt. Cuando se encuentra una instrucción al momento de leer los archivos .cpufm se analiza desde este módulo.
    
    c. RAM
        Este módulo contiene la data del BIOS.yaml, de igual manera, contiene momentaneamente las instrucciones que se indican en los archivos .cpufm. Además de los métodos para sobreescribir la data en las posiciones indicadas y de obtener el valor de la data en una posición determinada.

    d. ALU
        Este módulo realiza todas las operaciones aritméticas y lógicas necesarias para el programa. De este se destacan las operaciones de suma, resta, and, or, y comparaciones (<,>,=).

    e. CLOCK
        Este módulo obtiene el valor en Hz del clock indicado en BIOS.yaml y lo convierte a segundos. Su método sleepScreen es fundamental para la ejecución del programa, pues coordina el tiempo entre Fetch, Decode y Exedute.
    
    f. INTERGRATEDCIRCUIT
        Este módulo contiene el constructor del IC, que es la clase madre del proyecto.
    
    g. MEMORY
        Este módulo define el tope de bits de la memoria (4 en este caso)
    
    h. REGISTER
        Este módulo se encarga de definir cada registro y el valor de ram que contendrá cada registro según se vaya requiriendo por la operación o por lo indicado por las instrucciones de los archivos .cpufm

    i. RUN
        Desde este módulo se crea un objeto tipo CU, que contiene las características heredadas de IC. También llama al método esencial de CU, main().

2.  EJECUCIÓN DEL PROYECTO
    a. INICIO
        Al iniciar, se debe correr el módulo Run.py, desde donde se creara el objeto de tipo CU, e iniciará con la ejecución del proyecto.
    
    b. DENTRO DE LA EJECUCIÓN
        Al iniciar la ejecución el proyecto, este le dará al usuario la posibilidad de elegir entre los programas de tipo .cpufm disponibles. Luego, para ejecutar los mismos se da la posibilidad de elegir entre dos formas, de tipo Clock y de tipo Debug.
        
        b.1. CLOCK
            Esta forma de ejecución es automático, mostrará en pantalla lo realizado en cada etapa del ciclo Fetch, Decode y Execute, esto según el tiempo indicado por el Clock.
        
        b.2. DEBUG 
            Esta forma de ejecución es pausada, y avanzará cada vez que el usuario presione la tecla "Enter", mostrando en pantalla lo realizdo en cada etapa del ciclo Fetch, Decode y Execute.

        Cabe aclarar que en ambas formas de ejecución mostrara lo realizado en cada etapa del ciclo, así como los valor en cada Registro, la data contenida en la RAM y los estados de las banderas de la ALU.

3. CREADORES
    Los creadores del proyecto fueron:
    - Carlos Alvarado
    - Javier Mazariegos
    - Mario Pisquiy