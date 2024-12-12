import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

##### R:
# try:
#     n1 = int(input("Digite o primeiro número: "))
#     n2 = int(input("Digite o segundo número: "))
#     print(f"A soma dos valores é: {n1 + n2}")
# except:
#     print("Um dos valores digitados não é um número inteiro (1,2,3,4...) ou contém letras")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

##### R:
# try:
#     n1 = float(input("Número: "))
#     print(f"{n1 % 5}")
# except:
#     print("Algo deu errado... :/")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

##### R:
# try:
#      n1 = int(input("Digite o primeiro número: "))
#      n2 = int(input("Digite o segundo número: "))
#      print(f"{n1 * n2}")
#      print(f"{n1 ** n2}")
# except:
#      print("Algo deu errado... :/")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

##### R:
# try:
#     n1 = int(input("Digite o primeiro número: "))
#     n2 = int(input("Digite o segundo número: "))
#     print(f"{int(n1/n2)}")
# except:
#     print("Algo deu errado... :/")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

##### R:
# try:
#     n1 = int(input(""))
#     print(f"{n1**2}")
# except:
#     print("Algo deu errado... :/")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

##### R:
# try:
#     n1 = float(input(""))
#     n2 = float(input(""))
#     print(f"{n1+n2}")
# except:
#     print("Algo deu errado... :/")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

##### R:
# try:
#     n1 = float(input(""))
#     n2 = float(input(""))
#     print(f"{(n1+n2)/2}")
# except:
#     print("Algo deu errado... :/")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

##### R:
# try:
#     n1 = float(input(""))
#     n2 = float(input(""))
#     print(f"{(n1**n2)}")
# except:
#     print("Algo deu errado... :/")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

##### R:
# try:
#     celcius = int(input(" "))
#     print(f"{(celcius * 1.8)+32}"),
# except:
#     print("Algo deu errado... :/")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

##### R:
# try:
#     r = int(input("Digite o raio: "))
#     print(f"A área do círculo é: {math.pi * (r**2):.2f}")
# except:
#     print("Algo deu errado... :/")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

##### R:
# try:
#     t = input("Texto: ").upper()
#     print(t)
# except:
#     print("Algo deu errado... :/")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

##### R:
# try:
#     t = input("Nome: ").upper()
#     print(t)
# except:
#     print("Algo deu errado... :/")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

##### R:
# try:
#     t = input("Digite uma fase: ").strip()
#     print(t)
# except:
#     print("Algo deu errado... :/") 

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

##### R:
# try:
#     data = input("Digite a data no formato dd/mm/yyyy: ").split("/")
#     print(f"O dia informado foi {data[0]}, mês {data[1]} e ano {data[2]}")
# except:
#     print("Algo deu errado... :/") 

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

##### R:
# try:
#     st1 = input("1: ")
#     st2 = input("2: ")
#     st3 = st1 + " " + st2
#     print(st3)
# except:
#     print("Algo deu errado... :/") 

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

##### R:
# try:
#      v1 = True
#      v2 = False
#      v3 = v1 and v2
#      print(f"Valores: {v3}")
# except:
#     print("Algo deu errado... :/") 


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

##### R:
# try:
#      v1 = True
#      v2 = False
#      v3 = v1 or v2
#      print(f"Valores: {v3}")
# except:
#     print("Algo deu errado... :/") 
    
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

##### R:
# try:
#     v1 = bool(input(""))
#     if v1 == True:
#         print("False") 
#     else:
#         print("True")
# except:
#     print("Algo deu errado... :/")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

##### R:
# try:
#     n1 = int(input(""))
#     n2 = int(input(""))
#     if n1 == n2:
#         print("São enguais")
#     else:
#         print("Não são enguais")
# except:
#     print("Algo deu errado... :/")



# #### try-except e if

# 21: Conversor de Temperatura

##### R:

# 22: Verificador de Palíndromo

# try:
#     p = '233234'
#     if p == p[::-1]:
#         print("É um palindromo")
#     else:
#         print("Nâo é um palindromo")
# except:
#     print("Algo deu errado... :/")

# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação