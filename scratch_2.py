import os
import sys
import random
import math
"""
myList =[['portable', 12.3], [199,'nackademin']]


#print(3*'\n'+str(myList),3*'\n')

for r in range(len(myList)):
    for k in range(2):
        print(myList[r][k], end=' ')
    print('\n')

oneliner = '    Tobias Grönberg'

strings = '''

    ort: solna
    skola: nackademin
    utbildning:  yrkeshögskola
    '''
print(oneliner + strings)


x=10
y=1

if (x>y) and (x==10) and (y!=x) or print('this is false'):
    print('this is true')
"""

"""x=9


while x!=25:
    x+=1
    print(x)
    if x==25:
        print('du har nått 25')"""

"""age=int(input('hur gammal är du?'))"""
"""
x=1000
y=40
z=40-1000

print(z*100,'%')


x=1000
y=40
print(x*(y/100))
"""

"""age=int(input('hur gammal är du?'))
if age <= 18:
    print('du har inte uppnått myndig ålder!')"""


#ränkte-kalkylator
"""

age=int(input('För att kunna låna pengar av denna banken behöver du vara över 18 år gammal, hur gammal är du?:'))

if age < 18:
    print('Du är minderårig.')
if age >= 18:
    loan = int(input("Hur mycket vill du låna? ange ett värde mellan 434kr-720kr eller 1000kr-1498kr:"))
    if loan >= 434 and loan <= 720:
        print("Du måste betala:", loan * 1.063,'kronor i ränta.')
    elif loan >= 1000 and loan <= 1498:
        print("Du måste betala:", loan * 1.03, 'kronor i ränta.')
    else:
        print('du måste ange en summa mellan de angivna värdena för att kunna ta ett lån.')

"""


#if-elif statement

"""age=int(input('hur gammal är du?:'))
if age <= 2:
    print('du får ha födelsedagskalas!')
elif age >=16:
    print('du är för gammal för att ha kalas!')
elif age >2 and age <=16:
    print('du får bestämma själv om du vill ha kalas')"""

"""age=int(input('hur gammal är du?'))

#or statement

if age>=1 or age<17:
    print('du är minderårig')
elif age>18 or age<64:
    print('du är vuxen')
else:
    print('du är pensionerad')"""

#sträng hantering; konkatenering, formatering och decimaltals formation i, på och av strängar.

"""x='nackademin'
y='solna'
c='yrkeshögskola'
t='H'
u='e'
i='j'
o='vi önskar dig lycka till under skolgången!'
r=92.501314124124124132312312314214123123
k='procents chans att anställas'
a='våra elever har'
print( '\ndu går på; %s i %s som är en %s'%(x,y,c))
print('\n%c%c%c, %s %.2f %s, %s'%(t,u,i,a,r,k,o))"""


#oneliners sortering av strängar och strängbyggande.

"""print(sorted("%c%c%c%c%c%c%c%c"%('c','o','m','p','u','t','e','r')))

print(sorted("%s"%(input("vad vill du sortera?"))))

#true/false koll om strängen slutar eller börjar på en viss char.

x="computer".startswith("e")
print(x)
x="computer".endswith("r")
print(x)"""


#konfirmering av information innuti strängar; ger tillbaka ett true/false message.

c="nackademin"
print("nacka" in c)




