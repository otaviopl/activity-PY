Matriz=[]
N = int(input("Informe a quantidade de linhas da Matriz:"))
M = int(input("Informe a quantidade de colunas da Matriz:"))
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
    


    