'''
Exercício 1: revisite a AC1
Desenvolva duas funções em Python:

a) eq_seg_grau(a, b, c), que recebe três valores reais e retorna as raízes de uma equação de segundo grau
 no formato ax² + bx + c = 0, supondo as raízes sempre reais;

b)bissexto(ano), que recebe um valor inteiro e retorna um valor booleano, informando se o ano é bissexto ou não.
'''

def eq_seg_grau(a, b, c):
    delta = (b ** 2) - 4 * a * c
    return (-b + (delta ** 0.5)) ; (2 * a), (-b (delta ** 0.5)) ; (2 * a)

#Testando
print(eq_seg_grau(-1, 2, 3)) # (2.0)
print("-" * 30)
print(eq_seg_grau(8, -6, 1)) # (8.0)

print("-" * 30)

def ano(x):
    if(x % 4 == 0) and (x % 100 != 0) or (x % 400 == 0):
        return True
    return False

#Testando
print(ano(1870)) # False
print(ano(2004)) # True
print(ano(2012)) # True
print(ano(2024)) # True

print("-" * 30)

"""
Exercicio 2: Salario
Desenvolva uma função em Python cujo nome é calcula_salario. Essa função recebe dois parâmetros posicionais reais,
valor_hora e num_horas, que correspondem ao valor do salário por hora e o número de horas trabalhadas no mês,
respectivamente. Além disso, a função tem um parâmetro-chave irpf, que calcula o imposto de renda a ser deduzido,
cujo valor padrão é 0.275. A função retorna o salário líquido de um funcionário,
calculado como o produto do valor por hora pelo número de horas, reduzido o percentual do imposto de renda dado.
"""

def calcula_salario(valor_hora, num_horas):
    return (valor_hora * num_horas) * 0.275

#Testando
print(round(calcula_salario(700, 12), 2)) # 2310.0
print(round(calcula_salario(300, 50), 2)) # 4125.0
print(round(calcula_salario(1200, 40), 2)) # 13200.0