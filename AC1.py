"""
Elabore um código em Python que resolva uma equação do segundo grau ax² + bx + c = 0. O programa deve ler os
 parâmetros a, b e c da equação e deve calcular as raízes pela fórmula de Bhaskara.
Considere que as raízes dadas pelo usuário são sempre reais, e os valores passados pelo usuário são sempre numéricos.
"""

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c

print("\n**************************\n")

if a == 0:
    print("O valor de a, deve ser diferente de 0")
elif delta < 0:
    print("Sem raízes reais")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("x1: {}, x2: {}".format(x1, x2))

    # x1 -0.75 , x2 -1.0   sendo a = 4 , b = 7 e c = 3

    """
    Elabore um programa em Python que leia uma variável inteira ano. Em seguida, exiba na tela o resultado da expressão lógica
    que indica se um ano é ou não bissexto. Um ano é bissexto se ele é múltiplo de quatro.
    No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos.
    Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.
    """

ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    if ano % 100 !=0:
        print(f'(ano) é bissexto.')
    elif ano % 400 == 00:
        print(f'(ano) é bissexto.')
    else:
        print(f'(ano) não é bissexto.')
else:
    print(f'(ano) não é bissexto.')


