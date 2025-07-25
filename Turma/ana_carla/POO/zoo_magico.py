class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("Este animal não fala...")

    def apresentar(self):
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos!")

    
class Leao(Animal):

    def __init__(self, nome:str, idade:int, caçando:bool):
        super().__init__(nome, idade)
        self.caçando = caçando

    def falar(self):
        print(f"O leão {self.nome} ruge: ROARRR!\n")

    def caçar(self, caçando):
        if caçando == True:
            print(f"O leão {self.nome} está caçando!")
        else:
            print(f"O leão {self.nome} não esta caçando!")
    
    def apresentar(self):
        super().apresentar()
        self.caçar(self.caçando)
        

class Papagaio(Animal):
   
    def __init__(self, nome:str, idade:int, altura:int):
        super().__init__(nome, idade)
        self.altura = altura

    def falar(self):
        print(f"O papagaio {self.nome} diz: Quer um biscoito?\n")

    def voar(self):
        print(f"O papagaio voou a {self.altura} metros de altura!")
    
    def apresentar(self):
        super().apresentar()
        self.voar()


class Cobra(Animal):

    def __init__(self, nome:str, idade:int, venenosa:bool):
        super().__init__(nome, idade)
        self.venenosa = venenosa

    def falar(self):
        print(f"A cobra {self.nome} sibila: Sssssss...\n")

    def enrolar(self):
        print(f"A cobra {self.nome} se enrolou numa árvore!")

    def apresentar(self):
        super().apresentar()
        self.enrolar()
        if self.venenosa:
            print(f"Cuidado! Não me toque pois eu tenho veneno... Sssss!")
        else:
            print(f"Não tenho veneno, mas não ouse me tocar ou irei morder!")

class Tartaruga(Animal):
    def __init__(self, nome: str, idade: int, dentro_do_casco: bool):
        super().__init__(nome, idade)
        self.dentro_do_casco = dentro_do_casco

    def falar(self):
        print(f"A tartaruga {self.nome} diz: vou devagarinho mas chego lá...\n")

    def esconder(self):
        if self.dentro_do_casco:
            print(f"A tartaruga {self.nome} está escondida")
        else:
            print(f"A tartaruga {self.nome} está fora do casco, explorando!")

    def apresentar(self):
        super().apresentar()
        self.esconder()


#### **Parte 2: Crie uma Lista de Animais**  

zoo = [
    Leao("Lian", 10, True),
    Papagaio("Raparigo", 1, 3),
    Cobra("Jararaca", 8, False),
    Tartaruga("Rapidinha", 25, False)
]

for i in zoo:
    i.apresentar()
    i.falar()
    
           