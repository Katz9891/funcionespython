def invertiordenclaves(clave):
    z=0 #inicializamos z en 0 para almacenar el numero invertido
    x=clave

    while x>0:
        k=x%10 #obtiene el ultimo digito de x
        z=z*10+k #agrega el digito a z
        x=x//10 #elimina el ultimo digito de x

    print (z)
