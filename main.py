from calculator import somar, subtrair, multiplicar, dividir

def menu():
    print("\n" + "="*30)
    print("🧮  CALCULADORA PYTHON  📱")
    print("="*30)
    print("Escolha a operação:")
    print("1. ➕ Somar")
    print("2. ➖ Subtrair")
    print("3. ✖️ Multiplicar")
    print("4. ➗ Dividir")
    print("0. 🚪 Sair")
    print("-"*30)

while True:
    menu()
    opcao = input("Digite a opção: ").strip()

    if opcao == "0":
        print("\nEncerrando a calculadora. Até logo!\n")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("\n❌ Opção inválida. Tente novamente.")
        continue

    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
    except ValueError:
        print("\n⚠️ Entrada inválida. Use números válidos.")
        continue

    if opcao == "1":
        resultado = somar(a, b)
    elif opcao == "2":
        resultado = subtrair(a, b)
    elif opcao == "3":
        resultado = multiplicar(a, b)
    elif opcao == "4":
        if b == 0:
            print("\n🚫 Erro: divisão por zero não é permitida.")
            continue
        resultado = dividir(a, b)

    print(f"\n✅ Resultado: {resultado}")
