#Definição da classe base veículo e sus classes veículos terrestes
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo

    def get_marca(self):
        return self.__marca

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre