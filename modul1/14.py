def formatRupiah(num):
    a = "Rp {:,}".format(num)
    return ".".join(a.split(","))

print(formatRupiah(1500))
print(formatRupiah(2560000))
