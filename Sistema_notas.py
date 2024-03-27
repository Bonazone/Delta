import time
import os

print("=="*40)
print("{:^80}".format("Sistema de notas"))
print("=="*40,"\n")

while True:
    try:
        bim1 = float(input("Informe a nota da 1° avaliação bimestral (0 - 7.0): "))
        if (bim1 >= 0 and bim1 <= 7):
            break
        else:
            print("Por favor, digite um valor válido!")
            time.sleep(1.8)
            os.system("cls" if os.name == "nt" else "clear") #Limpa a tela
    except ValueError:
        print("Por favor, digite um valor válido!")   
        time.sleep(1.8)
        os.system("cls" if os.name == "nt" else "clear") #Limpa a tela    

while True:
    try:
        ta1 = float(input("Informe a nota dos trabalhos avaliativos (0 - 2.0): "))
        if (ta1 >= 0 and ta1 <= 2):
            break
        else:
            print("Por favor, digite um valor válido!")
            time.sleep(1.8)
            os.system("cls" if os.name == "nt" else "clear")
            print("Informe a nota da 1° avaliação bimestral (0 - 7.0): {}".format(bim1))
    except ValueError:
        print("Por favor, digite um valor válido!")
        time.sleep(1.8)
        os.system("cls" if os.name == "nt" else "clear")
        print("Informe a nota da 1° avaliação bimestral (0 - 7.0): {}".format(bim1))

while True:
    try:
        ted1 = float(input("Informe a nota do TED (0 - 1.0): "))
        if (ted1 >=0 and ted1 <= 1):
            break
        else:
            print("Por favor, digite um valor válido!")  
            time.sleep(1.8)
            os.system("cls" if os.name == "nt" else "clear") 
            print("Informe a nota da 1° avaliação bimestral (0 - 7.0): {}".format(bim1))
            print("Informe a nota dos trabalhos avaliativos (0 - 2.0):{}".format(ta1))
    except ValueError:
        print("Por favor, digite um valor válido!")
        time.sleep(1.8)
        os.system("cls" if os.name == "nt" else "Clear")
        print("=="*40)
        print("{:^80}".format("Sistema de notas"))
        print("=="*40,"\n")
        print("Informe a nota da 1° avaliação bimestral (0 - 7.0): {}".format(bim1))
        print("Informe a nota dos trabalhos avaliativos (0 - 2.0):{}".format(ta1))

bimestre1 = bim1 + ta1 + ted1
print("\nA nota do primeiro bimestre foi: {}".format(bimestre1))
print("=="*40,"\n")

while True:
    try:
        bim2 = float(input("Informe a nota da 1° avaliação bimestral (0 - 7.0): "))
        if (bim2 >= 0 and bim2 <= 7):
            break
        else:
            print("Por favor, digite um valor válido!")
            time.sleep(1.8)
            os.system("cls" if os.name == "nt" else "clear") #Limpa a tela
            print("=="*40)
            print("{:^80}".format("Sistema de notas"))
            print("=="*40,"\n")
            print("Informe a nota da 1° avaliação bimestral (0 - 7.0): {}".format(bim1))
            print("Informe a nota dos trabalhos avaliativos (0 - 2.0):{}".format(ta1))
            print("Informe a nota do TED (0 - 1.0):{}".format(ted1))
            print("\nA nota do primeiro bimestre foi: {}".format(bimestre1))
            print("=="*40,"\n")
    except ValueError:
        print("Por favor, digite um valor válido!")   
        time.sleep(1.8)
        os.system("cls" if os.name == "nt" else "clear") #Limpa a tela 
        print("=="*40)
        print("{:^80}".format("Sistema de notas"))
        print("=="*40,"\n")
        print("Informe a nota da 1° avaliação bimestral (0 - 7.0): {}".format(bim1))
        print("Informe a nota dos trabalhos avaliativos (0 - 2.0):{}".format(ta1))
        print("Informe a nota do TED (0 - 1.0):{}".format(ted1))   
        print("\nA nota do primeiro bimestre foi: {}".format(bimestre1))
        print("=="*40,"\n")
while True:
    try:
        ta2 = float(input("Informe a nota dos trabalhos avaliativos (0 - 2.0): "))
        if (ta2 >= 0 and ta2 <= 2):
            break
        else:
            print("Por favor, digite um valor válido!")
            time.sleep(1.8)
            os.system("cls" if os.name == "nt" else "clear")
            print("=="*40)
            print("{:^80}".format("Sistema de notas"))
            print("=="*40,"\n")
            print("Informe a nota da 1° avaliação bimestral (0 - 7.0): {}".format(bim1))
            print("Informe a nota dos trabalhos avaliativos (0 - 2.0):{}".format(ta1))
            print("Informe a nota do TED (0 - 1.0):{}".format(ted1))
            print("\nA nota do primeiro bimestre foi: {}".format(bimestre1))
            print("=="*40,"\n")
            print("Informe a nota da 2° avaliação bimestral (0 - 7.0): {}".format(bim2))
    except ValueError:
        print("Por favor, digite um valor válido!")
        time.sleep(1.8)
        os.system("cls" if os.name == "nt" else "clear")
        print("=="*40)
        print("{:^80}".format("Sistema de notas"))
        print("=="*40,"\n")
        print("Informe a nota da 1° avaliação bimestral (0 - 7.0): {}".format(bim1))
        print("Informe a nota dos trabalhos avaliativos (0 - 2.0):{}".format(ta1))
        print("Informe a nota do TED (0 - 1.0):{}".format(ted1))
        print("\nA nota do primeiro bimestre foi: {}".format(bimestre1))
        print("=="*40,"\n")
        print("Informe a nota da 2° avaliação bimestral (0 - 7.0): {}".format(bim2))

while True:
    try:
        ted2 = float(input("Informe a nota do TED (0 - 1.0): "))
        if (ted1 >=0 and ted2 <= 1):
            break
        else:
            print("Por favor, digite um valor válido!")  
            time.sleep(1.8)
            os.system("cls" if os.name == "nt" else "clear") 
            print("=="*40)
            print("{:^80}".format("Sistema de notas"))
            print("=="*40,"\n")
            print("Informe a nota da 1° avaliação bimestral (0 - 7.0): {}".format(bim1))
            print("Informe a nota dos trabalhos avaliativos (0 - 2.0):{}".format(ta1))
            print("Informe a nota do TED (0 - 1.0):{}".format(ted1))
            print("\nA nota do primeiro bimestre foi: {}".format(bimestre1))
            print("=="*40,"\n")
            print("Informe a nota da 2° avaliação bimestral (0 - 7.0): {}".format(bim2))
            print("Informe a nota dos trabalhos avaliativos (0 - 2.0):{}".format(ta2))
    except ValueError:
        print("Por favor, digite um valor válido!")
        time.sleep(1.8)
        os.system("cls" if os.name == "nt" else "Clear")
        print("=="*40)
        print("{:^80}".format("Sistema de notas"))
        print("=="*40,"\n")
        print("Informe a nota da 1° avaliação bimestral (0 - 7.0): {}".format(bim1))
        print("Informe a nota dos trabalhos avaliativos (0 - 2.0):{}".format(ta1))
        print("Informe a nota do TED (0 - 1.0):{}".format(ted1))
        print("\nA nota do primeiro bimestre foi: {}".format(bimestre1))
        print("=="*40,"\n")
        print("Informe a nota da 2° avaliação bimestral (0 - 7.0): {}".format(bim2))
        print("Informe a nota dos trabalhos avaliativos (0 - 2.0):{}".format(ta2))

bimestre2 = bim2 + ta2 + ted2
print("\nA nota do segundo bimestre foi: {}".format(bimestre2))
print("=="*40,"\n")

media = (bimestre1 + bimestre2)/2

print("\nA média semestral geral é:{}\n".format(media))
if (media >= 7):
    print("Aluno aprovado!\n")
elif (media < 7 and  media >= 4):
    print("O aluno se encontra em recuperação\n")   
else:
    print("Aluno reprovado\n")

print("=="*40)       


