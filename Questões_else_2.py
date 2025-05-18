#Questão0
numero = float(input("Digite um numero:"))
if (numero%2) != 0:
    print(numero,"é impar")
else:
    print(numero,"é par")
#Questão1
a = float(input("Digite o 1º numero:"))
b = float(input("Digite o 2º numero:"))
c = float(input("Digite o 3º numero:"))
if a > b:
    if a > c:
        if b > c:
            print("Maior:",a)
            print("Menor:",c)
        else:
            print("Maior:",a)
            print("Menor:",b)
    else:
        print("Maior:",c)
        print("Menor:",b)
elif b > c:
    if a > c:
        print("Maior:",b)
        print("Menor:",c)
    else:
        print("Maior:",b)
        print("Menor:",a)
else:
    if a > b:
        print("Maior:",c)
        print("Menor:",b)
    else:
        print("Maior:",c)
        print("Menor:",a)
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
    nota_exame = float(input("Digite a nota do exame:"))
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
mes = int(input("Digite o nº do mês:"))
ano = int(input("Digite o ano:"))
if 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 1:
    print(dia,"/",mes,"/",ano)
    print("Data valida")
else:
    print("Data invalida")
#Questão7
print("Milkshake = 1 Hamburguer = 2 Sorvete = 3 Refrigerante = 4")
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
filo_animal = input("Vertebrado(1) ou Invertebrado(0)? ")
if filo_animal == "1":
    classe_animal = input("Ave(1) ou Mamifero(0)? ")
    if classe_animal == "1":
        alimento_animal = input("Carnivoro(1) ou Onivoro(0)? ")
        if alimento_animal == "1":
            print("Aguia")
        elif alimento_animal == "0":
            print("Pomba")
        else:
            print("Invalido")
    elif classe_animal == "0":
        alimento_animal = input("Herbivoro(1) ou Onivoro(0)? ")
        if alimento_animal == "1":
            print("Vaca")
        elif alimento_animal == "0":
            print("Homem")
        else:
            print("Invalido")
    else:
        print("Invalido")
elif filo_animal == "0":
    classe_animal = input("Inseto(1) ou Anelideo(0)? ")
    if classe_animal == "1":
        alimento_animal = input("Hematofago(1) ou Herbivoro(0)? ")
        if alimento_animal == "1":
            print("Pulga")
        elif alimento_animal == "0":
            print("Lagarta")
        else:
            print("Invalido")
    elif classe_animal == "0":
        alimento_animal = input("Hematofago(1) ou Onivoro(0)? ")
        if alimento_animal == "1":
            print("Sanguessuga")
        elif alimento_animal == "0":
            print("Minhoca")
        else:
            print("Invalido")
    else:
        print("Invalido")
else:
    print("Invalido")
