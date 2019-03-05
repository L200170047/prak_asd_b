def jumlahHurufVokal(input):
    total = 0
    vkl = ["a", "i", "u", "e", "o"]
    for i in input:
        if i in vkl:
            total+=1
    return [len(input), total]

def jumlahHurufKonsonan(input):
    total = 0
    vkl = ["a", "i", "u", "e", "o"]
    for i in input:
        if i in voc:
            total+=1
    return [len(input), len(input)-total]

v = jumlahHurufVokal("Surakarta")
k = jumlahHurufKonsonan("Surakarta")

print(v)
print(k)
