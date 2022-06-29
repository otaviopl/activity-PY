def menu():
    print('1-Cadastrar uma nova pessoa:')
    print('2- Ver os dados.')
    a=input('digite o numero correspondente:')
    while a=='1':
        getting_infos()
    while a=='2':
        read_file()



def getting_infos():
    print('Olá, seja bem vindo a entrevista do IBOP')
    sex=input('Digite o número correspondendo do seu sexo:: Masculino:1:/ Feminino:2:/.')
    if sex=="1":
        sex="masculino"
    if sex=="2":
        sex="feminino"
    age=input('Digite sua idade::')
    smoke=input('Você é fumante? Sim:sim:/ Não:nao:/.')
    school=input('Digite o número correspondente à sua escolaridade::Fundamental:1:/ Médio:2:/ Superior:3:/')
    if school=="1":
        school="fundamental"
    if school=="2":
        school="medio"
    if school=="3":
        school=="superior"
    else:
        print('opção não dísponivel')

    arq=open("pesquisa.txt","a")
    arq.write("\n")
    arq.write(sex)
    arq.write(" ")
    arq.write(age)
    arq.write(" ")
    arq.write(smoke)
    arq.write(" ")
    arq.write(school)
    arq.write(" ")
    
    arq.close() 
    return(menu())

def read_file():
  
    all_data = []
    all_lines = []
    contador=0
    
    with open("pesquisa.txt") as f:
        all_lines = f.readlines()
        for single_line in all_lines:
            if single_line:
                contador+=1
    sub="sim"
    count_afirmatives=single_line.count(sub)
    print(f'A quantidade de pessoas fumantes foi de {count_afirmatives/contador*100}%')
    for single_line in all_lines:
        single_line = single_line.replace("\n", "")
        single_entry = single_line.split(" ")
        all_data.append(single_entry)
    print(all_data)

    
    non_new_smokers = 0
    count_mens=0
    for single_entry in all_data:
        if single_entry[0]=="masculino":
            count_mens+=1
    for single_entry in all_data:
        single_entry[1]=int(single_entry[1])
        if single_entry[0] == "masculino" and single_entry[1] < 40 and single_entry[2] == "nao":
            non_new_smokers += 1
            print(f"A porcentagem de nao fumantes a baixo de 40 anos é de:{non_new_smokers/count_mens*100}%")
    counter_ladies=0
    counter_lady=0
    for single_entry in all_data:
        if single_entry[0]=="feminino":
            counter_ladies+=1
    for single_entry in all_data:
        if single_entry[0] == "feminino" and single_entry[1] > 40 and single_entry[2] =='sim':
            counter_lady+=1
    print(f'A porcentagem de mulheres fumantes a cima de 40 anos é de: {counter_lady/counter_ladies*100}')
    return(menu())

menu()