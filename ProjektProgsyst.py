import os
import sys
import random
import math




class account(object): # detta är klassen som jag skapat, den kommer vi använda för att kunna kalla på de objekt inuti.
   def __init__(self,name): #detta är första objektet vi definierar
       self.name = name
       self.__balance = 0
   def deposit(self,amount):
       self.__balance += amount # summan av värdena blir det man väljer att lägga in på kontot adderat med start värdet som är 0
       print(amount,"deposited on",self.name)
   def withdraw(self,amount):
       if (self.__balance>amount):
           self.__balance -= amount # här räknar objektet ut summan genom att ta bort (dvs withdraw på engelska).
           print(amount,'has been withdrawn from',self.name)
       else:
           print('withdrawal exceeds account balance') #detta printas om det är så att användaren anger ett belopp som är högre än balansen på kontot.



accountname1 = input('whats your account name gonna be?: ') # här definierar vi en variabel vi senare ska använda
useraccount = account(accountname1) #

useraccount.deposit(10000) #i dessa koder kallar vi på klassen och de objekt vi skapade tidigare för att räkna ut vad som kommer att hamna på kontot.
useraccount.withdraw(400)
useraccount.withdraw(300)
useraccount.deposit(1000)
useraccount.balance=11000-700
print(useraccount.balance,'dollars on',accountname1,'account') # här kallar vi på de objekt och variabler för att printa ut värdet på kontot och namnet som användaren anger.


