from abc import ABC, abstractmethod


class EstadoContaBancaria(ABC):
    def __init__(self):
        self.nome = 'implements'

    @abstractmethod
    def realizar_saque(self):
        pass

    @abstractmethod
    def realizar_deposito(self):
        pass

    @abstractmethod
    def encerrar_conta(self):
        pass
