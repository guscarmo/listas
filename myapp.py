from random import randint
from time import sleep
computador = randint(0, 10)

resposta = int(input('Em qual número de 0 à 10 eu pensei ? '))

tentativas = 0
while (resposta != computador):
        print("Hmmmmm...")
        sleep(1)
        print("Você errou!!! Não é o número {} =P".format(resposta))
        resposta = int(input("Tente novamente: "))
        tentativas += 1
if tentativas == 1:
    print('Depois de 1 tentativa, você acertou... Parabéns! ')
elif tentativas == 0:
    print('De primeira =O Parabéns!!! Você acertou o número que pensei.')
else:
    print('Demorou ein.... {} tentativas para acertar o número q pensei... Parabéns.'.format(tentativas))