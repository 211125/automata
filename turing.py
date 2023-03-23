# código para transformar un for a while
# la cinta 1 almacenará el universo donde se encuentran los elementos
cinta1 = ['B','1','2','3','4','5','6','7','8','9','B']
# la cinta2 almacenará la expresión de for que el usuario ingresó
cinta2 = []
cinta4 = ['f','o','r','(']
# la cinta 3 almacenará el resultado de la transformación de for a while (aun no se han eliminado elementos repetidos)
cinta3 = ["B"]
# son los cabezales de cada cinta
cabezales = [0,0,0]
# estado final
trancision = [
    [['A','for','B'],['B','for','{','D','D']],
    [['C','(','B'],['B','(','(','D','D']],
    [['C',';','B'],['D',';','B','D','S']],
    [['D','B','B'],['E','B',';','S','S']],
    [['D','while','B'],['F','while',')','D','D']],
    [['F','{','B'],['B','{','B','D','S']],

    [['B','1','B'],['C','1','1','D','D']],
    [['B','2','B'],['C','2','2','D','D']],
    [['B','3','B'],['C','3','3','D','D']],
    [['B','4','B'],['C','4','4','D','D']],
    [['B','5','B'],['C','5','5','D','D']],
    [['B','6','B'],['C','6','6','D','D']],
    [['B','7','B'],['C','7','7','D','D']],
    [['B','8','B'],['C','8','8','D','D']],
    [['B','9','B'],['C','9','9','D','D']],

]
# mover cabezal
def mover_derecha(cual):
    cabezales[cual] += 1

# mover cabezal a la izquierda
def mover_inquierda(cual):
    cabezales[cual] -= 1

# identifica si el cabezal va a la derecha o a la izquierda
def identificar_D_I_cabezal(e): #pasar el numero de trancision

    if trancision[e][0][1] == 'for':
        mover_derecha(1)
        print("xd")
        print(trancision[e][1][1])
        print("xd")
    elif trancision[e][1][3] == 'I':
        mover_inquierda(1)
        print(trancision[e][1][3])
    elif trancision[e][1][3] == 'S':
       
        print('no se mueve el cabezal')
        print(trancision[e][1][3])

    if trancision[e][1][4] == 'D':
        mover_derecha(2)
        print(trancision[e][1][4])
    elif trancision[e][1][4] == 'I':
        mover_inquierda(2)
        print(trancision[e][1][4])
    elif trancision[e][1][4] == 'S':
        print('no se mueve el cabezal')

# se rellena la cinta2
def rellenar_cinta2():
    expresion_for = input("Hola por favor ingresa la expresión for para transformarla a while \n Ejemplo: for(i=1;i<=10;i++) \n")
    cinta2 = []
    for caracter in expresion_for:
        cinta2.append(caracter)
    cinta2.append("B")
   
    nueva_cinta2 = []
    for caracter in cinta2:
        if caracter != " ":
            nueva_cinta2.append(caracter)
    cinta2 = nueva_cinta2

    print(cinta2)
    
   
# se genera la lógica de la máquina de Turing para
# el error está en que lo pongo en la posición 0 por lo que pone primero { B después a { B

        
def rellenar_cinta3():
       print(cinta2)
    
def main():
    rellenar_cinta2()
    rellenar_cinta3()
main()