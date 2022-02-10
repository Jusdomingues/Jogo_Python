print("Bem vindo ao jogo de Adivinhação!")
print("---------------------------------")

numero_secreto = 13

chute_str = input("Digite sua aposta de número secreto:")
print("Você digitou", chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
    print("Você adivinhou o número secreto!")
else:
    print("Você errou o número secreto!")

print("Fim do jogo")