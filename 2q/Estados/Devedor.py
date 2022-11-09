import Disponivel
import EstadoContaBancaria


class Devedor(EstadoContaBancaria):
    def realizar_saque(self, quantidade: float) -> None:
        if quantidade <= self.ContaBancaria.saldo \
                + self.ContaBancaria.limite:
            self.ContaBancaria.saldo -= quantidade
        else:
            print("Não é possível realizar tal saque."
                  "Limite insuficiente.")

    def realizar_deposito(self, quantidade: float) -> None:
        self.ContaBancaria.saldo += quantidade
        if self.ContaBancaria.saldo > 0:
            self.ContaBancaria.__estado = Disponivel.Disponivel()

    def encerrar_conta(self) -> None:
        print(f"Não é possível encerrar sua conta, "
              f"pois você está devendo R${-self.ContaBancaria.saldo}.")
