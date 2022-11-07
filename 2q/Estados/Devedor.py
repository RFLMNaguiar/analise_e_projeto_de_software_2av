import Disponivel
import EstadoContaBancaria


class Devedor(EstadoContaBancaria):

    def realizar_saque(self, quantidade):
        if quantidade <= self.ContaBancaria.saldo + self.ContaBancaria.limite:
            self.ContaBancaria.saldo -= quantidade
        else:
            print("Não é possível realizar tal saque. Limite insuficiente.")

    def realizar_deposito(self, quantidade):
        self.ContaBancaria.saldo += quantidade
        if self.ContaBancaria.saldo > 0:
            self.ContaBancaria.__estado = Disponivel.Disponivel()

    def encerrar_conta(self):
        print(f"Não é possível encerrar sua conta, pois você está devendo R${-self.ContaBancaria.saldo}.")
