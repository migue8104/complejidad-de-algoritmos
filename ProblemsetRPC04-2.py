
dr_O = int (input())
alyssa= int (input())
konari = int (input())


verificar = False


for a in range(1, dr_O // alyssa + 1):
    for k in range(1, dr_O // konari + 1):
        if (a * alyssa) + (k * konari) == dr_O:
            verificar = True
            break
    if verificar:
        break

if verificar == True:
    print (1)
else:
    print(0)


