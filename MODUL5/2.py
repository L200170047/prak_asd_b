A = [1,2,3,4,5,6,7,8,9]
B = [1,3,4,5]

def gabungkanDuaList(A, B):
    pertama = len(A); kedua = len(B)
    C = list()
    i = 0; j = 0
    while i < pertama and j < kedua:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1

        else :
            C.append(B[j])
            j += 1
    while i < pertama :
        C.append(A[i])
        i += 1
    while j < kedua :
        C.append(B[i])
        i += 1
    return C

print (gabungkanDuaList(A, B))
