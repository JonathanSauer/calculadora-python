import calculator

def menu():
    print("Calculadora Python")
    print("Escolha a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")

while True:
    menu()
    escolha = input("Digite a opção: ")

    if escolha == "0":
        print("Saindo...")
        break

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if escolha == "1":
        print("Resultado:", calculator.somar(a, b))
    elif escolha == "2":
        print("Resultado:", calculator.subtrair(a, b))
    elif escolha == "3":
        print("Resultado:", calculator.multiplicar(a, b))
    elif escolha == "4":
        try:
            print("Resultado:", calculator.dividir(a, b))
        except ValueError as e:
            print("Erro:", e)
    else:
        print("Opção inválida.")