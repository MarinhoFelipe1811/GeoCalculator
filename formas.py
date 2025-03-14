from abc import ABC, abstractmethod
import math

def obter_numero_float(mensagem): #função para verificar se o que foi digitado nos parâmetros(lado,raio,etc..) é um float type.
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")

class FormaGeometrica2d (ABC):
    @abstractmethod
    def calcular_perimetro(self):
        pass
    @abstractmethod
    def calcular_area(self):
        pass
    @abstractmethod
    def coleta_dados_resultados_e_exibe(self):
        pass
    def exibir_resultados(self, calculo_da_area, calculo_do_perimetro): #função para mostrar prints com os resultados dos calculos 2d
        return (f'O cálculo da área é: {calculo_da_area:.2f}.\nO cálculo do perímetro é: {calculo_do_perimetro:.2f}.')
class FormaGeometrica3d(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    @abstractmethod
    def calcular_volume(self):
        pass
    @abstractmethod
    def coleta_dados_resultados_e_exibe(self):
        pass
    def exibir_resultados(self, calculo_da_area, calculo_do_volume ): #função para mostrar prints com os resultados dos calculos 3d
        return (f'O cálculo da área é: {calculo_da_area:.2f}.\nO cálculo do volume é: {calculo_do_volume :.2f}.')
    
class Circulo(FormaGeometrica2d):
    def __init__(self, raio):
        self.raio = raio
        super().__init__()
    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.raio
        return perimetro
    def calcular_area(self):
        area = math.pi * self.raio**2
        return area
    @staticmethod
    def obter_parametros():
        raio = obter_numero_float("Digite o raio do círculo: ")
        return (raio,)
    def coleta_dados_resultados_e_exibe(self):#função para coletar os dados dos resultados dos calculos e retorna chamando uma função para exibir eles
        calculo_da_area = self.calcular_area()
        calculo_do_perimetro = self.calcular_perimetro()
        return self.exibir_resultados(calculo_da_area, calculo_do_perimetro)
    
class Quadrado(FormaGeometrica2d):
    def __init__(self, lado):
        self.lado = lado
        super().__init__()
    def calcular_perimetro(self):
        perimetro = self.lado *4
        return perimetro
    def calcular_area(self):
        area = self.lado**2
        return area
    @staticmethod
    def obter_parametros():
        lado = obter_numero_float("Digite o lado do quadrado: ")
        return (lado,)
    def coleta_dados_resultados_e_exibe(self):#função para coletar os dados dos resultados dos calculos e retorna chamando uma função para exibir eles
        calculo_da_area = self.calcular_area()
        calculo_do_perimetro = self.calcular_perimetro()
        return self.exibir_resultados(calculo_da_area, calculo_do_perimetro)
    
class Cubo(FormaGeometrica3d):
    def __init__(self, lado):
        self.lado = lado
        super().__init__()
    def calcular_area(self):
        area = 6*self.lado**2
        return area 
    def calcular_volume(self):
        volume = self.lado**3
        return volume
    @staticmethod
    def obter_parametros():
        lado = obter_numero_float("Digite o lado do cubo: ")
        return (lado,)
    def coleta_dados_resultados_e_exibe(self): #função para coletar os dados dos resultados dos calculos e retorna chamando uma função para exibir eles
        calculo_da_area = self.calcular_area()
        calculo_do_volume = self.calcular_volume()
        return self.exibir_resultados(calculo_da_area, calculo_do_volume)
        
class Cilindro(FormaGeometrica3d):
    def __init__(self, raio, altura):
        self.raio =  raio
        self.altura= altura
        super().__init__()
    def calcular_area(self):
        area = 2 * math.pi * self.raio * (self.raio + self.altura)
        return area
    def calcular_volume(self):
        volume = math.pi * (self.raio**2) * self.altura
        return volume
    @staticmethod
    def obter_parametros():
        raio = obter_numero_float("Digite o raio do cilindro: ")
        altura = obter_numero_float("Digite a altura do cilindro: ")
        return (raio, altura)
    def coleta_dados_resultados_e_exibe(self):#função para coletar os dados dos resultados dos calculos e retorna chamando uma função para exibir eles
        calculo_da_area = self.calcular_area()
        calculo_do_volume = self.calcular_volume()
        return self.exibir_resultados(calculo_da_area, calculo_do_volume)