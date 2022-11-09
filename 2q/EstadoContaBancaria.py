from abc import ABC, abstractmethod


class EstadoContaBancaria(ABC):
    @abstractmethod
    def realizar_saque(self, dinheiro_disponivel: float, quantidade: float) -> float:
        pass

    @abstractmethod
    def realizar_deposito(self, quantidade: float) -> float:
        pass

    @abstractmethod
    def encerrar_conta(self) -> None:
        pass
