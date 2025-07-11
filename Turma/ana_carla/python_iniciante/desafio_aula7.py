password = 123
answer = 0
tryes = 0

while answer != password:
    answer = int(input('Qual é a senha ?'))
    tryes += 1
    if(answer == password):
        print('Senha correta')
    elif(tryes == 3):
        print('Tentativas excedidas')
        break
