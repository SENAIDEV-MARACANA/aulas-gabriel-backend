#encontrar maior e menor nota na lista

def min_nota(notas):

    menor_nota = None

    for nota in notas:
        if menor_nota is None:
            menor_nota = nota
        elif nota < menor_nota:
            menor_nota = nota
    print(f"Menor nota = {menor_nota}")

def max_nota(notas):

    maior_nota = None

    for nota in notas:
        if maior_nota is None:
            maior_nota = nota
        elif nota > maior_nota:
            maior_nota = nota
    print(f"Maior nota = {maior_nota}")

def main():
    
    notas = [10.0, 8.0, 9.0, 5.0]

    max_nota(notas)
    min_nota(notas)
    
if __name__ == "__main__":
    main()