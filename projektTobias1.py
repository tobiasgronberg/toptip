import os
import sys
import random
import math






balance=0
print('welcome to Tobias Official Bank System!\n')


try:
    while True:
        print("""\n--- Main menu ----
-----------------------------
1: New account
2: Deposit
3: Withdraw
4: Check your current balance
5: Exit
-----------------------------
        """)
        answer=int(input('Please select your choice from the menu: '))

        if answer==1:
            answer_1=float(input('\nDeposit your new account balance within our bank: '))
            balance += answer_1
        elif answer==2:
            answer_2=float(input('\nHow much would you like to deposit: '))
            balance += answer_2
        elif answer==3:
            answer_3=float(input('\nHow much would you like to withdraw: '))
            balance -= answer_3
        elif answer==4:
            print('\n',balance,' $ on your account')
        elif answer==5:
            print('\nGood bye and thank you for using our banking system!')
            exit()
        elif answer<5 or answer>0:
            print('\nTry again with different menu number!')


except ValueError:
    print('you need to input a valid number from the menu to advance!')


