nome = input("Digite o nome do produto:")
quantidade_adquirida = int(input("Quantidade adquirida:"))
preco_unitario = float(input("Preço unitario"))

total = quantidade_adquirida * preco_unitario

if quantidade_adquirida <= 5:
 desconto = (total * 2 )/ 100
 print(f"O valor {total:.2f - desconto}")
elif quantidade_adquirida > 5 and  10:
 desconto = (total * 3)/ 100
 print(f"O valor {total:.2f - desconto}")
elif quantidade_adquirida > 10:
 desconto =  (total * 5 )/ 100
 print(f"O valor {total:.2f - desconto}")
else:
  print("Opção invalida")