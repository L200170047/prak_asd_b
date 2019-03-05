def gambarlahPersegiEmpat(p, l):
    for i in range(1, p+1):
        if i==1 or i==p:
            print("@"*l)
        else:
            print("@"+" "*(l-2)+"@")
gambarlahPersegiEmpat(4, 5)
