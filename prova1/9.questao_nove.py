renda_mensal = float(input("Digite sua renda mensal:"))
valor_total_emprestimo = renda_mensal * 10
prestacao = (renda_mensal * 30) / 100
numero_parcelas = prestacao / valor_total_emprestimo

 

if renda_mensal >= 759:

 print("Emprestimo concedido")
else:
 print("Emprestimo não concedido")


print(f"Renda mensal {renda_mensal}")
print(f" Valor total do emprestimo {valor_total_emprestimo}")
print(f"Valor da parcela {prestacao}")
print(f"numero de parcelas{numero_parcelas}") 
