import Agencia as Ag
import Correntista as Co
import Estados
import datetime


class ContaBancaria:
    def __init__(self, numero_da_conta: int, saldo: float, limite: float, nome_da_agencia: str, numero_da_agencia: int,
                 nome_do_correntista: str, cpf: str, data_abertura: datetime.datetime,
                 data_encerramento: datetime.datetime) -> None:

        self.__estado = Estados.Disponivel()
        self.agencia = Ag.Agencia(nome_da_agencia, numero_da_agencia)
        self.correntista = Co.Correntista(nome_do_correntista, cpf)
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = datetime.datetime.now()
        self.data_encerramento = None

    def realizar_saque(self) -> None:
        self.__estado.realizar_saque()

    def realizar_deposito(self) -> None:
        self.__estado.realizar_deposito()

    def encerrar_conta(self) -> None:
        self.__estado.encerrar_conta()
