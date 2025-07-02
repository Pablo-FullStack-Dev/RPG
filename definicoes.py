import json
import os
import random
numeros_disponiveis = list(range(1, 11))
# Configurações:

def salvar(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)


def carregar_dados(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def dados():
    # Dicionário com todos os dados possíveis
    dados_possiveis = {
        "d4": list(range(1, 5)),
        "d6": list(range(1, 7)),
        "d8": list(range(1, 9)),
        "d10": list(range(1, 11)),
        "d12": list(range(1, 13)),
        "d20": list(range(1, 21)),
        "d100": list(range(1, 101))
    }

    while True:
        qu = input("\nQual dado usar?\n1. D4\n2. D6\n3. D8\n4. D10\n5. D12\n6. D20\n7. D100\n0. Sair\n-> ").lower().strip()
        if qu in ["0", "sair", "encerrar"]:
            break

        chave = {
            "1": "d4", "d4": "d4",
            "2": "d6", "d6": "d6",
            "3": "d8", "d8": "d8",
            "4": "d10", "d10": "d10",
            "5": "d12", "d12": "d12",
            "6": "d20", "d20": "d20",
            "7": "d100", "d100": "d100"
        }.get(qu)

        if chave and dados_possiveis[chave]:
            numero = random.choice(dados_possiveis[chave])
            dados_possiveis[chave].remove(numero)
            print(f"\nResultado do {chave.upper()}: {numero}")
        elif chave:
            print(f"\n⚠️ Todos os valores do {chave.upper()} já foram sorteados! Reiniciando lista...")
            dados_possiveis[chave] = list(range(1, int(chave[1:]) + 1))
        else:
            print("\nErro de digitação! Tente novamente.")

    return "\nFIM DOS DADOS"

# PERSONAGEM:
def adicionar_avatar(): 
    arquivo = "avatares.json"
    #vamos carregar os dados antigos:
    
    avatares = carregar_dados(caminho=arquivo)
    if len(avatares) == 1:
        return "Vc já tem um avatar"
    # vamos adicionar os novos arquivos:
    cor = str(input('\ndescreva a coloração do personagem: '))
    experiencia = str(input('\ndigite a experiencia do personagem: '))
    nome = str(input('\ndigite o nome do seu personagem: '))
    classe= str(input('\ndigite a classe do seu personagem:  '))
    nivel= int(input('\nQual o nivel do seu personagem:  '))
    vida = int(input("digite a vida/hp do seu personagem: "))
    mana = int(input("Digite a mana do seu personagem: "))
    personalidade= str(input('\ndigite a personalidade do personagem: '))
    avatar = {
        "nome": nome,
        "nivel": nivel,
        "vida": vida,
        "mana": mana,
        "classe": classe,
        "personalidade": personalidade,
        "experiencia": experiencia,
        "cor": cor
    }

    
    avatares.append(avatar)
    # agora vamos adicionar ambos os arquivos:
    salvar(caminho=arquivo, dados=avatares)
        
    return "Personagem adicionado"



def adicionar_armadura(): 
    arquivo = "equipamentos.json"
    # vamos carregar os antigos arquivos:
    
    equipamentos = carregar_dados(caminho=arquivo)
    #adicionando novos equipamentos
    elmo = str(input('digite o nome do elmo: '))
    forca_elmo = int(input('digite a resistencia do elmo: '))
    peitoral = str(input('digite o nome do peitoral'))
    forca_peitoral = int(input('digite a resistencia do peitoral: '))
    calca = str(input('digite o nome da calça: '))
    forca_calca = int(input('digite a resistencia da calça: '))
    bota = str(input('digite o nome da bota: '))
    forca_bota = int(input('digite a resistencia da bota: '))
    colar = str(input('digite o nome do colar'))
    anel = str(input('digite o nome do anel'))
    equipamento = {
        "elmo": elmo,
        "peitoral": peitoral,
        "calça": calca,
        "bota": bota,
        "colar": colar,
        "anel": anel
    }
    equipamentos.append(equipamento)

    #vamos salvar todos os equipamentos:
    salvar(caminho=arquivo,dados=equipamentos)
    
    return "\nEquipamento adicionado"

def inserir_atributos(): # terminar de atualizar o rpg pro json
    # Carregando os dados antigos:
    atributos = carregar_dados(caminho="atributos.json")
    #criando novos arquivos: 
    força = int(input('digite a aqui a força: '))
    destreza = str(input('digite a aqui a destreza: '))
    inteligencia = str(input('digite a inteligencia: '))
    sabedoria = str(input('digite a sabedoria: '))
    constituicao = str(input('digite a constituicao: '))
    carisma = str(input('digite a carisma: '))
    velocidade = int(input('digite a aqui a velocidade: '))
    peso = int(input('escreva o peso do seu personagem: '))
    atributo = {
        "força": força,
        "destreza": destreza,
        "inteligencia": inteligencia,
        "sabedoria": sabedoria,
        "constituicao": constituicao,
        "carisma": carisma,
        "velocidade": velocidade,
        "peso": peso
    }
    atributos.append(atributo)
    #salvando os novos e os antigos arquivos:
    salvar(caminho="atributos.json", dados=atributos)
    return "\nAtributos e adicionado"


        
 #   
#-------------------------------VIZUALIZAÇÃO-----------------------------------------------

def vizu_avatar():
    avatares = carregar_dados(caminho="avatares.json")
    for avatar in avatares:
        print(f'''

              Nome: {avatar["nome"]}
              nivel: {avatar["nivel"]}
              Vida: {avatar["vida"]}
              Mana: {avatar["mana"]}
              Classe: {avatar["classe"]}
              Personalidade: {avatar["personalidade"]}
              Experiencia: {avatar["experiencia"]}              
              Cor: {avatar["cor"]}
''')

    return ""

def vizu_armadura():
    equipamentos = carregar_dados(caminho="equipamentos.json")
    for equipamento in equipamentos:
        print(f'''
                        Elmo: {equipamento["elmo"]}
                        Peitoral: {equipamento["peitoral"]}
                        Calça: {equipamento["calça"]}
                        Bota: {equipamento["bota"]}
                        Colar: {equipamento["colar"]}
                        Anel: {equipamento["anel"]}
                       ''')
    return ""

def vizu_inimigos():
    personagens = carregar_dados("personagens.json")
    for personagem in personagens:
        print(f'''
              Nome: {personagem["nome"]}
              Vida: {personagem["vida"]}
              Estamina: {personagem["estamina"]}
              Resistência: {personagem["resistencia"]}
              Ataque: {personagem["ataque"]}
              Escudo: {personagem["escudo"]}
              Alma: {personagem["alma"]}''')
    return ""

def vizu_itens():
    itens = carregar_dados(caminho="itens.json")
    for item in itens:
        print(f'''
                  Nome:{item['nome']}
                  Dano:{item['dano']}
                  Tipo:{item['tipo']}''')
    return "" 


def vizualizar():#  1.Avatar/ 2. Armadura/ 3. inimigos/ 4. itens
    while True:
        question = str.lower(input('''
Vc gostaria de ver: 
                    1.avatares ou 
                    2.armaduras 
                    3.lista de inimigos
                    4. itens 
                    0. para voltar
--> '''))
        if question in ["0", "encerrar"]:
            return "\nFIM DA LISTA\n"
        elif question in ["avatares", "avatar", "1"]:
            print(vizu_avatar())
        elif question in ["armaduras", "armadura", "2"]:
            print(vizu_armadura())
        elif question in ["inimigos", "3"]:
            print(vizu_inimigos()) 
        elif question in ["itens"]:
            print(vizu_itens())
        else:
            print("\nERRO DE DIGITAÇÃO!!\n")
#-------------------------------NPC---------------------------------------------------------



def adicionar_npc():
    personagens = carregar_dados(caminho="personagens.json")

    #agora vamos colocar um novo personagem: 
    nome = str(input('escreva o nome: '))
    vida = int(input('escreva a vida: '))
    estamina = int(input('escreva a estamina: '))
    resistencia = int(input('escreva resistencia: '))
    ataque = int(input('escreva o dano: '))
    escudo = int(input('escreva a defesa: '))
    alma = str(input('escreva o tipo de alma: '))
    personagem = {
        "nome": nome,
        "vida": vida,
        "estamina": estamina,
        "resistencia": resistencia,
        "ataque": ataque,
        "escudo": escudo,
        "alma": alma
    }
    personagens.append(personagem)

    #agora vamos salvar o novo personagem e os antigos personagens:
    salvar(caminho="personagens.json", dados=personagens)
    return "\nNPC criado e salvo."


# INVENTÁRIO: 

def criar_item():
    # se não existia agora existe:
    arquivo = "itens.json"

    # lê e carrega os dados antigos pra salvar com os novos: 
   
    itens = carregar_dados(caminho=arquivo)

    nome = str(input('\nEscreva o nome do item: '))
    dano = int(input('\nEscreva o dano do item: '))
    tipo = str(input('\nEscreva que tipo de item ele é: '))
    item = {
        "nome": nome,
        "dano": dano,
        "tipo": tipo
    }
    itens.append(item)
    #Agora é salvar os itens:
    salvar(caminho="itens.json", dados=itens)
    return "item adicionado ao invetário"



#--------------------------------funções do APPA ---------------------------------------------------


def escolhendo():
    
    
    while True: #   Escolha do oponente:
        #carregando arquivo OPONENTES.JSON
        # arquivo = "oponentes.json"
        # with open(arquivo, "r", encoding="utf-8") as f:
        #     oponentes = json.load(f)
        oponentes = carregar_dados(caminho="personagens.json")
        for amostras in oponentes: #só pra mostrar a lista de personagens!
            print(amostras)
        
        jogador_one = str(input("digite o nome de um Avatar inimigo: "))
        for oponente in oponentes: # especificando o personagem 
            if oponente["nome"].lower() == jogador_one.lower():
                print(f"vc escolheu {oponente['nome']} para lutar\n")
                vermelho = {
        "nome": oponente['nome'],
        "classe": oponente['classe'],
        "nivel": oponente['nivel'],
        "grau": oponente['grau'],
        "experiencia": oponente['experiencia'],
        "vida": oponente['vida'],
        "mana": oponente['vida'],
        "escolhido": True} 
                nome_inimigo = []
                nome_inimigo.append(vermelho)
                salvar(caminho="time_vermelho.json", dados=nome_inimigo)
                 # Adiciona ao tima vermelho


                
        #-----------------------------------------------------------------------

        
        avatares = carregar_dados(caminho="avatares.json") # Carregando o arquivo dos avatares
        for mostrar in avatares:
            print(mostrar)
        jogador_second = str(input("Digite o nome do seu avatar: "))
        for avatar in avatares:
            if avatar["nome"].lower() == jogador_second.lower():
                azul = {
        "nome": avatar['nome'],
        "classe": avatar['classe'],
        "nivel": avatar['nivel'],
        "grau": avatar['grau'],
        "experiencia": avatar['experiencia'],
        "vida": avatar['vida'],
        "mana": avatar['mana'],
        "escolhido": True
    }
                nome_heroi = []
                nome_heroi.append(azul)

                salvar(caminho="time_azul.json", dados=nome_heroi)
                return f""
                 # adiciona ao time azul
        break
     
    return f"\n...\n" 

def defesa():
    if not numeros_disponiveis:
        return "Todos os números já foram sorteados!"
    
    numero = random.choice(numeros_disponiveis)
    numeros_disponiveis.remove(numero)
    return numero


def batalha():
    escolhendo()
    inimigos = carregar_dados(caminho="time_vermelho.json")
    avatares = carregar_dados(caminho="time_azul.json")
    escolhido = True
    while True:
        quest = str(input("Deseja:\n 1. soco\n2.verificar status do avatar\n3. Defender proximo ataque\n.0 encerrar\n--> "))
        if quest in ["0", "encerrar"]:
            return "\n...\n"
        elif quest in ["1", "soco"]:
           for inimigo in inimigos:
               if inimigo["vida"] == 0:
                   print(f'\nO {inimigo["nome"]} está morto\n')
                   break
               if defesa() > 5:
                   print("a defesa do goblin não permitiu seu ataque")
                   break
               if inimigo["escolhido"] == escolhido:
                print(f"\n{inimigo}\n")
                vida = inimigo["vida"] 
                vida -= 5
                inimigo["vida"] = vida
                salvar(caminho="time_vermelho.json", dados=inimigos)

        elif quest in ["2", "verificar status", "verificar", "verificar avatar"]:
             
            for avatar in avatares:
                if avatar:
                    
                    break
        else:
            print(f"\nERRO!\n")

def restaurar_hp():
    while True:
        quest = str(input("quer regenerar seu 1.avatar ou o 2.inimigo?"))
        oponentes = carregar_dados(caminho="oponentes.json")
        avatares = carregar_dados(caminho="avatares.json")
        if quest in ["a"]:
            print("\nERRO!\n")  

        elif quest in ["1", "avatar"]:
            for avatar in avatares:
                if avatar["vida"] <= 0:
                    avatar["vida"] += 5
                    salvar(caminho="avatares.json", dados=avatares)
                    return "A vida do avatar foi restaurada"
            
        elif quest in ["2", "inimigo"]:
            for oponente in oponentes :
                if oponente["vida"] <= 0:
                    oponente["vida"] += 5
                    salvar(caminho="oponentes.json", dados=oponentes)
                    return "a vida do oponente foi restaurada"
        else: 
            return "\nERRO!!\n"

def treinamento():
    avatares = carregar_dados(caminho="avatares.json")
    localizado = False
    while True:
        quem = str(input("digite o nome do avatar que deseja treinar: "))
        for avatar in avatares:
            localizado = True
            if avatar["experiencia"] > 100:
                level_up()
            if avatar["nome"].lower() == quem.lower():
                avatar["experiencia"] += 10
                salvar("avatares.json", dados=avatares)
                return "Fim do treinamento"

def level_up():    
    avatares = carregar_dados(caminho="avatares.json")
    localizado = False
    for avatar in avatares:
        if avatar["experiencia"] > 100:
            localizado = True
            avatar["nivel"] += 1
            salvar(caminho="avatares.json", dados=avatares)
            return f"O Avatar {avatar['nome']} subiu de nivel"
#----------------------------------EM DESENVOLVIMENTO---------------------------------------------------


def editar_avatar():
    # Terminar de editar avatar:

    return ""








