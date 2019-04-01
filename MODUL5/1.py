class mhs(object) :
    """Class mahasiswa dengan berbagai metode"""
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__ (self) :
        s = self.nama + ', NIM' + str(self.NIM)\
            +'.Tinggal di ' + self.kotaTinggal \
            +'. Uang saku Rp' + str(self.uangSaku)\
            +' tiap bulannya.'
        return s
    def ambilNama(self) :
        return self.nama
    def ambilNIM(self) :
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku

a0 = mhs("Ika", 10, "Sukoharjo", 240000)
a1 = mhs("Budi", 51, "Sragen", 230000)
a2 = mhs("Ahmad", 2, "Surakarta", 250000)
a3 = mhs("Chandra", 18, "Surakarta", 2350000)
a4 = mhs("Eka", 4, "Boyolali", 230000)
a5 = mhs("Fandi", 31, "Salatiga", 250000)
a6 = mhs("Deni", 13, "Klaten", 245000)
a7 = mhs("Galuh", 5, "Wonogiri", 245000)
a8 = mhs("Janto", 23, "Klaten", 245000)
a9 = mhs("Hasan", 64, "Karanganyar", 270000)
a10 = mhs("Khalid", 29, "Purwodadi", 265000)

daftar = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]

target = "Klaten"
def cari(daftar, target):
    a = []
    indeks = 0
    for i in daftar:
        if i.kotaTinggal == target:
            a.append(indeks)
        indeks += 1
    return a
print (cari(daftar, target))

kumpulan = []
for a in daftar :
    kumpulan.append(a.ambilUangSaku())
def kecil(kumpulan):
    n = len(kumpulan)
    terkecil = kumpulan[0]
    for i in range (1,n):
        if kumpulan[i] < terkecil:
            terkecil =kumpulan[i]
    return terkecil

print (kecil(kumpulan))

def kembalikanNama(kumpulan):
    li = []
    co = 1
    n = len(kumpulan)
    terkecil = kumpulan[0].ambilUangSaku()
    for i in range (1,n):
        if kumpulan[i].ambilUangSaku() < terkecil:
            li.append(co)
        co += 1
    res = []
    for i in li:
        res.append(kumpulan[i].ambilNama())
    return res

print (kembalikanNama(daftar))

kumpulan = []
for a in daftar :
    kumpulan.append(a.ambilNIM())
def insertionSort(kumpulan):
    n = len(kumpulan)    
    for i in range (1, n):
        nilai = kumpulan[i]
        pos = i
        while pos > 0 and nilai < kumpulan[pos - 1] :
            kumpulan[pos] = kumpulan[pos -1]
            pos = pos -1
            kumpulan[pos] = nilai

insertionSort(kumpulan)
print (kumpulan)
