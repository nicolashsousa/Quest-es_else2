#Questão0
numero = float(input("Digite um numero:"))
par_ou_impar = numero%2
if par_ou_impar != 0:
    print("Impar")
else:
    print("Par")
#Questão1
num1 = float(input("Digite um numero:"))
num2 = float(input("Digite um numero:"))
num3 = float(input("Digite um numero:"))
if num1 > num2 > num3:
    print("Maior:",num1)
    print("Menor:",num3)
elif num1 > num3 > num2:
    print("Maior:",num1)
    print("Menor:",num2)
elif num3 > num2 > num1:
    print("Maior:",num3)
    print("Menor:",num1)
elif num3 > num1 > num2:
    print("Maior:",num3)
    print("Menor:",num2)
elif num2 > num1 > num3:
    print("Maior:",num2)
    print("Menor:",num3)
elif num2 > num3 > num1:
    print("Maior:",num2)
    print("Menor:",num1)
#Questão2
nota1 = float(input("Digite a nota:"))
nota2 = float(input("Digite a nota:"))
nota3 = float(input("Digite a nota:"))
nota4 = float(input("Digite a nota:"))
media = (nota1+nota2+nota3+nota4)/4
if media >= 7:
    print("Media:",media)
    print("Aluno aprovado")
elif 5 <= media <= 6.9:
    print("Media:",media)
    print("Aluno em exame")
else:
    print("Media:",media)
    print("Aluno reprovado")
#Questão3
nota1 = float(input("Digite a nota:"))
nota2 = float(input("Digite a nota:"))
nota3 = float(input("Digite a nota:"))
nota4 = float(input("Digite a nota:"))
media = (nota1+nota2+nota3+nota4)/4
if media >= 7:
    print("Media:",media)
    print("Aluno aprovado")
elif 5 <= media <= 6.9:
    print("Media:",media)
    print("Aluno em exame")
    nota_exame = float(input("Digite a nota:"))
    print("Nota do exame:",nota_exame)
    media_final = (media+nota_exame)/2
    if media_final >= 5:
        print("Media final:",media_final)
        print("Aluno aprovado")
    else:
        print("Media final:",media_final)
        print("Aluno reprovado")
else:
    print("Media:",media)
    print("Aluno reprovado")
#Questão5
mes = int(input("Digite o numero do mês:"))
if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Mês invalido")
#Questão6
dia = int(input("Digite o dia:"))
mes = int(input("Digite o mês:"))
ano = int(input("Digite o ano:"))
if 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 1:
    print("Data valida")
else:
    print("Data invalida")
#Questão7
produto = int(input("Digite o codigo do produto:"))
if produto == 1:
    print("Milkshake")
elif produto == 2:
    print("Hamburguer")
elif produto == 3:
    print("Sorvete")
elif produto == 4:
    print("Refrigerante")
else:
    print("Codigo invalido")
#Questão8
filo_animal = input("Vertebrado ou Invertebrado? ")
if filo_animal == "vertebrado":
    classe_animal = input("Ave ou Mamifero? ")
    if classe_animal == "ave":
        alimento_animal = input("Carnivoro ou Onivoro? ")
        if alimento_animal == "carnivoro":
            print("Aguia")
        elif alimento_animal == "onivoro":
            print("Pomba")
        else:
            print("Invalido")
    elif classe_animal == "mamifero":
        alimento_animal = input("Herbivoro ou Onivoro? ")
        if alimento_animal == "herbivoro":
            print("Vaca")
        elif alimento_animal == "onivoro":
            print("Homem")
        else:
            print("Invalido")
    else:
        print("Invalido")
elif filo_animal == "invertebrado":
    classe_animal = input("Inseto ou Anelideo? ")
    if classe_animal == "inseto":
        alimento_animal = input("Hematofago ou Herbivoro? ")
        if alimento_animal == "hematofago":
            print("Pulga")
        elif alimento_animal == "herbivoro":
            print("Lagarta")
        else:
            print("Invalido")
    elif classe_animal == "anelideo":
        alimento_animal = input("Hematofago ou Onivoro? ")
        if alimento_animal == "hematofago":
            print("Sanguessuga")
        elif alimento_animal == "onivoro":
            print("Minhoca")
        else:
            print("Invalido")
    else:
        print("Invalido")
else:
    print("Invalido")