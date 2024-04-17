import random

def gerar_numeros_sorte(total_numeros, numero_minimo, numero_maximo):
    if total_numeros > (numero_maximo - numero_minimo + 1):
        print("Erro: O número total de números deve ser menor ou igual à faixa de números permitida")
        return None
    numeros_sorte = random.sample(range(numero_minimo, numero_maximo + 1), total_numeros)
    return sorted(numeros_sorte)

def main():
    print("Bem-vindo ao gerador de números da sorte!")
    numero_minimo = int(input("Digite o número mínimo: "))
    numero_maximo = int(input("Digite o número máximo: "))
    while True:
        total_numeros = int(input("Quantos números da sorte você deseja gerar? "))
        numeros_sorte = gerar_numeros_sorte(total_numeros, numero_minimo, numero_maximo)
        if numeros_sorte:
            print("Números da sorte:", numeros_sorte)
            jogar_novamente = input("Deseja gerar mais números da sorte? (s/n) ").lower()
            if jogar_novamente != 's':
                break

if __name__ == "__main__":
    main()