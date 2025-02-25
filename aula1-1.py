#o \n serve para pular a linha

#local de input dos dados
a = float(input("Digite o valor para a letra A: "))
b = float(input("Digite o valor para a letra B: "))

#resultados
print("O valor de A é: ", a)
print("O valor de A é: ", b)
print("O resultado da soma entre o A e o B é: ", a+b)
print("O resultado da subtração entre o A e o B é: ", a-b)
print("O resultado da divisão de A por B é: ", a/b)
print("O resultado da divisão de B por A é: ", b/a)
print("A parte inteira da divisão de A por B é: ", a//b)
print("A parte inteira da divisão de B por A é: ", b//a)
print("O resultado da potenciação de A sobre B é: ", a**b)

#valida se o A é PAR ou ÍMPAR
if a % 2 == 0:
    print("O A é PAR")
else:
    print("O A é IMPAR")

#valida se o B é PAR ou ÍMPAR    
if b % 2 == 0:
    print("O A é PAR")
else:
    print("O A é IMPAR")
    
    
#valida se o A = B
if a != b:
    print("O A é diferente de B")
else:
    print("O A é igual ao B")