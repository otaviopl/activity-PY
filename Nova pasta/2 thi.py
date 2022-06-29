
def reading_file():
    urna=open('votos.txt')
    counter_votes = 0
    counter_random = 0
    counter_100 = 0
    counter_200 = 0
    counter_300 = 0
    counter_400 = 0
    counter_500 = 0

    for votos in urna:
        counter_votes += 1
        if "100" in votos:
            counter_100 += 1
        if "200" in votos:
            counter_200 += 1
        if "300" in votos:
            counter_300 += 1
        if "400" in votos:
            counter_400 += 1
        if "500" in votos:
            counter_500 += 1

    if counter_100 > counter_200 and counter_100 > counter_300 and counter_100 > counter_400 and counter_100 > counter_500:
        print("O vencedor da eleição foi o candidato 100, com ",
            counter_100, " votos!")
    if counter_200 > counter_100 and counter_200 > counter_300 and counter_200 > counter_400 and counter_200 > counter_500:
        print("O vencedor da eleição foi o candidato 200, com ",
            counter_200, " votos!")
    if counter_300 > counter_100 and counter_300 > counter_200 and counter_300 > counter_400 and counter_300 > counter_500:
        print("O vencedor da eleição foi o candidato 300, com ",
            counter_300, " votos!")
    if counter_400 > counter_100 and counter_400 > counter_200 and counter_400 > counter_300 and counter_400 > counter_500:
        print("O vencedor da eleição foi o candidato 400, com ",
            counter_400, " votos!")
    if counter_500 > counter_100 and counter_500 > counter_200 and counter_500 > counter_300 and counter_500 > counter_400:
        print("O vencedor da eleição foi o candidato 500, com ",
            counter_500, " votos!")

    if counter_100 < counter_200 and counter_100 < counter_300 and counter_100 < counter_400 and counter_100 < counter_500:
        print(f"O candidato menos votado foi o candidato 100, com {counter_votes} votos!")
    if counter_200 < counter_100 and counter_200 < counter_300 and counter_200 < counter_400 and counter_200 < counter_500:
        print(f"O candidato menos votado foi o candidato 200, com {counter_200} votos!")
    if counter_300 < counter_100 and counter_300 < counter_200 and counter_300 < counter_400 and counter_300 < counter_500:
        print("O candidato menos votado foi o candidato 300, com ",
            counter_300, " votos!")
    if counter_400 < counter_100 and counter_400 < counter_200 and counter_400 < counter_300 and counter_400 < counter_500:
        print("O candidato menos votado foi o candidato 400, com ",
            counter_400, " votos!")
    if counter_500 < counter_100 and counter_500 < counter_200 and counter_500 < counter_300 and counter_500 < counter_400:
        print("O candidato menos votado foi o candidato 500, com ",
            counter_500, " votos!")
    counter_random = (counter_votes - (counter_100 + counter_200 +
                      counter_300 + counter_400 + counter_500))
    print("A quantidade de votos nulos da eleição foi de:", counter_random)

def menu():
    opcao = int(input("1-registrar/2-VER"))
    while opcao == 1:
        votos = []
        
        if opcao == 1:
            with open('votos.txt', 'a') as urna:
                voto = int(
                    input("Os candidatos são: 100, 200, 300, 400, 500\nDigite seu voto: "))
                urna.write(str(voto) + '\n')
    else:
        reading_file()
menu()