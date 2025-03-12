from fractions import Fraction as F
from random import randint as r

def gen_mat(n):#generuje jednotkovou matici tvaru nxn
    mat = []
    for i in range(n):
        line = [F(r(-100, 100)) for j in range(n)]
        mat.append(line)
    return mat

def mult(a, line):#ekvivalentní úprava násobení řádku číslem
    return [a*i for i in line]

def add(line1, line2):#ekvivalentní úprava přičtení jiného řádku
    return [line1[i] + line2[i] for i in range(len(line1))]

def det(X):#počítá determinant matice pomocí řádkových úprav
    A = X.copy()
    n = len(A)
    det = 1
    
    for i in range(n):#prochází matici po hlavní diagonále
        if A[i][i] == 0:#pokud je prvek na diagonále 0
            for j in range(i, n):#prochází prvky pod ním
                if A[j][i] != 0:#pokud najde nenulový
                    A[i], A[j] = A[j], A[i]#prohodí řádky v matici, tak aby na diagonále bylo nenulové číslo
                    det *= -1#vynásobí determinant -1
                    break
            else:#pokud cyklus proběhne celý, tak pod nulou na diagonále již není nenulové číslo, tzn. matice není regulární
                return 0
            
        for j in range(i+1, n):#prochází prvky pod nenulovým číslem na diagonále
            A[j] = add(mult(-A[j][i]/A[i][i], A[i]), A[j])#nuluje je pomocí čísla na diagonále
        det *= A[i][i]#vynásobí determinant číslem na diagonále
        
    return det

def cramer(X, vector_b, i):
    A = X.copy()
    det_A = det(A)
    if det_A == 0:
        return "ne"
    A_i = []
    for line in A:
        line[i-1] = vector_b[i-1]
        A_i.append(line)
    x_i = det(A_i)/det_A
    return x_i

