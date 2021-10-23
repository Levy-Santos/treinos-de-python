# coding=utf-8
# ex 11 :
"""l = float(input('qual a largura da parede? '))
h = float(input('qual a altura da parede? '))
area = l*h
tinta = area/2
print(f'sua parede tem as dimeções de {l} x {h} e sua area é de {area:.3f}m².')
print(f'para pintar essa parede você precisará de {tinta:.2f}L de tinta.')"""
# ex 12 :
"""p = float(input('qual o preço do produto: '))
d = p-(5/100 * p)
print(f'O produto que custava R${p:.2f}, na promoção com desconto de 5% custará R${d:.2f}.')"""
# ex 13 :
"""s = float(input('qual o salario do funcionario: '))
a = s + (s*15/100)
print(f'Um funcionario que ganhava R${s:.2f}, com um aumento de 15%, passa a receber {a:.2f}.')"""
# ex 14 :
"""t = float(input('qual a temperatura em °C: '))
F = (t*9/5) + 32
print(f'A temperatura de {t}°C corresponde à {F}°F.')"""
# ex 15 :
"""d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
p = (d*60)+(km*0.15)
print(f'O total à pagar é de R${p}.')"""
# ex 16 :
'''n = float(input('Digite um valor: '))
print(f'o valor digitado foi {n} e sua porção inteira é {n:.0f}.')'''
# ex 17 :
'''from math import hypot
co = float(input('qual é o cateto oposto? '))
ca = float(input('qual é o cateto adjacente? '))
h = hypot(co, ca)
print(f'a hipotenusa vai medir {h:.2f}')'''
# ex 18 :
'''import math
a = float(input('digite o angulo que deseja?'))
r = math.radians(a)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print('se o angulo for {} \n'
      'o seno será {:.3f} \n'
      'o coseno será {:.3f} \n'
      ' e a tangente será {:.3f}'.format(a, s, c, t))'''
# ex 19 :
'''from random import choice
a1 = str(input('digite o nome do primeiro aluno: '))
a2 = str(input('digite o nome do segundo aluno: '))
a3 = str(input('digite o nome do terceiro aluno: '))
a4 = str(input('digite o nome do quarto aluno: '))
s = [a1, a2, a3, a4]
print(f'O aluno sorteado foi {choice(s)}.')'''
# ex 20 :
'''from random import shuffle
a1 = str(input('digite o nome do primeiro aluno: '))
a2 = str(input('digite o nome do segundo aluno: '))
a3 = str(input('digite o nome do terceiro aluno: '))
a4 = str(input('digite o nome do quarto aluno: '))
s = [a1, a2, a3, a4]
shuffle(s)
print(f'a ordem de apresentação será')
print(s)'''