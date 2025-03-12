nome = str(input("Digite seu nome:")).upper()
sexo = str(input("Digite seu sexo:")).upper()
estado_civil = str(input("Digite seu estado civil:")).upper()
tempo_casada = int(input("Qual seu tempo de casada:"))
 
if sexo == "F"  and estado_civil == "CASADA":

 print(f"O nome do cliente é {nome} do {sexo} e {estado_civil} com {tempo_casada} de casada")
else:
 print(f"O nome do cliente é {nome} do {sexo} e {estado_civil}")