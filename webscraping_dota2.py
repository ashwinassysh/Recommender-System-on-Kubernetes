#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:01:48 2019

@author: ashwinassyshsharma
"""

import pandas as pd
from bs4 import BeautifulSoup

with open('Hero.html') as f:
    soup = BeautifulSoup(f)
names = soup.find_all('table')

labels = []
data = []

for h in names[0].find_all('th'):
    labels.append(h.get_text().strip())

data_carry = []    
counter=0
for h in names[0].find_all('tbody'):
    for n in h.find_all('tr'):
        a = counter % 2
        if a == 0:
            counter += 1
            continue
        else:
            for i in n.find_all('td'):
                for g in i.find_all('a'):
                    data_carry.append(g.get('title'))
            counter+=1
            
# df1 = pd.DataFrame(list(zip(data_carry, data_nuker,data_initiator,data_durable,data_support)), 
#               columns = ['Carry', 'nuker','initiator','durable','support']) 

df1 = pd.DataFrame(data_carry, columns = ['Carry']) 
df2 = pd.DataFrame(data_nuker, columns = ['Nuker']) 
df3 = pd.DataFrame(data_initiator, columns = ['Initiator']) 
df4 = pd.DataFrame(data_disabler, columns = ['Disabler']) 
df5 = pd.DataFrame(data_durable, columns = ['Durable']) 
df6 = pd.DataFrame(data_escape, columns = ['Escape']) 
df7 = pd.DataFrame(data_support, columns = ['Support']) 
df8 = pd.DataFrame(data_pusher, columns = ['Pusher']) 
df9 = pd.DataFrame(data_jungler, columns = ['Jungler']) 


df1.to_csv('hero_carry.csv',index=False)
df2.to_csv('hero_nuker.csv',index=False)
df3.to_csv('hero_initiator.csv',index=False)
df4.to_csv('hero_disabler.csv',index=False)
df5.to_csv('hero_durable.csv',index=False)
df6.to_csv('hero_escape.csv',index=False)
df7.to_csv('hero_support.csv',index=False)
df8.to_csv('hero_pusher.csv',index=False)
df9.to_csv('hero_jungler.csv',index=False)
