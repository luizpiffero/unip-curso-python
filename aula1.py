#np1, np2, media, nota_final = 7, 8, 7.5, "APROVADO"
#estado = True
print("=====================================")
print()
print(f"Programa de cálculo de média")
print()
np1 = float(input("Digite a primeira nota: "))
np2 = float(input("Digite a segunda nota: "))
media = (np1 + np2)/2

#Utilizando a função type
"""As variaveis no Python não precisam ser do tipo declarado"""

"""#O type retorna o tipo do item declarado
print(type(np1)) #retorna inteiro baseado na linha 1
print(type(np2)) #retorna inteiro baseado na linha 1
print(type(media)) #retorna float baseado na linha 1
print(type(nota_final)) #retorna string baseado na linha 1
print(type(estado)) #retorna boolean baseado na linha 1"""

#O comando "isinstance" retorna se a sentença é verdadeira ou falsa

if media >= 7:
    estado = "APROVADO"
elif media <= 5:
    estado = "REPROVADO"
else:
    estado = "RECUPERAÇÃO"

if np1 % 2:
    imparPar = True
else:
    impaPar = False
    
if np2 % 2:
    imparPar = True
else:
    impaPar = False
    
    
print("====================================")
print()
print(f"A primeira nota do aluno foi: {np1}")
print(f"A segunda nota do aluno foi: {np2}")
print()
print(f"A média  do aluno foi: {media}")
print(f"O status do aluno é: {estado}")
print()
print("====================================")
print()
