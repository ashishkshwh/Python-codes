# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 01:19:33 2015

@author: Ashish

Code for Hangman
"""

def find_letter(a,b):
    check = False
    for i in a:
        if i==b:
            check = True
    return check

def letter_replace(x_list,y_list,r):
    for i in range(0,len(x_list)):
        if (x_list[i]==r):
            y_list[i]=r
    return y_list
    
'''The real code starts'''

frame = [" __\r","   |\r","   |\r","   |\r","   |\r","   |\r","------"]
misses = [" __\r"," | |\r"," O |\r"," | |\r","/| |\r","/|\|\r"," | |\r",
"/  |\r","/ \|\r","------"]

x = 'ashishkushwaha' #Known string
x_letters = list(x) #list of known string letters
right_guess = list('_'*len(x)) #it's a list of blanks

missed_guess = "" #wrong guesses
print '==========================================='
print 'Missed: 0'+",".join(list(missed_guess))
print 'Guessed: '+' '.join(right_guess)
print "".join(frame)

attempt = 0
row = 0

while (find_letter(right_guess,'_') and (attempt<8)):
    print '==========================================='
    r = raw_input("Your guess?: ")
    if find_letter(x,r):
        right_guess = letter_replace(x,right_guess,r) #it's a list
    else:
        missed_guess = missed_guess + r
        attempt = attempt + 1
        row = row+1
        if ((attempt==3)or(attempt==4)or(attempt==5)):
            row = 3
        elif ((attempt==7)or(attempt==8)):
            row = 5
        frame[row]=misses[attempt]
        
    print '==========================================='
    if missed_guess=="":
        print 'Missed: 0'+",".join(list(missed_guess))
    else:
        print 'Missed: '+",".join(list(missed_guess))
    print 'Guessed: '+' '.join(right_guess)
    print "".join(frame)


if (attempt==8):
    print 'You killed him!'
else:
    print 'Good job!'