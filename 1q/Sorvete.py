class Sorvete:
    def __init__(self):
        self.quantidade_de_bolas = None
        self.preco_recepiente = None
        self.preco_por_bola = None
        self.preco_cobertura = None

    def define_valores(self):
        pass

    def calcula_preco(self):
        pass


class SorveteBasico(Sorvete):
    def __init__(self, qtd_bolas=1):
        super().__init__()
        self.recepiente = "Taça"
        self.cobertura = None
        self.quantidade_de_bolas = qtd_bolas

        self.preco_recepiente = 0.0
        self.preco_por_bola = 1.5
        self.preco_cobertura = 0.0

    def calcula_preco(self):
        return self.quantidade_de_bolas * self.preco_por_bola


class SorveteDecorator(Sorvete):
    _sorvete: Sorvete = None

    def __init__(self, sorvete: Sorvete):
        super().__init__()
        self._sorvete = sorvete

    @property
    def sorvete(self) -> Sorvete:
        return self._sorvete


class CopoDecorator(SorveteDecorator):
    def define_valores(self):
        self.sorvete.recepiente = "Copo"
        self.sorvete.preco_recepiente = 0.2

    def calcula_preco(self):
        self.define_valores()
        return (self.sorvete.quantidade_de_bolas * self.sorvete.preco_por_bola) + self.sorvete.preco_recepiente


class CasquinhaDecorator(SorveteDecorator):
    def define_valores(self):
        self.sorvete.recepiente = "Casquinha"
        self.sorvete.preco_recepiente = 1.5

    def calcula_preco(self):
        self.define_valores()
        return (self.sorvete.quantidade_de_bolas * self.sorvete.preco_por_bola) + self.sorvete.preco_recepiente


class ChocolateDietDecorator(SorveteDecorator):
    def define_valores(self):
        self.sorvete.preco_por_bola = 2.0

    def calcula_preco(self):
        self.define_valores()
        return (self.sorvete.quantidade_de_bolas * self.sorvete.preco_por_bola) + self.sorvete.preco_recepiente


class CoberturaDecorator(SorveteDecorator):
    def define_valores(self):
        self.sorvete.preco_cobertura = 0.5

    def calcula_preco(self):
        self.define_valores()
        return (
                (self.sorvete.quantidade_de_bolas * self.sorvete.preco_por_bola) +
                self.sorvete.preco_recepiente + self.sorvete.preco_cobertura
        )


def menu() -> None:
    print("\n\nBem vindo à sorveteria Nobre!")
    print("""
        Sabores: 
                1 - Chocolate         R$1.50/bola
                2 - Morango           R$1.50/bola
                3 - Flocos            R$1.50/bola
                4 - Pavê              R$1.50/bola
                5 - Napolitano        R$1.50/bola
                6 - Chocolate Diet    R$2.00/bola
        Recepientes: 
                1 - Taça              R$0.00
                2 - Copo              R$0.20
                3 - Casquinha         R$1.50
        Cobertura:
                1 - Sem Cobertura     R$0.00
                2 - Chocolate         R$0.50
                3 - Morango           R$0.50
                4 - Caramelo          R$0.50
    """)
    print("Por favor monte seu sorvete escolhendo os números do menu")


def main() -> None:
    menu()

    sabores = ["Chocolate", "Morango", "Flocos", "Pavê", "Napolitano", "Chocolate Diet"]
    sabor = int(input("Sabor: "))
    qtd_bolas = int(input("Quantas bolas de sorvete você deseja? "))
    sorvete_basico = SorveteBasico(qtd_bolas)
    preco_atual = sorvete_basico.calcula_preco()

    if sabor == 6:
        sorvete_diet = ChocolateDietDecorator(sorvete_basico)
        preco_atual = sorvete_diet.calcula_preco()

    recepientes = ["Taça", "Copo", "Casquinha"]
    recepiente = int(input("Recepiente: "))
    if recepiente == 2:
        sorvete_copo = CopoDecorator(sorvete_basico)
        preco_atual = sorvete_copo.calcula_preco()

    elif recepiente == 3:
        sorvete_casquinha = CasquinhaDecorator(sorvete_basico)
        preco_atual = sorvete_casquinha.calcula_preco()

    coberturas = ["Sem Cobertura", "Chocolate", "Morango", "Caramelo"]
    cobertura = int(input("Cobertura: "))
    if cobertura != 1:
        sorvete_cobertura = CoberturaDecorator(sorvete_basico)
        preco_atual = sorvete_cobertura.calcula_preco()

    sabor = sabores[sabor - 1]
    recepiente = recepientes[recepiente - 1]
    cobertura = coberturas[cobertura - 1]

    print(f"Sorvete sabor {sabor}, em {recepiente}", end=" ")
    if cobertura != "Sem Cobertura":
        print(f"e cobertura de {cobertura}", end=" ")
    print(f"saindo no valor de R${preco_atual}")


if __name__ == "__main__":
    main()
    sorvete = Sorvete()
    sorvete_basico = SorveteBasico()
    sorvete_copo = CopoDecorator(sorvete_basico)
    sorvete_casquinha = CasquinhaDecorator(sorvete_basico)
    sorvete_cobertura = CoberturaDecorator(sorvete_basico)
