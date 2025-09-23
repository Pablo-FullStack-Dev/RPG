# class Bolsa:
#     def __init__(self):
#         pass

class Forja:
    def __init__(self, tipo):
        self.tipo = tipo

class Avatar(Forja):
    def __init__(self, nome, vida, mana, classe, raca):
        super().__init__("Avatar")
        #Caracteristicas básicas: 
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.classe= classe
        self.raca = raca
        # self.nivel= nivel
        #////////////////////////////////////////////////////////////////
        # self.cor = str(input('\ndescreva a coloração do personagem: '))
        # self.experiencia = str(input('\ndigite a experiencia do personagem: '))
        
    def info(self):
        avatar = {
            "nome": self.nome,
            "vida": self.vida,
            "mana": self.mana,
            "classe": self.classe,
            "raca": self.raca
            # "nivel": self.nivel
        }
        return avatar
    def adicionar_armadura(): 
        elmo = str(input('digite o nome do elmo: '))
        resi_elmo = int(input('digite a resistencia do elmo: '))
        peitoral = str(input('digite o nome do peitoral'))
        resi_peitoral = int(input('digite a resistencia do peitoral: '))
        calca = str(input('digite o nome da calça: '))
        resi_calca = int(input('digite a resistencia da calça: '))
        bota = str(input('digite o nome da bota: '))
        resi_bota = int(input('digite a resistencia da bota: '))
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
        
        
        return "\nEquipamento adicionado"
    def inserir_atributos(): 
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
        
        return "\nAtributos e adicionado"

class Npc(Forja):
    def __init__(self):
        super().__init__("npc")
        self.nome = str(input('escreva o nome: '))
        self.vida = int(input('escreva a vida: '))
        self.estamina = int(input('escreva a estamina: '))
        self.resistencia = int(input('escreva resistencia: '))
        self.ataque = int(input('escreva o dano: '))
        self.escudo = int(input('escreva a defesa: '))
        self.alma = str(input('escreva o tipo de alma: '))
    def info(self):
        npc = {
        "nome": self.nome,
        "vida": self.vida,
        "estamina": self.estamina,
        "resistencia": self.resistencia,
        "ataque": self.ataque,
        "escudo": self.escudo,
        "alma": self.alma
        }
        return npc


class Item(Forja):
    def __init__(self,nome, dano, tipo):
        super().__init__("item")
        self.nome = nome
        self.dano = dano
        self.tipo = tipo
    def info(self):
        item = {
        "nome": self.nome,
        "dano": self.dano,
        "tipo": self.tipo
        }
        return item



class Dado:
    def __init__(self, tipo):
        self.tipo = tipo
     
    def rolar(self):
        import random
        chave = {
            "1": "d4", "d4": "d4",
            "2": "d6", "d6": "d6",
            "3": "d8", "d8": "d8",
            "4": "d10", "d10": "d10",
            "5": "d12", "d12": "d12",
            "6": "d20", "d20": "d20",
            "7": "d100", "d100": "d100"
        }.get(self.tipo)
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
        # if self.tipo in ["0", "sair", "encerrar"]:
        #     break

        

        if chave and dados_possiveis[chave]:
            numero = random.choice(dados_possiveis[chave])
            dados_possiveis[chave].remove(numero)
            return f"{chave.upper()} = {numero}"
            # print(f"\nResultado do {chave.upper()}: {numero}")
        elif chave:
            # print(f"\n Todos os valores do {chave.upper()} já foram sorteados! Reiniciando lista...")
            dados_possiveis[chave] = list(range(1, int(chave[1:]) + 1))
            return f" Todos os valores do {chave.upper()} já foram sorteados! Reiniciando lista..."
        else:
            return "Erro de digitação! Tente novamente."

        return "\nFIM DOS DADOS"


class Inventário(Forja):
    def __init__(self):
        super().__init__("item")
        

