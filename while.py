def turing_machine(datos_for):
    # Definimos el alfabeto
    alfabeto = ['i', '=', '1', '<=', '>', '+', '-', '*', '/', '(', ')', '{', '}', ';', ':', ',', '.', '_', ' ', '\n']
    
    # Definimos la tabla de transición
    tabla = [
        # Estado 0
        {
            'i': (1, 'i'),
            ' ': (0, ''),
            '\n': (0, ''),
        },
        # Estado 1
        {
            'i': (1, 'i'),
            '=': (2, '='),
        },
        # Estado 2
        {
            '1': (3, '1'),
        },
        # Estado 3
        {
            '<': (4, '<'),
            '>': (7, '>'),
        },
        # Estado 4
        {
            '=': (5, '='),
        },
        # Estado 5
        {
            '1': (6, '1'),
        },
        # Estado 6
        {
            '+': (3, '+'),
            '-': (3, '-'),
            '*': (3, '*'),
            '/': (3, '/'),
            ';': (0, ';'),
            ' ': (0, ''),
            '\n': (0, ''),
        },
        # Estado 7
        {
            '=': (8, '='),
        },
        # Estado 8
        {
            '1': (9, '1'),
        },
        # Estado 9
        {
            '+': (7, '+'),
            '-': (7, '-'),
            '*': (7, '*'),
            '/': (7, '/'),
            ';': (0, ';'),
            ' ': (0, ''),
            '\n': (0, ''),
        },
    ]
    
    # Inicializamos la cinta y el puntero
    cinta = list(datos_for[0])
    cinta.append(' ')
    puntero = 0
    
    # Inicializamos el estado
    estado = 0
    
    # Inicializamos la salida
    salida = ""
    
    # Empezamos la simulación
    while estado != 0:
        # Leemos el símbolo de la cinta
        simbolo = cinta[puntero]
        
        # Buscamos la transición correspondiente
        if simbolo in alfabeto:
            transicion = tabla[estado][simbolo]
        else:
            transicion = tabla[estado]['_']
        
        # Escribimos el símbolo en la salida
        salida += transicion[1]
        
        # Movemos el puntero
        if transicion[1] == '>':
            puntero += 1
        elif transicion[1] == '<':
            puntero -= 1
        
        # Cambiamos al nuevo estado
        estado = transicion[0]
        
        # Actualizamos la cinta si es necesario
        if len(cinta) <= puntero:
            cinta.append(' ')
        elif puntero < 0:
            cinta.insert(0, ' ')
    
    # Eliminamos los espacios en blanco y los retornos de carro
    salida = salida.replace(' ', '')
    salida = salida.replace('\n', '')
    
    # Construimos la
