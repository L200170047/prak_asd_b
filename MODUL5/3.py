def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def selectionSort(A):
    n = len(A)
    for i in range(n - 1):
        indexkecil = cariposisiyangterkecil(A, i, n)
        if indexkecil != 1:
            swap(A, i, indexkecil)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos -1
        A[pos] = nilai

def cariposisiyangterkecil(A, darisini, sampaisini):
    posisiyangterkecil = darisini
    for i in range(darisini+1, sampaisini):
        if A[i] < A[posisiyangterkecil]:
            posisiyangterkecil = i
    return posisiyangterkecil


            
def bubbleSort(A):
    n = len (A)
    for i in range (n-1):
        for j in range (n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

from time import time as detak
from random import shuffle as kocok
k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub); ak=detak();print('bubble : %g detik' %(ak-aw));
aw = detak();selectionSort(u_sel); ak=detak();print('Selection : %g detik' %(ak-aw));
aw = detak();insertionSort(u_ins); ak=detak();print('insertion : %g detik' %(ak-aw));

