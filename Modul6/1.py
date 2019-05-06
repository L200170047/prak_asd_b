class MhsTIF(object):
    def __init__(self, nama, no, kota, us):
        self.nama = nama
        self.no = no
        self.kota = kota
        self.uangSaku = us

c0 = MhsTIF('Susi', 20, 'Bojonegoro', 5000000)
c1 = MhsTIF('Triana', 5, 'Sragen', 2000000)
c2 = MhsTIF('Wati', 20, 'Surakarta', 4500000)
c3 = MhsTIF('Andra', 88, 'Sukoharjo', 935000)
c4 = MhsTIF('Ika', 41, 'Boyolali', 2900000)
c5 = MhsTIF('Andi', 12, 'Solo', 3500000)
c6 = MhsTIF('Eni', 10, 'Klaten', 5450000)
c7 = MhsTIF('Salsa', 67, 'Malang', 8450000)
c8 = MhsTIF('Anto', 26, 'Klaten', 2350000)
c9 = MhsTIF('Ali', 45, 'Karanganyar', 4700000)
c10 = MhsTIF('Jaki', 22, 'Solo', 7650000)

daftar = [c0.no, c1.no, c2.no, c3.no, c4.no, c5.no, c6.no, c7.no, c8.no, c9.no, c10.no]

def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i += 1
            else:
                A[k] = separuhKanan[j]
                j += 1
            k += 1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i += 1
            k += 1

        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j += 1
            k += 1

        return A

print(daftar)
mergeSort(daftar)
print(daftar)

def partisi(A, awal, akhir):
    nilaiPivot = A[awal]

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:

        while penandaKiri <= penandaKanan and \
              A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1

        while A[penandaKanan] >= nilaiPivot and \
              penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan
    
def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)

def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)
    return A

print('\n')
print(daftar)
quickSort(daftar)
print(daftar)
