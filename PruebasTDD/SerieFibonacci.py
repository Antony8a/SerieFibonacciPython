def calcularSerie(numero):
    v1 = 0
    v2 = 1

    if(numero == 1):
        return 0
    elif(numero == 2):
        return 1
    else:
        for i in range(1,numero-1,1):
            temp = v1
            v1=v2
            v2=temp+v1

        return(v2)