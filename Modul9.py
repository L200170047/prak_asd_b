class simpulbiner(object):
    def __init__(self, data):
        self.data=data
        self.kiri=None
        self.kanan=None
def preordertrav (subpohon, isi):
    if subpohon is not None:
        isi.append(subpohon.data)
        preordertrav(subpohon.kiri, isi)
        preordertrav(subpohon.kanan, isi)
def ukuranpohon(akar):
    isi=[]
    preordertrav(A, isi)
    print ("ukuran Pohon: ", len(isi))
def levelcheck(root):
    if root is not None:
        count, le, ri = 0, 0, 0
        if root.data is not None:
            count +=1
        if root.kiri is not None:
            le = levelcheck(root.kiri)
        if root.kanan is not None:
            ri = levelcheck(root.kanan)
        if le > ri:
            count += le
        else:
            count += ri
        return count
def cetakdatalevel(root, level=0):
    if root is not None:
        print(str(root.data)+ ",level "+str(level))
        if root.kiri is not None:
            cetakdatalevel(root.kiri, level+1)
        if root.kanan is not None:
            cetakdatalevel(root.kanan, level+1)
A=simpulbiner('Ambarawa')
B=simpulbiner('Bantul')
C=simpulbiner('Cimahi')
D=simpulbiner('Denpasar')
E=simpulbiner('Enrekang')
F=simpulbiner('Flores')
G=simpulbiner('Garut')
H=simpulbiner('Halmahera Timur')
I=simpulbiner('Indramayu')
J=simpulbiner('Jakarta')

A.kiri=B; A.kanan=C
B.kiri=D; B.kanan=E
C.kiri=F; C.kanan=G
E.kiri=H
G.kanan=I

ukuranpohon(A)
print(levelcheck(A))
cetakdatalevel(A)
