import datetime
import random
import sys
import Agencia as Ag
import Correntista as Co
import Devedor
import Disponivel


class ContaBancaria:
    def __init__(self, nome_do_correntista: str, cpf: str,) -> None:

        self.__estado = Disponivel.Disponivel()
        self.agencia = Ag.Agencia(f"Agência P{random.randint(100, 999)}", random.randint(100, 999))
        self.correntista = Co.Correntista(nome_do_correntista, cpf)
        self.numero_da_conta = random.randint(10000, 99999)
        self.saldo = 0
        self.limite = 50
        self.data_abertura = datetime.datetime.now()
        self.data_encerramento = None
        self.dinheiro_disponivel = self.saldo + self.limite

    def realizar_saque(self, quantidade) -> None:
        quantidade_sacada = self.__estado.realizar_saque(self.dinheiro_disponivel, quantidade)
        self.saldo -= quantidade_sacada
        self.__verificar_estado()

    def realizar_deposito(self, quantidade) -> None:
        quantidade_depositada = self.__estado.realizar_deposito(quantidade)
        self.saldo += quantidade_depositada
        self.__verificar_estado()

    def encerrar_conta(self) -> None:
        self.data_encerramento = self.__estado.encerrar_conta()
        if self.data_encerramento is not None:
            sys.exit()

    def __verificar_estado(self) -> None:
        if self.limite + self.saldo < 0:
            self.__estado = Devedor.Devedor()
        elif self.saldo + self.limite >= 0:
            self.__estado = Disponivel.Disponivel

        self.dinheiro_disponivel = self.saldo + self.limite
