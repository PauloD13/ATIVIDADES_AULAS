#Importando bibliotecas e definindo variáveis globais
import random
import os
foccus = False

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

#funções de menu e execução do jogo
def menu_classe():
    limpar()
    print("Escolha sua classe:")
    print("1. Ladino")
    print("2. Guerreiro")
    escolha = input("Digite o número da classe desejada: ")
    return escolha

def menu_inimigo():
    limpar()
    print("Escolha seu inimigo:")
    print("1. Goblin")
    print("2. Orc")
    escolha = input("Digite o número do inimigo desejado: ")
    return escolha

def menu_acao():
    limpar()
    print("Escolha uma ação:")
    print("1. Atacar")
    print("2. Esquivar")
    print("3. Usar Ataque forte")
    print("4. Usar habilidade especial")
    print("5. Sair do jogo")
    escolha = input("Digite o número da ação desejada: ")
    return escolha

#defeninição das classes 
#classe base Personagem e classes derivadas Ladino e Guerreiro
#classe pai
class Personagem:
    #função construtora
    def __init__(self, nome, vida=100, poder=3, defesa=3, agilidade=3, classe="Personagem"):
        self.__nome = nome
        self.__vida = vida
        self.__poder = poder
        self.__defesa = defesa
        self.__agilidade = agilidade
        self.__classe = classe

    #definindo os valores e prorpriedades
    #registrando atributos privados com getters e setters
    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def classe(self):
        return self.__classe
        
    @classe.setter
    def classe(self, classe):
        self.__nome = classe

    @property
    def vida(self):
        return self.__vida
        
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    @property
    def poder(self):
        return self.__poder
    
    @poder.setter
    def poder(self, poder):
        self.__poder = poder
    
    @property
    def defesa(self):
        return self.__defesa
    
    @defesa.setter
    def defesa(self, defesa):
        self.__defesa = defesa

    @property
    def agilidade(self):
        return self.__agilidade
        
    @agilidade.setter
    def agilidade(self, agilidade):
        self.__agilidade = agilidade

    #definindo métodos de ataque e defesa
    #funções
    def tackle(self, personagem):
        dano = self.poder * 10
        personagem.vida -= (dano / (personagem.defesa * 15/20))
        print(f"{self.nome} atacou {personagem.nome}!")
        print(f"Vida de {personagem.nome}: {personagem.vida:.2f}")

    def dodge(self):
        chance = random.randint(1, 100)
        if chance <= self.__agilidade * 5:
            print(f"{self.nome} esquivou do ataque!")
            return True
        else:
            print(f"{self.nome} não conseguiu esquivar do ataque.")
            return False

#classe filha Ladino
class Ladino(Personagem):
    def __init__(self, nome, vida=90, poder=2, defesa=1, agilidade=10, classe="Ladino"):
        super().__init__(nome, poder, defesa)
        self.__nome = nome
        self.__vida = vida
        self.__poder = poder
        self.__defesa = defesa
        self.__agilidade = agilidade
        self.__classe = classe

    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def classe(self):
        return self.__classe
        
    @classe.setter
    def classe(self, classe):
        self.__nome = classe

    @property
    def vida(self):
        return self.__vida
        
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    @property
    def poder(self):
        return self.__poder
    
    @poder.setter
    def poder(self, poder):
        self.__poder = poder
    
    @property
    def defesa(self):
        return self.__defesa
    
    @defesa.setter
    def defesa(self, defesa):
        self.__defesa = defesa

    @property
    def agilidade(self):
        return self.__agilidade
        
    @agilidade.setter
    def agilidade(self, agilidade):
        self.__agilidade = agilidade
    
    #definindo funções das habilidades exclusivas do ladino
    #apunhalada e poção de cura
    def apunhalada(self, personagem):
        dano = self.__poder * 100
        chance = random.randint(1, 100)
        if chance > self.__agilidade * 5:
            print(f"{self.nome} errou a apunhalada!")
            return
        else:
            personagem.vida -= dano
            print(f"{self.nome} atacou {personagem.nome} com uma apunhalada!")
            print(f"Vida de {personagem.nome}: {personagem.vida:.2f}")

    def heal_potion(self, personagem):
        chance = random.randint(1, 100)
        if chance > 85:
            cura = 50
            self.__vida += cura
            print(f"{self.nome} usou uma poção de cura! Vida aumentada para {self.__vida}.")
        else:
            cura = personagem.vida/2
            personagem.vida += cura
            print(f"{self.nome} errou a cura e acabou curando o oponente\n{personagem.nome} : {personagem.vida}.")

#classe filha Guerreiro
class Guerreiro(Personagem):
    def __init__(self, nome, vida=100, poder=6, defesa=5, agilidade=1, classe="Guerreiro"):
        super().__init__(nome, poder, defesa, vida)
        self.__defesa = defesa
        self.__nome = nome
        self.__vida = vida
        self.__poder = poder
        self.__defesa = defesa
        self.__agilidade = agilidade
        self.__classe = classe

    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def classe(self):
        return self.__classe
        
    @classe.setter
    def classe(self, classe):
        self.__nome = classe

    @property
    def vida(self):
        return self.__vida
        
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    @property
    def poder(self):
        return self.__poder
    
    @poder.setter
    def poder(self, poder):
        self.__poder = poder
    
    @property
    def defesa(self):
        return self.__defesa
    
    @defesa.setter
    def defesa(self, defesa):
        self.__defesa = defesa

    @property
    def agilidade(self):
        return self.__agilidade
        
    @agilidade.setter
    def agilidade(self, agilidade):
        self.__agilidade = agilidade

    #definindo funções das habilidades exclusivas do guerreiro
    #escudo, ataque pesado e foco
    def escudo(self):
        self.__defesa += 2
        print(f"{self.nome} levantou o escudo! Defesa aumentada para {self.__defesa}.")
    
    def heavy_attack(self, personagem):
        dano = self.__poder * 50
        chance = random.randint(1, 100)
        if chance > 65:
            print(f"{self.nome} errou o ataque pesado!")
            return
        else:
            personagem.vida -= (dano / (personagem.defesa * 10/20))
            print(f"{self.nome} atacou {personagem.nome} com um ataque pesado!")
            print(f"Vida de {personagem.nome}: {personagem.vida:.2f}")

    def foccus(self):
        chance = random.randint(1, 100)
        if chance < 80:
            self.__poder += 2
            print(f"{self.nome} se concentrou! Poder aumentado para {self.__poder}.")
            global foccus
            foccus = True
        else:
            self.__poder -= 1
            print(f"{self.nome} falhou em se concentrar! Poder diminuído para {self.__poder}.")

#random foi usado para definir as chances de acerto e falha dos ataques e habilidades especiais
#definindo personagens e inimigos base
astolfo = Ladino("Astolfo")

Siedfried = Guerreiro('Siedfried', vida=100)

goblin = Personagem("Goblin", vida=50, poder=2, defesa=1, agilidade=2, classe="Mosntro")

orc = Personagem("Orc", vida=800, poder=4, defesa=4, agilidade=1, classe="Mosntro")

#loop principal do jogo
print("Bem-vindo ao jogo de RPG!")
#escolher classe do jogador
match menu_classe():
    case '1':
        jogador = astolfo
    case '2':
        jogador = Siedfried
    case _:
        print("Classe inválida. Saindo do jogo.")
        exit()
print(f"Você escolheu a classe {jogador.classe}!")
print(f"Vida: {jogador.vida}\nPoder: {jogador.poder}\nDefesa: {jogador.defesa}\nAgilidade: {jogador.agilidade}")
input("Pressione Enter para começar o jogo...")

#escolher inimigo
match menu_inimigo():
    case '1':
        oponente = goblin
    case '2':
        oponente = orc
    case _:
        print("Classe inválida. Saindo do jogo.")
        exit()
print(f"Você escolheu o {oponente.nome}\nClasse: {oponente.classe}!")
print(f"Vida: {oponente.vida}\nPoder: {oponente.poder}\nDefesa: {oponente.defesa}\nAgilidade: {oponente.agilidade}")
input("Pressione Enter para começar o jogo...")

#loop principal do jogo
#acoes de batalha
while True:
    acao = menu_acao()
    #testando casos
    match acao:
        case '1':
            jogador.tackle(oponente)
        case '2':
            jogador.dodge()
        case '3':
            if isinstance(jogador, Ladino):
                jogador.apunhalada(oponente)
            elif isinstance(jogador, Guerreiro):
                jogador.heavy_attack(oponente)
        case '4':
            if isinstance(jogador, Ladino):
                jogador.heal_potion(jogador)
            elif isinstance(jogador, Guerreiro):
                if not foccus:
                    jogador.foccus()
                elif foccus:
                    print(f"{jogador.nome} já está focado!")
        case '5':
            print("Saindo do jogo. Até a próxima!")
            break
        case _:
            print("Ação inválida. Tente novamente.")
    
    if oponente.vida <= 0:
        print(f"{oponente.nome} foi derrotado! Você venceu!")
        break
    
    # Turno do goblin
    print(f"Turno do {oponente.nome}!")
    if not jogador.dodge():
        oponente.tackle(jogador)
    
    if jogador.vida <= 0:
        print(f"{jogador.nome} foi derrotado! Fim de jogo.")
        break

    input("Pressione Enter para continuar...")

