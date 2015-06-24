# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:47:30 2015

@author: Ashish

To convert a piece of text into a made-up language with predefined roots.
"""

def word_trans(word):
    if word=="":
        return ""
    else:
        prefix = ""
        stem_count=0
        for i in word:
            if (i=='a')or(i=='e')or(i=='i')or(i=='o')or(i=='u')or(i=='y'):
                break
            elif (i=='A')or(i=='E')or(i=='I')or(i=='O')or(i=='U')or(i=='Y'):
                break
            else:
                prefix = prefix+i
                stem_count = stem_count+1
        
        stem = word[stem_count::]

        if (ord(word[0])>=65) and (ord(word[0])<=90):
            if prefix=="":
                prefix=""
            else:    
                prefix_list = list(prefix)
                prefix_list[0]=chr(ord(prefix_list[0])+32)    
                prefix = "".join(prefix_list)
                stem_list = list(stem)
                stem_list[0]=chr(ord(stem_list[0])-32)
                stem = "".join(stem_list)
                            
        if prefix=="":
            final_word = stem+"yay"
        else:
            final_word = stem+prefix+"ay"
                                    
    return final_word

sentence = raw_input('Enter the text: ')
word=""
trans_string = ""
for letter in sentence:
    if (ord(letter)>=65 and ord(letter)<=90):
        word = word + letter
    elif (ord(letter)>=97 and ord(letter)<=122):
        word = word + letter
    else:
        trans_string = trans_string + word_trans(word) + letter
        word=""

if word=="":
    word=""
else:
    trans_string = trans_string + word_trans(word)

print trans_string        