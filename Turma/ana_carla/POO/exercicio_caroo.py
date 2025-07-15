class Carro:
    def __init__(self, placa, modelo, dono, quantidade_rodas = 4, quantidade_volante = 1):
        self.placa = placa
        self.modelo = modelo
        self.quantidade_rodas = quantidade_rodas
        self.dono = dono
        self.quantidade_volante = quantidade_volante

    def buzina(self):
        print("Biiiiiiii bi bi!")

    def status(self):
        print(f"Placa do carro: {self.placa}\n")
        print(f"Modelo: {self.modelo}")
        print(f"Dono: {self.dono}\n")

carro_1 = Carro("x125", "celta", "Alex")
carro_2 = Carro("m234", "jeep", "Ana")

#antes da alteração
carro_1.status()
carro_2.status()

#alterando
carro_2.dono = "Carla"
carro_2.modelo = "BMW"
carro_2.placa = "vc567"

carro_2.status()
carro_2.buzina()
