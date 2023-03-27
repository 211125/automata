def turing_machine(input_list):
    # Definir la tabla de transiciones
    transitions = {
        ('q0', 'i'): ('q0', 'i', 'R'),
        ('q0', '='): ('q0', '=', 'R'),
        ('q0', '0'): ('q0', '0', 'R'),
        ('q0', ','): ('q0', ';', 'R'),
        ('q0', '_'): ('qf', '_', 'S'),
        ('q1', '<'): ('q1', '<', 'R'),
        ('q1', '3'): ('q1', '3', 'R'),
        ('q1', '2'): ('q1', '2', 'R'),
        ('q1', ','): ('q2', '{', 'R'),
        ('q2', 'd'): ('q3', 'd', 'R'),
        ('q3', 'a'): ('q4', 'a', 'R'),
        ('q4', 't'): ('q5', 't', 'R'),
        ('q5', 'o'): ('q6', 'o', 'R'),
        ('q6', ','): ('q7', ' ', 'R'),
        ('q7', 'i'): ('q8', 'i', 'R'),
        ('q8', '+'): ('q9', '+', 'R'),
        ('q9', '+'): ('q0', '}', 'R'),
    }
    # Unir las cadenas en la lista de entrada en una sola cadena
    input_string = ''.join(input_list)
    # Configurar la cinta y la cabeza de lectura/escritura
    tape = list(input_string) + ['_']
    head_position = 0
    current_state = 'q0'
    # Ejecutar la máquina de Turing hasta que se detenga
    while current_state != 'qf':
        current_symbol = tape[head_position]
        try:
            new_state, new_symbol, direction = transitions[(current_state, current_symbol)]
        except KeyError:
            print('Error: no se encontró la transición para el estado y el símbolo actual')
            return None
        tape[head_position] = new_symbol
        if direction == 'R':
            head_position += 1
        elif direction == 'L':
            head_position -= 1
        current_state = new_state
    # Eliminar los símbolos en blanco y devolver la cadena de texto
    result_string = ''.join(tape[:-1]).replace('_', '')
    return result_string

a = ['i=0', 'i<32', 'i++', 'dato']
result = turing_machine(a[0])
print(result)
