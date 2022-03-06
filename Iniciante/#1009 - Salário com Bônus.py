nome = input()
salarioFixo = float(input())
vendas = float(input())

comissao = vendas * 0.15
salarioBonus = salarioFixo + comissao


print("TOTAL = R$ %.2F" % salarioBonus) 
