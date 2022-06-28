#EX1#
print('PRIMEIRO EX')
L1=[7,132,5,28,-1,69,-16]
L2=[0,-8,267,21,9,18,755]
print(f'Lista1:{L1} e lista2:{L2}')
o=L1+L2
o[0::2]=L1
o[1::2]=L2
print('lista nova:',o)
#EX  'incompleto :(' #
print('SEGUNDO EX')

l1=[]
x=input('digite sim para continuar:')
while x=='sim':
    num=input('qual numero deseja colocar?')
    x=input('digite sim para continuar:')
    l1.append(num)
    print(f'lista:{l1}')
else:
    print(f'voce escolheu parar!A lista finalizou assim:{l1}')
#EX3#
print('TERCEIRO EX')
X=str(input('digite uma palavra:'))
print('palavra original:',X)

for x in range(len(X)+1):
    print(X[:x])
for i in range(len(X)):
    print(X[:-i])

#EX4#
print('QUARTO EX')
x1=str(input('Digite a frase de sua escolha:'))
c=x1.lower()
o=c[::-1]
if o==c:
    print('É uma frase palíndromo.')
else:
    print('Não é uma frase palíndromo')

#EX5# #maior elemento da linha do menor elemento#
'''Contagem do exercicio a partir do ZERO'''
print('QUINTO EX:')
#matrizprovas
Matriz=[]
N = int(3)
M = int(4)
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
maior=Matriz[0][0]
linhamaior=0
for i in range(N):
    for j in range(N):
        if (Matriz[i][j]<maior):
            maior=Matriz[i][j]
            linhamaior=i
menor=Matriz[linhamaior][0]
colunamenor=0
for j in range(M):
    if (Matriz[linhamaior][j]>menor):
        menor=Matriz[linhamaior][j]
        colunamenor=j
print('posicao:linha' ,linhamaior, 'e coluna' ,colunamenor)







        









