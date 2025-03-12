gasolina_valor = 6,59
alcool_valor = 3,79

litro_gasolina = float(input("Digite a quantidade de litros de gasolina:"))
litro_alcool = float(input("Digite a quantidade de litros de álcool:"))

valor_pagar_gasolina = litro_gasolina * gasolina_valor
valor_pagar_alcool = litro_alcool * alcool_valor

if litro_gasolina == 25:
 valor_pagar = (valor_pagar_gasolina * 2) / 100
 print(valor_pagar)
elif litro_gasolina > 25:
 valor_pagar = (valor_pagar_gasolina * 4) / 100
 print(valor_pagar)
elif litro_alcool == 25: 
 valor_pagar = (valor_pagar_alcool * 3) / 100
 print(valor_pagar)
elif litro_alcool > 25: 
 valor_pagar = (valor_pagar_alcool * 5) / 100
 print(valor_pagar)
else:
 print("opção invalida")
