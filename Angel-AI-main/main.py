from robot.process.FinancialMarket import monitor_stocks

def main():
    while True:
        print("\n" + "=" * 30)
        print("      🛠 MENU PRINCIPAL 🛠      ")
        print("=" * 30)
        print("1️⃣  📈 Monitorar Mercado Financeiro")
        print("2️⃣  💬 Enviar Mensagem no WhatsApp")
        print("3️⃣  📊 Exibir Relatórios")
        print("4️⃣  ⚙️  Configurações")
        print("5️⃣  ❌ Sair")
        print("=" * 30)

        opcao = input("🔹 Escolha uma opção: ")

        if opcao == "1":
            print("\n▶️ Iniciando monitoramento do mercado financeiro...\n")
            monitor_stocks()
        elif opcao == "2":
            print("\n▶️ Abrindo WhatsApp Messenger...\n")
        elif opcao == "3":
            print("\n▶️ Exibindo relatórios...\n")
        elif opcao == "4":
            print("\n▶️ Acessando configurações...\n")
        elif opcao == "5":
            print("\n❌ Saindo do programa...\n")
            break
        else:
            print("\n⚠️ Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()
