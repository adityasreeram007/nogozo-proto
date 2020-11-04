import csv
import random as rand
areas=["Adayar","velachery","kodambakkam","sholinganallur","Nungambakkam","Rk Puram","Nungambakkam","Royepetta","Ponamalle"]
c=600021
dict1={}
for x in areas:
    dict1[x]=c
    c+=rand.randint()%10+1
shops=["walmart store","heritage",'fresh','nilgiris','ck selvam','himalayas','Amazon Storex','webuy','poorvika','mega mart','big bazaar','relience digital','reliance fresh']
with open('shopdata.csv','w') as file:
    writer=csv.writer(file)
    for i in range(0,len(len(areas))):
        for j in range