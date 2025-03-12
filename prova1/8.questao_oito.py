cd = int(input("""Código \t 
1 \t Verde \t\t  
2 \t Azul \t\t
3 \t Amarelo \t\t 
4 \t Vermelho\t

                  
Digite a opção desejada:                  
                  """))

match cd:
 case 1:
  print("O valor é 10,00 reais.")
 case 2:
  print("O valor é 20,00 reais.")
 case 3:
  print("O valor é 30,00 reais.")
 case 4:
  print("O valor é 40,00 reais.")

print(cd)