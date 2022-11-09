from datetime import datetime
from EstadoContaBancaria import EstadoContaBancaria


class Disponivel(EstadoContaBancaria):
    def realizar_saque(self, dinheiro_disponivel: float, quantidade: float) -> float:
        return quantidade

    def realizar_deposito(self, quantidade: float) -> float:
        return quantidade

    def encerrar_conta(self) -> datetime:
        data_encerramento = datetime.now()
        print(f"Conta encerrada no momento: "
              f"{data_encerramento}.")
        return data_encerramento
