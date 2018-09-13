import random
import os
import sys
import math



"""total=0
count=0
while (True):
    inp=input('enter a number: ')
    if inp=="done": break
    value=float(inp)
    total = total + value
    count=count +1
average = total/count
print('average', average)"""


"""n=5
while n>0:
    print(n)
    n=n-1
print('blastoff!')"""




"""while True:
    line =input('>')
    if line == 'done':
        break
    print(line)
print('done')

coins=['1','5','10','15']
for coin in coins:
    print('du har: ', coin)"""


"""x = 30
if (x == 30):
    print('\nstämmer')
elif (x > 30):
    print('\nstämmer ej')
elif (x < 30):
    print('\nstämmer ej') """

"""x = 100
if x > 99:
    print('ditt köp är godkänt')
elif x < 100:
    print('ditt saldo är för litet')"""

"""x = 100
if x >= 100:
    print('du har fått VG')
elif x >= 50:
    print('grattis du klarade provet')
else:
    print('du har fått icke godkänt')"""

"""x = 1000
if x != 1000:
    print('du sköt för högt eller för lågt')
elif x == 1000:
    print('du prickade rätt, grattis!')"""
"""y=0
x = random.randrange(0, 101)
print(x)
while x != 20:
    y += 1
    x = random.randrange(0, 101)
    print("nummer", x,"efter", y, "slumpade försök")"""

"""x='hej'
y='då'
if x and y:
    print(x, y)"""

"""friends=['josh', 'molly','cat']
for friend in friends:
    line= input('enter name for their trait')
    if line=='cat':
        print('\ncat is a sillybilly')
    if line=='josh':
        print('\njosh is a poopyhead')
    elif line=='molly':
        print('\nmolly is a stinkyface')
    elif line=='done':
        print('YOU SUCK!')
        break"""
"""class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)


s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()

"""

age=int(input('För att kunna låna pengar av denna banken behöver du vara över 18 år gammal, hur gammal är du?:'))

if age < 18:
    print('Du är minderårig.')
if age >= 18:
    loan = int(input("Hur mycket vill du låna? 434kr-720kr eller 1000kr-1498kr."))
    if loan >= 434 and loan <= 720:
        print("Du måste betala:", loan * 1.063,'i ränta.')
    elif loan >= 1000 and loan <= 1498:
        print("Du måste betala:", loan * 1.03, 'i ränta.')
    else:
        print('du måste ange en summa mellan de angivna värdena för att kunna ta ett lån.')
