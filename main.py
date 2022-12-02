from random import random
import face_recognition
lA = int(input("Digite o nº de linhas de A: "))
cA = int(input("Digite o nº de colunas de A: "))

lB = int(input("Digite o nº de linhas de B: "))
cB = int(input("Digite o nº de colunas de B: "))

def questao_1(lA,cA,lB,cB):
#CADASTRO DE MATRIZES
    A = [None]* lA
    for i in range(len(A)):
        A[i] = [None]*cA

    B = [None]* lB
    for i in range(len(B)):
        B[i] = [None]*cB

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = int(random()*11)

    for i in range(len(B)):
        for j in range(len(B[i])):
            B[i][j] = int(random()*11)

    print(A)
    print(B)

    x = int(input("Digite x: "))
    y = int(input("Digite y: "))

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = A[i][j] * x

    print('Matriz A')
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end='    ')
        print()
    print()
    for i in range(len(B)):
        for j in range(len(B[i])):
            B[i][j] = B[i][j] * y

    print('Matriz B')
    for i in range(len(B)):
        for j in range(len(B[i])):
            print(B[i][j], end='    ')
        print()

def questao_2(lA,cA,lB,cB):
    #CADASTRO DE MATRIZES
    A = [None]* lA
    for i in range(len(A)):
        A[i] = [None]*cA

    B = [None]* lB
    for i in range(len(B)):
        B[i] = [None]*cB

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = int(random()*11)

    for i in range(len(B)):
        for j in range(len(B[i])):
            B[i][j] = int(random()*11)

    print(A)
    print(B)

    x = int(input("Digite x: "))
    y = int(input("Digite y: "))

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = A[i][j] * x

    print('Matriz A')
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end='    ')
        print()
    print()
    for i in range(len(B)):
        for j in range(len(B[i])):
            B[i][j] = B[i][j] * y

    print('Matriz B')
    for i in range(len(B)):
        for j in range(len(B[i])):
            print(B[i][j], end='    ')
        print()
        
    C = [None]*cA
    for i in range(len(C)):
        C[i] = [None]*lA

    for i in range(len(C)):
        for j in range(len(C[i])):
            C[i][j] = A[j][i]
    
    print("Matriz C")
    for i in range(len(C)):
        for j in range(len(C[i])):
            print(C[i][j], end='    ')
        print()
questao_2(lA,cA,lB,cB)    