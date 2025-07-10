def calcular_desconto(idade, situacao, conhecimento, comunidade):
    if idade < 18:
        return 0 

    desconto = 0

    opcoes_situacao = {
        "estudante": 10,
        "desempregado": 15,
        "empregado": 0
    }

    desconto += opcoes_situacao.get(situacao, 0)

    if conhecimento == "sim":
        desconto += 5

    if comunidade == "sim":
        desconto += 20

    return desconto


def main():
    print("=== Sistema de Verificação de Desconto em Cursos de TI ===")
    
    try:
        idade = int(input("Qual é a sua idade ? "))

        if idade < 18:
            print("Inelegível a desconto(menor de idade)")
            return

        while True:
            situacao = input("Situação profissional ('estudante', 'desempregado', 'empregado'): ").strip().lower()
            if situacao in ["estudante", "desempregado", "empregado"]:
                break
            print("Erro: Situação inválida. Escolha entre: estudante, desempregado, empregado.")

        while True:
            conhecimento = input("Possui conhecimento prévio em TI? ('sim' ou 'não'): ").strip().lower()
            if conhecimento in ["sim", "não"]:
                break
            print("Erro: Responda com 'sim' ou 'não'.")

        while True:
            comunidade = input("Participa ativamente da comunidade de TI? ('sim' ou 'não'): ").strip().lower()
            if comunidade in ["sim", "não"]:
                break
            print("Erro: Responda com 'sim' ou 'não'.")

        desconto_total = calcular_desconto(idade, situacao, conhecimento, comunidade)
        print(f"Seu desconto é de {desconto_total}%")

    except ValueError:
        print("Erro: Idade deve ser um número inteiro.")


if __name__ == "__main__":
    main()
