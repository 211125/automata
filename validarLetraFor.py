a = ['f', ' ', ' ', 'o', ' ', ' ', 'r', '(', 'i', '=', '8', ';', ' ', '8', ' ', '3', ';', ')', '{', '}']
n = len(a)

i = 0
while i < n - 2:
    if a[i] == 'f' and a[i+1] == 'o' and a[i+2] == 'r':
        i += 3
    elif a[i+1] == ' ' or a[i+2] == ' ':
        print('Error: espacio en la secuencia')
        break
    else:
        print('Error: secuencia inválida')
        break

if i == n - 2:
    print('Error: secuencia incompleta')
elif i == n - 1:
    print('Error: falta un carácter en la secuencia')
else:
    print('Secuencia válida')
