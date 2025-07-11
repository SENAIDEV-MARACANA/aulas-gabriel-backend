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

def interpretar_resposta_sim_nao(resposta):
    resposta = resposta.strip().lower()
    if resposta in ["sim", "s"]:
        return "sim"
    elif resposta in ["não", "nao", "n"]:
        return "não"
    else:
        return None
    
def main():
    print("=== Sistema de Verificação de Desconto em Cursos de TI ===")

    while True:
        idade_input = input("Qual é a sua idade ? ").strip()
        try:
            idade = int(idade_input)
            if 0 <= idade <= 100:
                break
            else:
                print("Erro: Idade fora do intervalo permitido.")
        except ValueError:
            print("Erro: Digite apenas números inteiros.")

    if idade < 18:
        print("Inelegível a desconto(menor de idade)")
        return

    while True:
        situacao = input("Situação profissional ('estudante', 'desempregado', 'empregado'): ").strip().lower()
        if situacao in ["estudante", "desempregado", "empregado"]:
            break
        print("Erro: Situação inválida. Escolha entre: estudante, desempregado, empregado.")

    while True:
        conhecimento_input = input("Possui conhecimento prévio em TI? ('sim' ou 'não'): ").strip().lower()
        conhecimento = interpretar_resposta_sim_nao(conhecimento_input)
        if conhecimento:
            break
        print("Erro: Responda com 'sim' ou 'não'.")

    while True:
        comunidade_input = input("Participa ativamente da comunidade de TI? ('sim' ou 'não'): ").strip().lower()
        comunidade = interpretar_resposta_sim_nao(comunidade_input)
        if comunidade:
            break
        print("Erro: Responda com 'sim' ou 'não'.")

    desconto_total = calcular_desconto(idade, situacao, conhecimento, comunidade)
    print(f"Seu desconto é de: {desconto_total}%")

if __name__ == "__main__":
    main()
