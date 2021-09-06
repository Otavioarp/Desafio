def retorna_guiche_ingresso(ingresso_numero):
    impares = []
    for j in range(1,ingresso_numero,2):
        if j % 2 != 0:
            impares.append(j)
    print(impares)
    if  2 > ingresso_numero >= 0:
        return 1 if ingresso_numero ==1 else 0
    i , x = 2 , 0
    while x < len(impares):
        if ingresso_numero in range(1,i):
            return x + 1
        x += 1
        i += impares[x]