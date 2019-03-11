class Manusia(object):
    keadaan="lapar"
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self,s):
        print("Saya baru saja makan", s)
        self.keadaan="kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan="lapar"
    def mengalikanDenganDua(self,n):
        return n*2
class SiswaSMA(Manusia):
    """Class SiswaSMA yang dibangun dari class Manusia"""
    def __init__(self,nama,email,status,alamat):
        """Metode inisialisasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.email = email
        self.status = status
        self.alamat = alamat
    def __str__(self):
        a = "Nama : "+self.nama+'\n'+"Email : "+str(self.email)+'\n'+"Tinggal di : "+self.alamat+'\n'+"Status : "+str(self.status)
        print (a)
    def ambilNama(self):
        print (self.nama)
    def ambilNoInduk(self):
        print (self.email)
    def ambilKelas(self):
        print (self.status)
    def ambilAlamat(self):
        print (self.alamat)
