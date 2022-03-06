peca1 = input().split(" ")
peca2 = input().split(" ")

total = (float(peca1[1]) * float(peca1[2])) + (float(peca2[1]) * float(peca2[2]))

print("VALOR A PAGAR: R$ %.2f" % total)