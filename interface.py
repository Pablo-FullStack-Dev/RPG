from definicoes import (dados, adicionar_avatar, adicionar_armadura, inserir_atributos, adicionar_npc, criar_item, treinamento, vizualizar)
# Ainda vou ver o que vou fazer com isso ainda
while True:
    quest = str.lower(input('''\n
vc gostaria de usar:
                            1. Dados
                            2. Item
                            3. Personagem ou NPC 
                            4. Visualizar
                            0. Encerrar programa
                            
--> '''))
    if quest in ["0", "encerrar"]:
        break
    elif quest in ["1", "dados"]: # 1. Dados
        print(dados())
    elif quest in ["2", "item"]:
        while True:
            question = str.lower(input('''\n
Vc gostaria de:
                          1. Criar Item
                          0. Voltar
-->  '''))
            if question in ["0", "encerrar", "voltar"]:
                break
            elif question in ["1", "criar item", "item"]:
                criar_item()
            else:
                print("\nErro de digitação!\n")

    elif quest in ["3", "Personagem","npc"]:
        while True:
            ques = str.lower(input('''\n
Vc gostaria de:
                          1. Criar NPC
                          2. Criar Avatar
                          3. Criar atributos
                          4. Criar armadura
                          0. Voltar
-->  '''))
            if ques in ["0", "voltar"]:
                break
            elif ques in ["1","criar npc"]: #testar escrever "CRIAR NPC"
                adicionar_npc()
            elif quest in ["2", "criar avatar"]:
                print(adicionar_avatar()) 
            elif ques in ["3", "criar atributos"]:
                print(inserir_atributos())
            elif ques in ["4", "criar armadura"]:
                print(adicionar_armadura())
            elif ques in ["criar"]:
                print("\nTá achando que tenho bola de cristal agora?\n")
            else:
                print("\nERRO!\n")

        
    elif quest in ["4", "visualizar"]:
        vizualizar()
    
    else:
        print("\nErro de digitação\n")
                  


            
