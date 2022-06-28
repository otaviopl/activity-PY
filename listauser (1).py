lista=[]
mai=0
men=0
for x in range(0,11):
    lista.append(int(input(f'Forneça um numero para adicionar na lista:{x}:')))
    if x==0:
        mai=lista[x]
    else:
        if lista [x]>mai:
            mai=lista[x]
    if x==0:
        men=lista[x]
    else:
        if lista [x]<men:
            men=lista[x]

soma = 0
for i in range(len(lista)):
    soma += lista[i]

for x in range(1,11):
    if x%3==0:
        print('numeros impares:',x,)
        
if x > 18:
    print('maiores que 18:',x)
        
print('lista esta desta forma:',lista)
print('maior numero ate agora:',mai)
print('menor numero ate agora:',men)
print('soma é:',soma)
