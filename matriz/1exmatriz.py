Matriz=[]
N = int(input("Informe a quantidade de linhas da Matriz:"))
M = int(input("Informe a quantidade de colunas da Matriz:"))
mai=0
men=0
for i in range(N):
    Linha = []
    print(f"Informe os elementos da linha {i};")
    for j in range(M):
        elem = int(input(f"Entre com o elemento da coluna {j}: "))
        Linha.append(elem)
    Matriz.append(Linha)
for i in range(N):
    for j in range(M):
        print(f"[{Matriz[i][j]}]", end = " " )
    print()    
for i in range(N,M):
    
    if i==0:
        mai=Linha[i]
    else:
        if Linha [i]>mai:
            mai=Linha[i]
    if i==0:
        men=Linha[i]
    else:
        if Linha [i]<men:
            men=Linha[i]
            for j in range(N,M):
                if j==0:
                    mai=Linha[j]
                else:
                    if Linha [j]>mai:
                        mai=Linha[j]
                        if j==0:
                            men=Linha[j]
                        else:
                            if Linha [j]<men:
                                men=Linha[j]
print('maior',mai)
print('menor',men)                               
    
            
    

    


    