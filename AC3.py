"""
Exercício 1: triângulos
Desenvolva uma função determina_tipo_triangulo que recebe três lados de um triângulo e retorna uma string, 
"Escaleno", "Isósceles" ou "Equilátero", conforme o tipo do triângulo.
 A função deve retornar "Não é um triângulo" se os três lados não formarem um triângulo. Use a função abaixo como teste:
 """

def determina_tipo_triangulo(lado1, lado2, lado3):
      if(lado1) != (lado2) != (lado3):
            return "Escaleno"
      if (lado1) == (lado2) != (lado3) or (lado1) != (lado2) == (lado3) or (lado1) == (lado3) != (lado2):
            return "Isósceles"
      if (lado1) == (lado2) == (lado3):
            return "Equilátero"
      
#Teste
      print(determina_tipo_triangulo(3, 5, 2)) # Escaleno
      print(determina_tipo_triangulo(7, 7, 2)) # Isósceles
      print(determina_tipo_triangulo(5, 5, 5)) # Equilátero

"""
Desenvolva uma função dia_semana que recebe um número inteiro e retorna uma string indicando o dia da semana equivalente,
considerando que o dia da semana igual a 1 é o domingo, 2 é segunda-feira, etc.
 A função deve retornar uma string vazia caso o número seja inválido. Use a função abaixo como teste:
"""   

def dia_semana(dia):
      if (dia) == "1":
            return "Domingo"
      if (dia) == "2":
            return "Segunda-Feira"
      if (dia) == "3":
            return "Terça-Feira"
      if (dia) == "4":
            return "Quarta-Feira"
      if (dia) == "5":
            return "Quinta-Feira"
      if (dia) == "6":
            return "Sexta-Feira"
      if (dia) == "7":
            return "Sábado"
    
#Teste
      print(dia_semana("1")) # Domingo
      print(dia_semana("2")) # Segunda-Feira
      print(dia_semana("3")) # Terça-Feira
      print(dia_semana("4")) # Quarta-Feira
      print(dia_semana("5")) # Quinta-Feira
      print(dia_semana("6")) # Sexta-Feira
      print(dia_semana("7")) # Sábado
      print(dia_semana("9")) # str vazia(none)

"""
Desenvolva funções de operações aritméticas soma, subtracao, multiplicacao e divisao,
que recebem dois números cada uma e retornam o resultado da operação indicada. 
Em seguida, crie uma função que elabora uma interface por linha de comando (CLI), que lê dois números e uma operação e 
exibe na tela o valor do resultado, ou exibe "operação inválida" se o usuário inserir uma mensagem diferente das quatro operações.
"""

def soma (a, b):
      return a + b

def multiplicacao(a, b):
      return a * b

def subtracao(a, b):
      return a - b

def divisao(a, b):
      return a / b

def cli():
      a = float(input("1º número"))
      b = float(input("2º número"))
      x = input("Escolha a operação")
      if  x == "soma":
            resultado = a + b
            print("O resultado da soma é:", resultado)
      if x == "subtracao":
            resultado = a - b
            print("O resultado da subtração é:", resultado)
      if x == "multiplicacao": 
            resultado = a * b
            print("O resultado da multiplicação é:", resultado)
      if x == "divisao":
            resultado = a / b 
            print("O resultado da divisão é:", resultado)
      else:
            print("Operação inválida!")

cli()

#Teste 
a = input('Entre com valor de a:')
b = input('Entre com valor de b:')
x = input('Entre com a operação desejada:')
