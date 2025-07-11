import operator

operacoes = {
    "1": operator.add,
    "2": operator.sub,
    "3": operator.mul,
    "4": operator.truediv
}

def main():
    print("""Escolha a operação:
          1: Soma
          2: Subtração
          3: Multiplicação
          4: Divisão""")
    
    while True:
        opcao = input("Opção : ").strip()
        if opcao in operacoes:
             break 
        print("Erro: Opção invalida, escolha um dos nºs mostrados.")
         
    try:
        num1 = float(input('Digite o primeiro nº:'))
        num2 = float(input('Digite o segundo nº: '))
        resultado = operacoes[opcao](num1, num2)
    except ValueError:
        print('Erro: Entrada inválida. Use apenas números.')
    except ZeroDivisionError:
        print('Erro: divisão por 0.')
    else:         
         print(f"Resultado: {resultado}")
    
if __name__ == "__main__":
        main()