import random
pc = random.randint(1,10)
u =  int(input("Tente adivinhar um numero de 1 a 10: "))
if (u == pc):
    print("Você acertou!")
else:
    print("Opa, numero errado!") 
    print("O numero correto é: {}".format(pc))    