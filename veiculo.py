class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Portas: {self.portas}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tipo: {self.tipo}")
        
# Exemplo de uso
carro1 = Carro("Toyota", "Corolla", 2020, 4)
moto1 = Moto("Honda", "CB500", 2019, "Esportiva")
carro1.exibir_informacoes()
print("\n")
moto1.exibir_informacoes()
