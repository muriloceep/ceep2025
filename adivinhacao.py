import random
import os
erros=0
sorteado=random.randrange(0,100)
jogador=int(input("digite seu numero    "))
while(sorteado!=jogador):
    os.system('cls')
    if(sorteado>jogador):
        print("ERRO, o número é maior")
    elif(sorteado<jogador):
        print("ERRO, o número é menor")
    erros+=1
    jogador=int(input("digite seu número:    "))
erros+=1
print("Número" + str(jogador) + " , você acertou em: " + str(erros) + "tentativas")
