from EstadoContaBancaria import EstadoContaBancaria


class Devedor(EstadoContaBancaria):
    def realizar_saque(self, dinheiro_disponivel: float, quantidade: float) -> float:
        if dinheiro_disponivel >= 0:
            return quantidade - dinheiro_disponivel
        else:
            print("Não é possível realizar tal saque."
                  "Limite insuficiente.")

    def realizar_deposito(self, quantidade: float) -> float:
        return quantidade

    def encerrar_conta(self) -> None:
        print(f"Não é possível encerrar sua conta, pois você está devendo.")
        return None
