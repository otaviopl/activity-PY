#listas usadas#
#modelo usado na lista (FILMES): CODIGO/ NOME/ ANO/ DIRETOR/ATORES
#modeulo usado na lista(salas): CODIGO/ NOME/ EXIBICAO/ ACESSIBILIDADE


listafilmes = [
                            ["123","Lucas e Otávio 1: A aventura começa.","2019","Cris bom",["Lucas","Otávio "]],
                            ["456","Lucas e Otávio 2: A aventura continua","2022","Cris bom",["Lucas", "Otávio"]],
                            ["789","The Batman 2","2022","Alan zika",["Nicolas Cage", "WILL SMITH", "SCARLETT JOHANSSON","KEANU REEVES"]],
                            ["987","The Batman ","2017","Alan zika",["ROBERT PATTINSON",  "ZOË KRAVITZ", "PAUL DANO", "COLIN FARRELL", "ANDY SERKIS", "JEFFREY WRIGHT"]]]                 
salas1 = [
            ["1213","Sala azul","305","2D/3D","cadeirantes e obesos"],
            ["1415","Sala vermelha","300","3D","obesos"],
            ["1617","Sala amarela","205","2D","cadeirantes e obesos"],
            ["1819","Sala verde","200","3D","besos"],
            ["2021","Sala preta","155","2D/3D","cadeirantes"],
            ["2022","Sala cinza","150","2D","cadeirantes e obesos"]
          ]
#modelo: Nome sessao/ data/ cod_filme / cod_sala / hora / preço
dic_sessao = {'Sessao1': ('07/04/2022...' '123...' '1213...' '21:00...' '15 reais...'),'Sessao2': ('08/05/2022...' '456...' '1415...' '22:00hrs...' '15 reais...')}

#começando as funcoes#
#FUNCOES SALAS#
def cadastrar(salas1):
    lista_cadastro=[]
    codigo=input("Codigo desta sala:")
    for i in salas1:
        if i[0]==codigo:
            print('Este codigo ja existe, por favor insira outro...')
            return menu(salas1)
        else:
            lista_cadastro.append(codigo)
            nome = input("Nome da sala:")
            capacidade = input("Capacidade da sala:")
            exibicao = input("Exibicao:")
            acessibilidade = input("Acessibilidade:")
            lista_cadastro.append(nome)
            lista_cadastro.append(capacidade)
            lista_cadastro.append(exibicao)
            lista_cadastro.append(acessibilidade)
            
            salas1.append(lista_cadastro)
            print(salas1)
            escrever_alteracoes_salas() 
            return menu(salas1)

def listar(salas1):
    for sala in salas1:
        codigo,nome, capacidade, exibicao, acessibilidade = sala
        print(f" Codigo: {codigo}, Nome: {nome}, capacidade: {capacidade}, tipo de exibição {exibicao}, acessibilidade: {acessibilidade}")

def buscar(salas1):
    nome_da_sala = input(" nome: ")
    for plut in salas1:
        codigo,nome, capacidade, exibicao,acessibilidade, = plut
        if nome == nome_da_sala:
            print('Sala achada!!')
            print(f"Codigo: {codigo}, Nome: {nome},Capacidade: {capacidade},tipo de Exibição: {exibicao}, Acessibilidade: {acessibilidade}")
            return menu(salas1)
        else:
            print(f"Buscando sala com nome '{nome_da_sala}'...não encontrada")
            return menu(salas1)

#codigo/nome/capacidade/exibi/acess
def alterar (salas1):
    print("*** Alterar uma sala ***")
    cod = str(input("Insira o Código do filme a ser Alterado: "))
    for c in listafilmes:
        if c[0] == cod:
            print("O que será alterado na sala:",c,"?\n1. Código\n2. Nome\n 3.capacidade\n 4.exibicao \n5.acessibilidade \n6.Voltar")
            esc = int(input("Insira a opção a ser alterada: "))
            if esc == 1:
                cod1 = str(input("Digite o novo Código:"))
                c[0] = cod1
                print("A sala foi alterado com sucesso!",c)
                escrever_alteracoes_salas()
                print("Voltando ao Menu Principal...")
                return menu(salas1)
            elif esc == 2:
                novo_nome = str(input("Digite o novo nome da sala em questao. "))
                c[1] = novo_nome
                print("O filme foi alterado com sucesso!",c)
                escrever_alteracoes_salas()
                print("Voltando ao Menu Principal...")
                return menu(salas1)
            elif esc==3:
                nova_capcidade=str(input('digite a nova capacidade da sala...(200)'))
                c[2]=nova_capcidade
                print('a sala foi alterada com sucesso!')
                escrever_alteracoes_salas()
                print('voltando ao menu principal!')
                return menu(salas1)
            elif esc==4:
                nova_exi=str(input('digite a nova exibicao da sala?'))
                c[3]=nova_exi
                print('a sala foi alterada com sucesso.')
                escrever_alteracoes_salas()
                print('voltando ao menu principal...')
                return menu(salas1)
            elif esc==5:
                nova_acess=str(input('Digite a nova acessibilidade..'))
                c[4]=nova_acess
                print('A sala foi alterada com sucesso.')
                escrever_alteracoes_salas()
                print('voltando ao menu principal...')
                return menu(salas1)
            elif esc==5:
                print('voltando ao menu principal...')
                return menu(salas1)
            else:
                print("Opção inválida")
                return menu(salas1)            
   
  

def excluir(salas1):
    identif_desejado = input("nome: ")
    index = 0    
    for sala in salas1:
        if sala[1] == identif_desejado:
              salas1.pop(index)
    print(salas1)
    escrever_alteracoes_salas()
    return menu(salas1)
   

def listar1(salas1):
    print("*** Salas Disponíveis ***\n1. Listar todas as salas\n2. Listar uma sala em específico.\n3. Incluir uma sala\n4. Alterar uma sala.\n5. Excluir uma sala.\n6. Voltar ao Menu Principal.")
    opcao = int(input("Insira a opção desejada: "))
    if opcao == 1:
        listar(salas1)
    elif opcao == 2:
        buscar(salas1)    
    elif opcao == 3:
        cadastrar(salas1)   
    elif opcao == 4:
        alterar(salas1)   
    elif opcao == 5:
        excluir(salas1)
    elif opcao == 6:
        menu(salas1)
#FUNCOES PARA FILMES#
def filmes(listafilmes):
    print("*** Filmes: ***\n1. Listar todos os filmes.\n2. Listar um filme.\n3. Incluir um filme.\n4. Alterar um filme.\n5. Excluir um filme.\n6. Voltar ao Menu Principal.")
    opcao = int(input("O que você quer fazer? "))
    if opcao == 1:
        print("*** Listar todos os filmes dispovíveis ***")
        print("Todos os filmes são: ")
        print(listafilmes)
        return menu(salas1)


    elif opcao==2:
        print("Mostrar um filme em específico:")
        codigo_filme = input(" codigo do filme desejado: ")
        for plut in listafilmes:
            codigo,nome, ano , diretor, atores = plut
        if codigo == codigo_filme:
            print('Filme achado!!')
            print(f"Codigo: {codigo}, Nome: {nome}, ano: {ano}, diretor: {diretor}, atores: {atores}")
            return menu(salas1)
        else:
            print(f"Buscando filme com codigo '{codigo_filme}'...não encontrada")
            return menu(salas1)
    elif opcao == 3:
        print("*** Inserir um novo filme ***")
        lista_cadastro=[]
        codigo=input("Codigo do filme:")
        for i in salas1:
            if i[0]==codigo:
                print('Este codigo ja existe, por favor insira outro...')
                return menu(salas1)
        else:
            lista_cadastro.append(codigo)
            nome = input("Nome do filme:")
            capacidade = input("ano do filme")
            exibicao = input("diretor do filme")
            acessibilidade = input("elenco:")
            lista_cadastro.append(nome)
            lista_cadastro.append(capacidade)
            lista_cadastro.append(exibicao)
            lista_cadastro.append(acessibilidade)
            
            listafilmes.append(lista_cadastro)
            print(listafilmes)
            escrever_alteracoes_filmes()
            return menu(salas1)
#modelo usado na lista (FILMES): CODIGO/ NOME/ ANO/ DIRETOR/ATORES
    elif opcao == 4:
        print("*** Alterar um filme em específico ***")
        cod = str(input("Insira o Código do filme a ser Alterado: "))
        for c in listafilmes:
            if c[0] == cod:
                print("O que será alterado no filme:",c,"?\n1. Código\n2. Nome\n 3.Ano\n 4.Diretor \n5.Elenco \n6.Voltar")
                esc = int(input("Insira a opção a ser alterada: "))
                if esc == 1:
                    cod1 = str(input("Digite o novo Código:"))
                    c[0] = cod1
                    print("O filme foi alterado com sucesso!",c)
                    escrever_alteracoes_filmes()
                    print("Voltando ao Menu Principal...")
                    return menu(salas1)
                if esc == 2:
                    novo_nome = str(input("Digite o nono nome do filme em questao. "))
                    c[1] = novo_nome
                    print("O filme foi alterado com sucesso!",c)
                    escrever_alteracoes_filmes()
                    print("Voltando ao Menu Principal...")
                    return menu(salas1)
                
                if esc == 4:
                    ano_novo= str(input("Digite o novo ano do filme:"))
                    c[3] = ano_novo
                    print("O filme foi alterado com sucesso!",c)
                    escrever_alteracoes_filmes()
                    print("Voltando ao Menu Principal...")
                    return menu(salas1)
                if esc == 5:
                    novo_diretor= str(input("Digite o novo diretor do filme: "))
                    c[4] = novo_diretor
                    print("O filme foi alterado com sucesso!",c)
                    escrever_alteracoes_filmes()
                    print("Voltando ao Menu Principal...")
                    return menu(salas1)
                if esc == 6:
                    print("Voltando ao Menu Principal...")
                    escrever_alteracoes_filmes()
                    return menu(salas1)
            
            else:
                print("O Código",cod,"não foi encontrado, voltando ao Menu Principal!")
                menu(salas1)

    elif opcao == 5:
        print("*** Excluir um filme***")
        cod = str(input("Insira o Código do filme que deseja excluir: "))
        for c in filmes:
            if c[0] == cod:
                print(f"Deseja excluir o filme:{c}: ")
                escolha = int(input("1. Sim\n2. Não\n"))
                if escolha == 1:
                    filmes.remove(c)
                    print("Filme foi excluido!")
                    print(listafilmes)
                    escrever_alteracoes_filmes()
                    print("Voltando ao Menu Principal...")
                    menu(salas1)
                if escolha == 2:
                    print("Voltando ao Menu Principal...")
                    menu(salas1)
            else:
                print("O Código",cod,"não foi encontrado, voltando ao Menu Principal!")
                menu(salas1)

    elif opcao == 6:
        print("Voltando ao Menu Principal...")
        menu(salas1)

    else:
        print("Opção Inválida!")
        print("Voltando ao Menu Principal...")
        menu(salas1)

def sessao_todos(dic_sessao):
    print('Mostrar todas as sessoes disponiveis:')
    print('modelo: Nome sessao/ data/ cod_filme / cod_sala / hora / preço')
    print(dic_sessao.items())
    return menu(salas1)
         
    

def sessao_especifico():
    print('Mostrando uma sessão em esécífico:')
    nome_sessao=input('digite o nome da sessão que deseja vizualizar:')
    for key in dic_sessao.keys():
        if nome_sessao==key:
            print(dic_sessao.get(key))
            return menu(salas1)
        else:
            print('Não achei a sessao citada...')
            return menu(salas1)

def sessao_cadastrar():
    print('Adicionando uma sessao...')
    for key in dic_sessao.keys():
        print(key)
        nome=input('qual é o nome da sessao que deseja adicionar?')
        if nome!=key:
           data=input('Qual é a data desta sessao?')
           codigo_filme=input('Qual é o codigo deste filme?')
           codigo_sala=input('Qual é o codigo desta sala?')
           hora=input('Qual hhorario esta sessao vai acontecer?')
           preco=input('Quanto vai ser o preco do ingresso?')
           dic_sessao[nome]= data,'...',codigo_filme,'...',codigo_sala,'...',hora, '....',preco
           print(dic_sessao)
           escrever_alteracoes_sessoes()
           return menu(salas1)
        else:
            print('nome ja existe, por favor insira outro...')
            return menu(salas1)

def sessao_alterar():
    print('alterando uma sessao...')
    for key in dic_sessao.keys():
        nome=input('qual é o nome da sessao que voce deseja alterar?')
        if nome==key:
            desejo=int(input('o que deseja alterar na sessao?\n1-->nome//\n2-->data//\n3-->codigo do filme//\n4-->codigo da sala//\n5-->hora da sessao\n6-->preço do ingresso//\n7-->sair'))
            if desejo==1:
                novo_nome=input('Qual é o novo nome da sessao?')
                dic_sessao[nome]=dic_sessao[novo_nome]
                print(dic_sessao)
                escrever_alteracoes_sessoes()
                return menu(salas1)
            elif desejo==2:
                nova_data=input('Qual é a nova data da sessao?(!07/04/2004!)')
                for valor in dic_sessao.values():
                    valor[0]==nova_data
                    print(dic_sessao)
                    escrever_alteracoes_sessoes()
                    return menu(salas1)
            elif desejo==3:
                novo_filme=input('Qual é o novo codigo do filme?')
                for codigos in listafilmes:
                    if novo_filme in codigos:
                        print('codigo aceito.')
                        for valor in dic_sessao.values():
                            valor[1]==novo_filme
                            print(dic_sessao)
                            escrever_alteracoes_sessoes()
                            return menu(salas1)
                    else:
                        print('codigo inexistente')
                        return menu(salas1)
            elif desejo==4:
                nova_sala=int(input('Qual é o novo codigo de sala?'))
                
                for codigos_salas in salas1:
                    if nova_sala in codigos_salas:
                        print('codigo aceito')
                        for valor in dic_sessao.values():
                            valor[2]==nova_sala
                            print(dic_sessao)
                            escrever_alteracoes_sessoes()
                            return menu(salas1)
            elif desejo==5:
                nova_hora=input('Qual é a nova hora desejada? 21:00hrs')
                for valor in dic_sessao.values():
                    valor[3]==nova_hora
                    print(dic_sessao)
                    escrever_alteracoes_sessoes()
                    return menu(salas1)
            elif desejo==6:
                novo_preco=input('Insira o novo preço:15 reais')
                for valor in dic_sessao.values():
                    valor[4]=novo_preco
                    print(dic_sessao)
                    escrever_alteracoes_sessoes()
                    return menu(salas1)
            else:
                return menu(salas1)

                


def sessao_excluir():
    print('Excluindo uma sessao...')
    nome_sessao=input('Escreva o nome da sessao que deseja excluir...')
    ctz=int(input('Tem certeza que deseja excluir esta sessao?1--sim//2--nao'))
    if ctz==1:
        for key in dic_sessao.keys():
            if nome_sessao==key:
                del dic_sessao[key]
                print('exlcuida.')
                print(dic_sessao)
                escrever_alteracoes_sessoes()
                return menu(salas1)
    else:
        print('ok...voltando...')
        return menu(salas1)
            
def filmes_relatorio():
    
    print('relatando filmes desejados:')
    ano=input('A partir de qual ano voce deseja ver?')
    for anos in listafilmes:
        if anos[2]>=ano:
            print(anos)
            return menu(salas1)

def salas_relatorio():
    print('relatando salas desejadas...')
    capa=int(input('Qual é a capacidade das salas desejadas?'))
    exi=input('qual é o tipo de exbicicao desejada?  1-->2d\n//2-->3d//\n3-->2d/3d')
    if exi==1:
        exi=='2D'
        for exibicao in salas1:
            if exibicao[3]==exi and capa==exibicao[2]:
                print(exibicao)
                return menu(salas1)
    elif exi==2:
        exi=='3D'
        for exibicao in salas1:
            if exibicao[3]==exi and capa==exibicao[2]:
                print(exibicao)
                return menu(salas1)
    else:
        exi=='2D/3D'
        for exibicao in salas1:
            if exibicao[3]==exi and capa==exibicao[2]:
                print(exibicao)
                return menu(salas1)









def relatorios():
    print("*** Relatórios ***\n1.Filmes--relatórios.\n2.Salas--relatório.\n3.Sessoes--relatórios 4.Voltar ao Menu Principal.")
    opcao=int(input('Qual opcao deseja?'))
    if opcao==1:
        filmes_relatorio()
        return menu(salas1)
    elif opcao==2:
        salas_relatorio()
        return menu(salas1)
    elif opcao==3:
        relatorio_sessao()
        return menu(salas1)
    else:
        print('opcao invalida...')
        return menu(salas1)

        
    
def sessao(dic_sessao):
    print("*** Sessões ***\n1. Listar todas as sessões.\n2. Listar uma sessão.\n3. Incluir uma sessão.\n4. Alterar uma sessão.\n5. Excluir uma sessão.\n6. Voltar ao Menu Principal.")
    opcao=int(input('Qual das opções deseja?'))
    if opcao==1:
        sessao_todos(dic_sessao)
        return menu(salas1)
    elif opcao==2:
        sessao_especifico()
        return menu(salas1)
    elif opcao==3:
        sessao_cadastrar()
        return menu(salas1)
    elif opcao==4:
        sessao_alterar()
        return menu(salas1)
    elif opcao==5:
        sessao_excluir()
        return menu(salas1)
    else:
        return menu(salas1)
#escrever no arquivo  
def escrever_alteracoes_salas():
    print('escrevendo no banco de dados...')
    arq=open('dadossalas.txt','a')
    arq.write("\n".join(salas1))
    
    arq.close()

    print('sucesso!')

def escrever_alteracoes_filmes():
    print('escrevendo no banco de dados...')
    arq=open('dadosfilmes.txt','a')
    arq.write("\n".join(listafilmes))
    
    arq.close()

    print('sucesso!')

def escrever_alteracoes_sessoes():
    print('escrevendo no banco de dados...')
    arq=open('dadoscinema.txt','a')
    arq.write("\n".join(dic_sessao))
    arq.close()

    print('sucesso!')
    
def relatorio_sessao():
    print('progresso')
    data=input('Digite a data inicial que deseja ver sessoes: (dd/mm/aaaa)')
    data2=input('Digite a data final que deseja ver as sessoes: (dd/mm/aaaa')
    print(f'Anotado... Voce deseja ver as sessoes do dia {data} até o dia data2{data2}')
    data=data.split('/')
    data2=data2.split('/')
    for datas in dic_sessao.values():
        print(datas)
############################################################################################################
def menu(salas1):
    print("*** Menu Principal *** \n1. Submenu de Salas\n2. Submenu de Filmes\n3. Submenu de Relatórios\n4. Submenu de Sessões\n 5. Sair")
    opcao = int(input("Insira a opção desejada: "))
    if opcao == 1:
        listar1(salas1)
    elif opcao== 2:
        filmes(listafilmes)
    elif opcao==3:
        relatorios()
    elif opcao==4:
        sessao(dic_sessao)      
    elif opcao==5:
        print('saindo...')
    else:
        print("Opção Inválida")
        menu(salas1)
############################################################################################################   
menu(salas1)