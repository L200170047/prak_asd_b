class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai',len(self.teks),'karakter.')
    def perbarui(self,stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, kata):
        self.kata = kata
        if self.kata in self.teks:
            return True
        else:
            return False
    def hitungKonsonan(self):
        k = self.teks
        vowel = " AIUEOaiueo"	
        jml = 0	
        for a in k:
            if a.lower() not in vowel :
                jml+=1
        return jml
    def hitungVokal(self):
        k = self.teks
        vowel = " AIUEOaiueo"	
        jml = 0	
        for a in k:
            if a.lower() in vowel :
                jml+=1
        return jml
p9 = Pesan('Indonesia adalah negeri yang indah')
print (p9.apakahTerkandung('ege'))
print (p9.apakahTerkandung('eka'))
p10 = Pesan('Surakarta')
print (p10.hitungKonsonan())
print (p10.hitungVokal())
