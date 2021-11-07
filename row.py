import pandas as pd
import csv
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

dataset=[]
k1=[]
l=[]
with open('list.csv','r') as csvfile:
	reader = csv.reader(csvfile,delimiter=',')
	for row in reader:
		dataset +=[row]
	#print dataset

for i in range(len(dataset)):
	k1.append(dataset[i][0])
#print k
bdchar1 =''
bdchar2 =''
c=''
f=k1[14]
for j in range(len(f)-7):
	if(j==0):
		bdchar1=f[j+7]
	if(j==1):
		bdchar2=f[j+7]
print bdchar1
print bdchar2


	

c=''
t=0
f=''
k=0
l=[]

for i in range(len(dataset)):
	f=k1[i].strip()
	for j in range(len(f)):
		#print f[j]
		if(f[j]!=" " ):
			if(f[j]==bdchar1):
				break
			else:
				c=c+f[j]
		if(f[j]==" "):
			if(ord(f[j+1])>64 and ord(f[j+1])<123):
				c= c+ " "
	l.append(c)
	c=""
	t=0
d=0
for i in l:
	print i,len(i)	
	d=d+1
f = open("a.txt","w+")
for i in l:
	f.write(i+"\n")
f.close
