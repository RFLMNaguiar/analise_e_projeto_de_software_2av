import datetime

import Devedor
import EstadoContaBancaria


class Disponivel(EstadoContaBancaria):
    def realizar_saque(self, quantidade: float) -> None:
        self.ContaBancaria.saldo -= quantidade
        if self.ContaBancaria.limite + self.ContaBancaria.saldo >= quantidade > self.ContaBancaria.saldo:
            self.ContaBancaria.__estado = Devedor.Devedor()

    def realizar_deposito(self, quantidade: float) -> None:
        self.ContaBancaria.saldo += quantidade

    def encerrar_conta(self) -> None:
        self.ContaBancaria.data_encerramento = datetime.datetime.now()
        print(f"Conta encerrada no momento: {self.ContaBancaria.data_encerramento}.")
