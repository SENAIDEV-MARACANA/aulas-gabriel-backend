#separar alunos aprovados de reprovados

def indicador_aprovacao(notas):
    aprovados = []
    reprovados = []

    for nota in notas:
        if nota >= 7.0:
            aprovados.append(nota)
        else:
            reprovados.append(nota)
    
    return aprovados, reprovados

def main():

    notas = [9.0, 5.0, 8.5, 4.3, 9.9, 6.8, 10.0]

    aprovados, reprovados = indicador_aprovacao(notas)

    print(f"Aprovados ({len(aprovados)}) : {aprovados}\nReprovados ({len(reprovados)}): {reprovados}")


if __name__ == "__main__":
    main()

    

    