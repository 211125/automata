def for_to_while_turing(for_code):
    # Definimos el alfabeto de entrada y salida de la máquina de Turing
    input_alphabet = {'f', 'o', 'r', '(', ')', ';'}
    output_alphabet = {'w', 'h', 'i', 'l', 'e', '(', ')', '{', '}', ';'}

    # Definimos las transiciones de la máquina de Turing
    transitions = {
        ('start', 'f'): ('start', 'w'),
        ('start', 'o'): ('start', 'h'),
        ('start', 'r'): ('start', 'i'),
        ('start', '('): ('start', 'l'),
        ('start', ')'): ('start', 'e'),
        ('start', ';'): ('start', ';'),

        ('start', ' '): ('start', ' '),

        ('l', 'i'): ('l', 'i'),
        ('l', ';'): ('l', ';'),
        ('l', ' '): ('l', ' '),
        ('l', ')'): ('start', '{'),

        ('{', ' '): ('{', ' '),
        ('{', '}'): ('start', ' '),
        ('{', 'f'): ('for', 'w'),
        ('{', 'w'): ('while', 'w'),

        ('for', 'o'): ('for', 'h'),
        ('for', 'r'): ('for', 'i'),
        ('for', ';'): ('for', ';'),

        ('for', ' '): ('for', ' '),

        ('for', ')'): ('for_to_end', ';'),

        ('while', 'o'): ('while', 'h'),
        ('while', 'r'): ('while', 'i'),
        ('while', ';'): ('while', ';'),

        ('while', ' '): ('while', ' '),

        ('while', ')'): ('while_to_do', '{'),

        ('for_to_end', ' '): ('for_to_end', ' '),
        ('for_to_end', '{'): ('for_to_end', '{'),

        ('for_to_end', ';'): ('start', ' '),

        ('while_to_do', ' '): ('while_to_do', ' '),
        ('while_to_do', '{'): ('do', ' '),

        ('do', ' '): ('do', ' '),
        ('do', '}'): ('while_to_end', ';'),

        ('while_to_end', ' '): ('while_to_end', ' '),
        ('while_to_end', ';'): ('start', ' '),
    }

    # Inicializamos la cinta de entrada con el código del bucle for
    input_tape = ['B'] + [c for c in for_code] + ['B']

    # Inicializamos la cinta de salida con un espacio en blanco
    output_tape = ['B', ' ']

    # Inicializamos la posición de la cabeza de lectura/escritura en la cinta de entrada
    input_head = 1

    # Definimos la posición de la cabeza de escritura en la cinta de
    # salida
    output_head = 1

    # Definimos el estado actual de la máquina de Turing
    current_state = 'start'

    # Mientras no hayamos llegado al estado final
    while current_state != 'end':
        # Leemos el carácter en la cinta de entrada
        current_input = input_tape[input_head]

        # Buscamos la transición correspondiente


        # Buscamos la transición correspondiente
        if (current_state, current_input) in transitions:
            # Obtenemos el estado de destino
            target_state = transitions[(current_state, current_input)][0]

            # Obtenemos el carácter de salida
            output_char = transitions[(current_state, current_input)][1]

            # Escribimos el carácter de salida en la cinta de salida
            try:
                output_tape[output_head] = output_char
            except IndexError:
                # Si la cabeza de escritura se ha movido más allá del tamaño actual
                # de la cinta de salida, agregamos un carácter en blanco
                output_tape.append(' ')
                output_tape[output_head] = output_char

            # Movemos la cabeza de lectura/escritura
            if output_char == ' ':
                input_head += 1
            elif output_char in output_alphabet:
                output_head += 1

            # Cambiamos al estado destino
            current_state = target_state
        else:
            # Si no hay transición, detenemos la máquina de Turing
            current_state = 'end'

    # Devolvemos la cinta de salida sin los caracteres de borde
    return ''.join(output_tape[1:-1])

result = for_to_while_turing("for (int i = 0; i < 10; i++);")
print(result)