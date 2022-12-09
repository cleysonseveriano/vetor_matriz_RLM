from random import random

#CADASTRO DE MATRIZES
lA = int(input("Digite o nº de linhas de A: "))
cA = int(input("Digite o nº de colunas de A: "))

lB = int(input("Digite o nº de linhas de B: "))
cB = int(input("Digite o nº de colunas de B: "))

A = [None]* lA
for i in range(len(A)):
    A[i] = [None]*cA

B = [None]* lB
for i in range(len(B)):
    B[i] = [None]*cB

for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = int(random()*10)

for i in range(len(B)):
    for j in range(len(B[i])):
        B[i][j] = int(random()*10)

print('Matriz A')
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end='    ')
    print()
print()

print('Matriz B')
for i in range(len(B)):
    for j in range(len(B[i])):
        print(B[i][j], end='    ')
    print()

def primo(number):
    j = 0
    for i in range(1, number + 1):
        if number%i==0:
            j+=1
    if j==2:
        return True
    else:
        return False

def questao_1(lA,cA,A,lB,cB,B):
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

def questao_2(lA,cA,A,lB,cB,B):
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

    D = [None]*cB
    for i in range(len(B)):
        D[i] = [None]*lB

    for i in range(len(B)):
        for j in range(len(B[i])):
            D[i][j] = B[j][i]
    
    print("Matriz D")
    for i in range(len(D)):
        for j in range(len(D[i])):
            print(D[i][j], end='    ')
        print()

def questao_3(lA,cA,A,lB,cB,B):
#OPERAÇÃO PARA CONSTRUÇÃO DA MATRIZ SOMA
#ATRIBUÍMOS VALORES A MATRIZ SOMA
    if (lA==lB) and (cA==cB):
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] += B[i][j]
        print('Matriz SOMA')
        for i in range(len(A)):
            for j in range(len(A[i])):
                print(A[i][j], end='    ')
            print()
    else:
        print('O número de linhas e colunas de A e B, devem ser iguais')

def questao_6(lA,cA,A):
    if (lA==1 and cA==1) or (lA==1 and cA==0) or (lA==0 and cA==1):
        A = [None]
        A[0] = int(random()*10)
        print(f'Vetor unitário: {A}')
    elif lA>1 and cA==1:
        print('Vetor coluna A')
        for i in range(len(A)):
            for j in range(len(A[i])):
                print(A[i][j], end='    ')
            print()
        #MEDIA VETOR
        media = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                media += A[i][j]
        media = media/len(A)
        print(f'Média do vetor coluna: {media:.2f}')
    elif lA==1 and cA>1:
        print('Vetor linha A')
        for i in range(len(A)):
            for j in range(len(A[i])):
                print(A[i][j], end='    ')
            print()
        #MEDIA COLUNA
        media = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                media += A[i][j]
            media = media/len(A[i])
        print(f'Média do vetor linha: {media:.2f}')
    else:
        #MATRIZ COLUNA
        mColuna = [None]
        for i in range(len(mColuna)):
            mColuna[i] = [None]*cA
        somaLA = 0
        for r in range(cA):
            somaLA = 0
            for j in range(len(A)):
                somaLA+=A[j][r]
            mColuna[0][r] = somaLA/len(A)

        print('MATRIZ COLUNA')
        for i in range(len(mColuna)):
            for j in range(len(mColuna[i])):
                print(f'{mColuna[i][j]:.2f}', end='     ')

        print()

        #MATRIZ COLUNA
        mColuna =[None]*lA
        for i in range(len(mColuna)):
            mColuna[i] = [None]
        for i in range(len(mColuna)):
            somaCA = 0
            for j in range(cA):
                somaCA+=A[i][j]
            mColuna[i][0] = somaCA/cA

        print('MATRIZ COLUNA')
        for i in range(len(mColuna)):
            print(f'{mColuna[i][0]:.2f}', end='\n')

def questao_7(lB,cB,B):
    lB = int(input("Digite o nº de linhas de B: "))
    cB = int(input("Digite o nº de colunas de B: "))
    if (lB==1 and cB==1) or (lB==1 and cB==0) or (lB==0 and cB==1):
        B = [None]
        B[0] = int(random()*10)
        print(f'Vetor unitário: {B}')
    elif lB==1 and cB>1:
        nP = 0
        for i in range(len(B)):
            for j in range(len(B[i])):
                if primo(B[i][j])==True:
                    nP+=1
        print(f'Qtnd de n°primos: {nP}')
    elif lB>1 and cB==1:
        B = [None]* lB
        for i in range(len(B)):
            B[i] = [None]*cB
        for i in range(len(B)):
            for j in range(len(B[i])):
                B[i][j] = int(random()*10)
        print('Vetor coluna B')
        for i in range(len(B)):
            for j in range(len(B[i])):
                print(B[i][j], end='    ')
            print()
        nP = 0
        for i in range(len(B)):
            for j in range(len(B[i])):
                if primo(B[i][j])==True:
                    nP+=1
        print(f'Qtnd de n°primos: {nP}')
    else:
        #Matriz B Transposta
        BT = [None]*cB
        for i in range(len(BT)):
            BT[i] = [None]*lB
        for i in range(len(BT)):
            for j in range(len(BT[i])):
                BT[i][j] = B[j][i]
        print('Matriz BT')
        for i in range(len(BT)):
            for j in range(len(BT[i])):
                print(BT[i][j], end='    ')
            print()
        print()
        print('Matriz X')
        X =[None]*cB
        for i in range(len(X)):
            X[i] = [None]*lB
        for i in range(len(X)):
            for j in range(len(X[i])):
                X[i][j] = BT[i][j] * 2.5
        for i in range(len(X)):
            for j in range(len(X[i])):
                print(X[i][j], end='    ')
            print()

def questao_8(lA,cA,A,lB,cB,B):
    print()
    N = int(input('Digite [1] ou [0]: '))
    while ((N != 0) and (N != 1)):
        N = int(input('Digite [1] ou [0]: '))

    if N==1:
        Z = A
        #VETOR LINHA
        if lA==1 and cA>1:
            Z_aux = [0]*cA
            for i in range(len(Z_aux)):
                Z_aux[i] = [0]*cA
            print()
            print('Matriz Z LINHA')
            soma = 0
            for i in range(len(Z_aux)):
                for j in range(len(Z_aux[i])):
                    if i == j:
                        Z_aux[i][j] = Z[0][j]
                        soma+=Z[0][j]
            Z = Z_aux
            for i in range(len(Z)):
                for j in range(len(Z[i])):
                    print(Z[i][j], end='    ')
                print()
            print()
            print(f'A soma do vetor linha é: {soma}')
        #VETOR COLUNA
        elif lA>1 and cA==1:
            Z_aux = [0]*lA
            for i in range(len(Z_aux)):
                Z_aux[i] = [0]*lA
            print()
            print('Matriz Z')
            for i in range(len(Z_aux)):
                for j in range(len(Z_aux[i])):
                    if i == j:
                        Z_aux[i][j] = Z[i][0]
            Z = Z_aux
            for i in range(len(Z)):
                for j in range(len(Z[i])):
                    print(Z[i][j], end='    ')
                print()  
        #MATRIZ QUADRADA
        elif lA==cA:
            Z_aux = [None]*lA
            for i in range(len(Z_aux)):
                Z_aux[i] = [None]
            for i in range(len(Z_aux)):
                for j in range(len(Z)):
                    if i == j:
                        Z_aux[i][0] = Z[i][j]
            print('\nMATRIZ COLUNA')
            for i in range(len(Z_aux)):
                for j in range(len(Z_aux[i])):
                    print(Z_aux[i][j], end='    ')
                print()
            print()
        #DEMAIS VETORES
        else:
            soma = 0
            for i in range(len(Z)):
                for j in range(len(Z[i])):
                    soma+=Z[i][j]
            print(f'A soma do vetor é: {soma}')

    elif N==0:
        Z = B
        #VETOR LINHA
        if lB==1 and cB>1:
            Z_aux = [0]*cB
            for i in range(len(Z_aux)):
                Z_aux[i] = [0]*cB
            print()
            print('Matriz Z')
            soma = 0
            for i in range(len(Z_aux)):
                for j in range(len(Z_aux[i])):
                    if i == j:
                        Z_aux[i][j] = Z[0][j]
                        soma+=Z[0][j]
            Z = Z_aux
            for i in range(len(Z)):
                for j in range(len(Z[i])):
                    print(Z[i][j], end='    ')
                print()
            print()
            print(f'A soma do vetor linha é: {soma}')
        #VETOR COLUNA
        elif lB>1 and cB==1:
            Z_aux = [0]*lB
            for i in range(len(Z_aux)):
                Z_aux[i] = [0]*lB
            print()
            print('Matriz Z')
            for i in range(len(Z_aux)):
                for j in range(len(Z_aux[i])):
                    if i == j:
                        Z_aux[i][j] = Z[i][0]
            Z = Z_aux
            for i in range(len(Z)):
                for j in range(len(Z[i])):
                    print(Z[i][j], end='    ')
                print()  
        #MATRIZ QUADRADA
        elif lB==cB:
            Z_aux = [None]*lB
            for i in range(len(Z_aux)):
                Z_aux[i] = [None]
            for i in range(len(Z_aux)):
                for j in range(len(Z)):
                    if i == j:
                        Z_aux[i][0] = Z[i][j]
            print('\nMATRIZ COLUNA')
            for i in range(len(Z_aux)):
                for j in range(len(Z_aux[i])):
                    print(Z_aux[i][j], end='    ')
                print()
            print()
        #DEMAIS VETORES
        else:
            soma = 0
            for i in range(len(Z)):
                for j in range(len(Z[i])):
                    soma+=Z[i][j]
            print(f'A soma do vetor é: {soma}')



questao_6(lA,cA,A)