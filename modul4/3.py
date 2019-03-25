class MhsTifUMS(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

c0 = MhsTifUMS("Susi", 1, "Bojonegoro", 900000)
c1 = MhsTifUMS("Triana", 2, "Purwosari", 800000)
c2 = MhsTifUMS("Wati", 3, "Jakarta", 700000)
c3 = MhsTifUMS("Rima", 4, "Brebes", 60000)
c4 = MhsTifUMS("Dwi", 5, "Tegal", 50000)
c5 = MhsTifUMS("Novika", 6, "Kelaten", 40000)
c6 = MhsTifUMS("Kori", 7, "Merauke", 20000)
c7 = MhsTifUMS("Indah", 8, "Papua", 30000)
c8 = MhsTifUMS("Prastika", 9, "Jayapura", 20000)
c9 = MhsTifUMS("Fitri", 10, "Ngawi", 370000)
c10 = MhsTifUMS("Cahya", 11, "Gentinga", 12000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def cariUangSakuTerkecilObject(list):
    temp = [list[0]]
    for i in list[1:]:
        if i.uangSaku < temp[0].uangSaku:
            temp = [i]
        elif i.uangSaku == temp[0].uangSaku:
            temp.append(i)
    return temp

a = cariUangSakuTerkecilObject(Daftar)
print(a)
