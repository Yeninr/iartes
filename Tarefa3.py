# Tarefa 3
# 1. Definição da classe base veículo e sus classes veículos terrestes
# 2. Use a classe escolhida para definir uma hierarquia.
# 3. Escreva um código que faça uso da classe definidas

#Clase Base
class Veiculo:
    #Atributos
    def __init__(self, marca, modelo, motor):
        self._marca = marca
        self._modelo = modelo
        self._motor = motor

    #Metodos
    def acelerar(self):
        print("Fora de o meu caminho")

    def freiar(self):
        print("Eu vou parar, pode ir!")    

#Clase Hija: Herencia
class Maritimo(Veiculo):
    #Atributos 
    def __init__(self, timon, ancla, porte):
        self.__timon = timon
        self.__ancla = ancla
        self.__porte = porte

class terrestre(Veiculo):
    def __init__(self, nroPneus):
        self._nroPneus = nroPneus
    
    def freiar(self):
        super().freiar()
        print("Travando pneus")   

    #Metodos
    def get_navegar(self):
            print("Vou navegando ...")  

#Evidenciando a herença
print(Maritimo.__bases__)


barco = Maritimo("SEATBOAT","Cruzero","5")
print(barco.marca)
#barco.get_navega()