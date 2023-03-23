# la cinta 1 almacenara el universo donde se encuantran los elementos
cinta1 = ['B','a','b','c','d','e','f','g','h','i','j','k','l','m','n','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','B']

# la cinta2 almacenara la expresion de union que el usuario ingreso 
cinta2 = []

# la cinta 3 almacenara el resultado de la union de los conjuntos(aun no se an eliminado elementos repetidos)
cinta3 = ["B"]

#son los cabezales de cada cinta 
cabezales = [0,0,0]

# estado final


trancision = [
    [['A','{','B'],['B','{','{','D','D']],
    [['C',',','B'],['B',',',',','D','D']],

    [['C','}','B'],['D','}','B','D','S']],
    [['D','B','B'],['E','B','}','S','S']],
    [['D','∪','B'],['F','∪',',','D','D']],
    [['F','{','B'],['B','{','B','D','S']],

    [['B','a','B'],['C','a','a','D','D']],
    [['B','b','B'],['C','b','b','D','D']],
    [['B','c','B'],['C','c','c','D','D']],
    [['B','d','B'],['C','d','d','D','D']],
    [['B','e','B'],['C','e','e','D','D']],
    [['B','f','B'],['C','f','f','D','D']],
    [['B','g','B'],['C','g','g','D','D']],
    [['B','h','B'],['C','h','h','D','D']],
    [['B','i','B'],['C','i','i','D','D']],
    [['B','j','B'],['C','j','j','D','D']],
    [['B','k','B'],['C','k','k','D','D']],
    [['B','l','B'],['C','l','l','D','D']],
    [['B','m','B'],['C','m','m','D','D']],
    [['B','n','B'],['C','n','n','D','D']],
    [['B','o','B'],['C','o','o','D','D']],
    [['B','p','B'],['C','p','p','D','D']],
    [['B','q','B'],['C','q','q','D','D']],
    [['B','r','B'],['C','r','r','D','D']],
    [['B','s','B'],['C','s','s','D','D']],
    [['B','t','B'],['C','t','t','D','D']],
    [['B','u','B'],['C','u','u','D','D']],
    [['B','v','B'],['C','v','v','D','D']],
    [['B','w','B'],['C','w','w','D','D']],
    [['B','x','B'],['C','x','x','D','D']],
    [['B','y','B'],['C','y','y','D','D']],
    [['B','z','B'],['C','z','z','D','D']],
    [['B','0','B'],['C','0','0','D','D']],
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




#mover cabezal
def mover_derecha(cual):
    cabezales[cual] += 1

#mover cabezal a la izquierda
def mover_inquierda(cual):
    cabezales[cual] -= 1

#identifica si el cabezal va a la derecha o a la izquierda
def identificar_D_I_cabezal(e): #pasar el numero de trancision

    if trancision[e][1][3] == 'D':
        mover_derecha(1)
    elif trancision[e][1][3] == 'I':
        mover_inquierda(1)
    elif trancision[e][1][3] == 'S':
        print('no se mueve el cabezal')

    if trancision[e][1][4] == 'D':
        mover_derecha(2)
    elif trancision[e][1][4] == 'I':
        mover_inquierda(2)
    elif trancision[e][1][4] == 'S':
        print('no se mueve el cabezal')


#se rellena la cinta2
 
def rellenar_cinta2():
    expresion_union = input("Hola por favor agrega los conjuntos que se van unir \n Ejemplo: {a,b,c}∪{h,1,2} \n")
    for caracter in expresion_union:
        cinta2.append(caracter)
    cinta2.append("B")

    print(cinta2)

#se genera la logica de la maquina de turing para
#el error esta en que ilo pongo en la posicon 0 por lo que pone primero { B depues a { B
def rellenar_cinta3():
    estatado_actual = 'A'
    arreglo_auxiliar = []
    numero_elementos = len(cinta2)
    numero_transiciones = len(trancision) +1
    for i in range(numero_elementos):
        
        print('Buenas tardes')
        print(cabezales[1])
        print(cabezales[2])

        arreglo_auxiliar.append(estatado_actual)
        print()
        arreglo_auxiliar.append(cinta2[cabezales[1]])
        arreglo_auxiliar.append(cinta3[cabezales[2]])
        for e in range(numero_transiciones):
            if trancision[e][0] == arreglo_auxiliar:
                print(trancision[e][0],' == ', arreglo_auxiliar)
                print(trancision[e][1][0])
                estatado_actual = trancision[e][1][0]
                cinta2[cabezales[1]] =  trancision[e][1][1]
                cinta3[cabezales[2]] =  trancision[e][1][2]
                cinta3.append('B')
                identificar_D_I_cabezal(e)
                arreglo_auxiliar = []
                print(cinta3)
                break
    print(cinta3)







def main():
    rellenar_cinta2()
    rellenar_cinta3()
    
        
    


   


main()