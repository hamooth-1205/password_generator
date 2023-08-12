# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 13:55:23 2023

@author: ELCOT
"""
def password(uc,lc,num,spl):
    pw=""
    for i in range(2):
        pw=pw+(random.choice(uc))
    for i in range(6):
        pw=pw+(random.choice(lc))
    for i in range(3):
        pw=pw+(random.choice(num))
    pw=pw+(random.choice(spl))
    l=list(pw)
    random.shuffle(l)
    return "".join(l)
import random
uc=[]
lc=[]
num=['1','2','3','4','5','6','7','8','9','0']
spl=["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]","|",":",";","'","<",",",">",".","?","/"]
pwl=[]
for i in range(65,91):
    uc.append(chr(i))
for i in range(97,123):
    lc.append(chr(i))
ps=password(uc,lc,num,spl)
if(ps not in pwl):
    pwl.append(ps)
    print(ps)
else:
    ps=password(uc, lc, num, spl)
