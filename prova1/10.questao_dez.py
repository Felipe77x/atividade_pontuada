
litro_gasolina = float(input("Digite a quantidade de litros de gasolina:"))
litro_alcool = float(input("Digite a quantidade de litros de álcool:"))

gasolina_valor = 6.59
alcool_valor = 3.79
valor_pagar_gasolina = litro_gasolina * gasolina_valor
valor_pagar_alcool = litro_alcool * alcool_valor

if litro_gasolina == 25:
 valor_pagar_gasol = (valor_pagar_gasolina * 2) / 100
 print(f"Seu valor de desconto será: {valor_pagar_gasol:.2f}")
elif litro_gasolina > 25:
 valor_pagar_gasol = (valor_pagar_gasolina * 4) / 100
 print(f"Seu valor de desconto será: {valor_pagar_gasol:.2f}")
else:
 print("Opção invalida")

if litro_alcool == 25: 
 valor_pagar_alcooll = (valor_pagar_alcool * 3) / 100
 print(f"Seu valor de desconto será: {valor_pagar_alcooll:.2f}")
elif litro_alcool > 25: 
 valor_pagar_alcooll = (valor_pagar_alcool * 5) / 100
 print(f"Seu valor de desconto será: {valor_pagar_alcooll:.2f}")
else:
 print("opção invalida")
