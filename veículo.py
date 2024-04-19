class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def frear(self):
        print(f"{self.modelo} freou")

    def acelerar(self):
        print(f"{self.modelo} acelerou")

class Carro(Veiculo):
    def __init__(self, cor):
        super()._init_cor(cor)

    def abrir_porta(self):
        print(f"{self.modelo} abriu a porta!")

class Moto(Veiculo):
    def __init__(self, cilindrada):
        super()._init_cilindrada(cilindrada)

    def empinar(self):
        print(f"{self.modelo} empinou")

if __name__ == '__main__':

    carro1 = Veiculo('Fiat', 'Fusca')
    print(carro1)
    moto1 = Veiculo('Fiat', 'CB500')
    print(moto1)



    