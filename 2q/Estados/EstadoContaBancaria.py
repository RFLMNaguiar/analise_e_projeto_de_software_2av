from abc import ABC, abstractmethod


class EstadoContaBancaria(ABC):

    @abstractmethod
    def realizar_saque(self) -> None:
        pass

    @abstractmethod
    def realizar_deposito(self) -> None:
        pass

    @abstractmethod
    def encerrar_conta(self) -> None:
        pass
