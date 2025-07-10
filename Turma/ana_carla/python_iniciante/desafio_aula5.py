def main():
    print("TABUADA SIMPLES")

    try:
        numero = int(input("Digite um número para ver a tabuada: "))
    except ValueError:
        print("Erro: Entrada inválida. Use apenas números inteiros.")
        return
    
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

if __name__ == "__main__":
    main()
