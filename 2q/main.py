from ContaBancaria import ContaBancaria
import sys

print(f"Bem vindo ao banco Santo André!")
resposta = input("Você gostaria de criar uma nova conta? (S/N)").upper()
if resposta == "S":
    nome = input(f"Digite o seu nome: ").title()
    cpf = str(input(f"Digite o seu CPF: "))
    Conta = ContaBancaria(nome, cpf)

elif resposta == "N":
    print("O banco Santo André agradece a sua visita! Esperamos que possamos fazer negócios no futuro!")
    sys.exit()

while True:
    print("O que você deseja fazer?")
    opcao = int(input("1 - Sacar.\n2 - Depositar\n3 - Ver seu saldo\n4 - Encerrar a conta.\n"))
    if opcao == 1:
        qte = int(input("Digite a quantidade que você desejar sacar."))
        Conta.realizar_saque(qte)
    elif opcao == 2:
        qte = int(input("Digite a quantidade que você desejar depositar."))
        Conta.realizar_deposito(qte)
    elif opcao == 3:
        print(f"Seu saldo é {Conta.saldo}.")
    elif opcao == 4:
        Conta.encerrar_conta()
    else:
        print("Opção inválida!")
