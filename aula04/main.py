import random


dados = list(range(1, 21)) # [1,2,3,....,21]
aleatorio = random.sample(dados, 2)

print("qual idade do aluno A?")
idade_a = int(input("insira numeros inteiros"))
print("qual idade do aluno B?")
idade_b = int(input("insira numeros inteiros"))
print("qual idade do aluno C?")
idade_c = int(input("insira numeros inteiros"))

def media_adaptada_dois(idade_a,idade_b):
    media = (idade_a+idade_b)/2
    return media

def media_adaptada_tres(idade_a,idade_b,idade_c):
    media = (idade_a+idade_b+idade_c)/3
    return media

print("resultado com dois:")
print(media_adaptada_dois(idade_a,idade_b))

print("resultado com tres:")
print(media_adaptada_tres(idade_a,idade_b,idade_c))