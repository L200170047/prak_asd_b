from random import randint

tebak = randint(1, 101)
print("Permainan tebak angka.")
print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.")
i = 1
gameOver = True
while i <= 8 :
    a = int(input("Masukkan tebakan ke-"+str(i)+" :> "))
    if a == tebak:
        print("Ya. Anda benar")
        gameOver = False
        break
    else:
        if a < tebak:
            print("Itu terlalu kecil. Coba lagi")
        else:
            print("Itu terlalu besar. Coba lagi")
    i = i+1
if gameOver:
    print("Permainan selesai")
