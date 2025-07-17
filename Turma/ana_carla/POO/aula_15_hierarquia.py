### **Exercício: Modelagem de Veículos**

#Crie um sistema de classes que represente veículos com diferentes níveis de hierarquia:

#### **Código Base para Implementação:**

class Veiculo:
    tipo = "genérico"
    velocidade_maxima = 0
    
    def __init__(self, nome):
        self.nome = nome
    
    def mover(self):
        print(f"{self.nome} está se movendo a {self.velocidade_maxima} km/h")


class Carro(Veiculo):
    # Implemente aqui conforme o enunciado
    tipo = "carro"
    velocidade_maxima = 120

    def buzinar(self):
       print(f"Carro {self.nome} está buzinando: Bii Bii")

class CarroEletrico(Carro):
    # Implemente aqui conforme o enunciado
    autonomia = 300

    def __init__(self, nome, marca):
       super().__init__(nome)
       self.marca = marca

    def mostrar_autonomia(self):
       print(f"O carro elétrico {self.marca} {self.nome} tem autonomia de {self.autonomia} km")

# Teste seu código
veiculo1 = Veiculo("Transportador")
carro1 = Carro("Fusca")
eletrico1 = CarroEletrico("Model S", "Tesla")

veiculo1.mover()
carro1.mover()
carro1.buzinar()
eletrico1.mostrar_autonomia()

