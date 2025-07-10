#Calculo de média de notas

def calculo_media(notas):
    soma = 0

    for nota in notas:
        soma += nota
    
    media = soma /len(notas) if notas else 0
    return soma, media

def main():
    
    notas = [10.0, 8.0, 9.0, 5.0]

    soma, media = calculo_media(notas)
    print(f"Notas :{notas} \nSoma das notas = {soma} \nMédia = {media}")

if __name__ == "__main__":
    main()