"""***Secuencia de Collatz***"""
number_co=696           #inicia con los ultimos 3 digitos de mi carnet (201444696).   

while number_co !=1:    #El numero debe ser diferente de 1 para ejecutarse.
    if number_co%2==0:  #Si el resto 696 (y cada nuevo numero) es igual a 0, (numero par).
        print("%d"%(number_co),end = "" "\n") #Mostrar la sucecion.
        number_co=number_co / 2 #Hacer la division dentro de 2 para cada nuevo numero
    else:
        print("%d" % (number_co),end = "" "\n") #Si el resto es diferente de 0 para cada numero, imprimir su sucecion.
        number_co=(number_co * 3)+1             #Hacer 3 vaces cada nuevo numero mas una unidad.
