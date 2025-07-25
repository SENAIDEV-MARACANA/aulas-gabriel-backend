from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def __init__(self, placa, modelo, dono, quantidade_rodas: int, quantidade_volante: int):
        self.__placa = placa
        self.__modelo = modelo
        self.__quantidade_rodas = quantidade_rodas
        self.__dono = dono
        self.__quantidade_volante = quantidade_volante

    #Funções de retorno das informações privadas
    def get_placa(self):
        return self.__placa

    def get_modelo(self):
        return self.__modelo

    def get_dono(self):
        return self.__dono

    def get_quantidade_rodas(self):
        return self.__quantidade_rodas

    def get_quantidade_volante(self):
        return self.__quantidade_volante

    # Função de alteração de quntdd
    def set_placa(self, nova_placa):
        self.__placa = nova_placa

    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    def set_dono(self, novo_dono):
        self.__dono = novo_dono

    def set_quantidade_rodas(self, nova_qtd):
        self.__quantidade_rodas = nova_qtd

    def set_quantidade_volante(self, nova_qtd):
        self.__quantidade_volante = nova_qtd

    @abstractmethod
    def buzina(self):
        pass

    @abstractmethod
    def status(self):
        pass

class Carro(Veiculo):
    def __init__(self, placa, modelo, dono, quantidade_rodas=4, quantidade_volante=1):
        super().__init__(placa, modelo, dono, quantidade_rodas, quantidade_volante)

    def buzina(self):
        print(f"{self.get_modelo()}: Biiiiiiii bi bi!")

    def status(self):
        print(f"Placa do carro: {self.get_placa()}")
        print(f"Modelo: {self.get_modelo()}")
        print(f"Dono: {self.get_dono()}")
        print(f"Rodas: {self.get_quantidade_rodas()}")
        print(f"Volantes: {self.get_quantidade_volante()}")
        print("-" * 30)

# Objetos
carro_1 = Carro("x125", "Celta", "Alex")
carro_2 = Carro("m234", "Jeep", "Ana")

# Antes da alteração
carro_1.status()
carro_2.status()

#Durante
print ("Alterando carro_2")
carro_2.set_dono("Carla")
carro_2.set_modelo("BMW")
carro_2.set_placa("vc567")

# Depois da alteração
carro_2.status()
carro_2.buzina()
carro_1.buzina()

