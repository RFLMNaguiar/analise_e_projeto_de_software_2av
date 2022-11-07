import Agencia as Ag
import Correntista as Co
import Estados
import datetime


class ContaBancaria:
    def __init__(self, numero_da_conta, saldo, limite, nome_da_agencia, numero_da_agencia, nome_do_correntista, cpf,
                 data_abertura, data_encerramento):
        self.__estado = Estados.Disponivel()
        self.agencia = Ag.Agencia(nome_da_agencia, numero_da_agencia)
        self.correntista = Co.Correntista(nome_do_correntista, cpf)
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = datetime.datetime.now()
        self.data_encerramento = None

    def realizar_saque(self):
        self.__estado.realizar_saque()

    def realizar_deposito(self):
        self.__estado.realizar_deposito()

    def encerrar_conta(self):
        self.__estado.encerrar_conta()
