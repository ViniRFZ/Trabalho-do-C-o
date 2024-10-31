from cao import Cao

def main():
    nome = input("Digite o nome do cão: ")
    raca = input("Digite a raça do cão: ")

    meu_cao = Cao(nome, raca)
    
    while True:
        print("\n--- Menu ---")
        print("1. Acordar o cão")
        print("2. Alimentar o cão")
        print("3. Brincar com o cão")
        print("4. Mostrar status do cão")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            meu_cao.acordar()
        elif escolha == "2":
            meu_cao.alimentar()
        elif escolha == "3":
            meu_cao.brincar()
        elif escolha == "4":
            meu_cao.status()
        elif escolha == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
