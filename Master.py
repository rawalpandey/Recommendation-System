import pandas as pd
import csv
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import re

dataset=[]
with open('genre.csv','r') as csvfile:
	reader = csv.reader(csvfile,delimiter=',')
	for row in reader:
		dataset +=[row]
	#print dataset


#TRANSACTION ENCODING - encodes database transaction data in form of a python list
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df =pd.DataFrame(te_ary,columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.001,use_colnames=True)

#print frequent_itemsets[1:10]

from mlxtend.frequent_patterns import association_rules




rules = association_rules(frequent_itemsets,metric="lift",min_threshold=1.2)
rules["antecedent_len"]=rules["antecedents"].apply

nrules = rules[(rules['antecedent_len']>2) & (rules['confidence']>0.8) & (rules['lift']>1.2)]
#print nrules[1:10]

qrules=rules[['antecedents','consequents','confidence']]

'''
d = pd.DataFrame(rules[['antecedents','consequents','confidence']])
print d
d.to_csv("a.csv")'''
dataset2=[]
with open('list.csv','r') as csvfile:
	reader = csv.reader(csvfile,delimiter=',')
	for row in reader:
		dataset2 +=[row]
	#print dataset



#print qrules[1:50]

movig1=[]
songg1=[]
bookg1=[]

pregm=[]
pregs=[]
pregb=[]


songl=[]
movl=[]
bookl=[]

inpu = []
with open('input.txt','r') as csvfile:
	reader = csv.reader(csvfile,delimiter=',')
	for row in reader:
		inpu += [row]

print inpu


for i in inpu:
	for j in i:
		if(i.index(j)==0):
			for k in range(len(dataset2)):
				if(j==(dataset2[k][0])):	
					pregm.append(dataset2[k][1])

		elif(i.index(j)==1):
			for k in range(len(dataset2)):
				if(j==dataset2[k][5]):
					pregs.append(dataset2[k][4])
		else:
			for k in range(len(dataset2)):
				if(j==dataset2[k][10]):
					pregb.append(dataset2[k][12])
print pregm
print pregb
print pregs


movig = pregm[0]
songg = pregs[0]
bookg = pregb[0]
'''

movig=''
songg=''
bookg=''
		

movig = inpu[0][0]
songg = inpu[0][1]
bookg = inpu[0][2]



movig = raw_input("enter movie genre: ")
songg = raw_input("enter song genre: ")
bookg = raw_input("enter book genre: ")
pregm.append(movig)
pregs.append(songg)
pregb.append(bookg)
'''




dataset1=[]
with open('rules.csv','r') as csvfile:
	reader = csv.reader(csvfile,delimiter=',')
	for row in reader:
		dataset1 +=[row]
ass=[]
cons=[]
conf=[]
for i in range(len(dataset1)):
	ass.append(dataset1[i][1])
	cons.append(dataset1[i][2])


k=""
c1=0
g1=0
l1=''
c2=0
g2=0
l2=''
c3=0
g3=0
l3=''
for i in range(len(ass)):
	k=ass[i].strip()
	if(k==('m'+ movig)):
			if(c1!=3):
				
				l1=cons[i].strip()
				if(l1[1]=='m' and g1!=1):
					if l1[1:] not in pregm:
						pregm.append(l1[1:])
						g1=1
						c2=c2+1
				elif(l1[0]=='b' and g1!=2):
					if l1[1:] not in pregb:
						pregb.append(l1[1:])
						g1=2
						c1=c1+1
				elif(l1[0]=='s' and g1!=3):
					if l1[1:] not in pregs:
						pregs.append(l1[1:])
						g1=3
						c1=c1+1
			else:
				break
	elif(k==('s'+ songg)):
			if(c2!=3):
				
				l2=cons[i].strip()
				if(l2[0]=='m' and g2!=1):
					if l2[1:] not in pregm:
						pregm.append(l2[1:])
						g2=1
						c2=c2+1
				elif(l2[0]=='b' and g2!=2):
					if l2[1:] not in pregb:
						print l1[1:]
						pregb.append(l2[1:])
						g2=2
						c2=c2+1
				elif(l2[0]=='s' and g2!=3):
					if l2[1:] not in pregs:
						pregs.append(l2[1:])
						g2=3
						c2=c2+1
			else:
				break
	elif(k==('b'+ bookg)):
			if(c3!=3):
				
				l3=cons[i].strip()
				if(l3[0]=='m' and g3!=1):
					if l3[1:] not in pregm:
						pregm.append(l3[1:])
						g3=1
						c3=c3+1
				elif(l3[0]=='b' and g3!=2):
					if l3[1:] not in pregb:
						pregb.append(l3[1:])
						g3=2
						c3=c3+1
				elif(l3[0]=='s' and g3!=3):
					if l3[1:] not in pregs:
						pregs.append(l3[1:])
						g3=3
						c3=c3+1
			else:
				break
'''print pregs
print pregm
print pregb'''




print " Predicted genres: "
print "Prediction based on "
print " 1. Song genre Choice: ",pregs
print " 2. Book genre Choice: ",pregb
print " 3. Movie genre Choice: ",pregm



for i in pregm:
	c=0
	for j in range(len(dataset2)):
		if(c!=5):
			if(i==dataset2[j][1]):
				movl.append(dataset2[j][0])
				c=c+1
c=0
for i in pregb:
	c=0
	for j in range(len(dataset2)):
		if(c!=5):
			if(i==dataset2[j][12]):
				bookl.append(dataset2[j][10])
				c=c+1
c=0
for i in pregs:
	c=0
	for j in range(len(dataset2)):
		if(c!=5):
			if(i==dataset2[j][4]):
				songl.append(dataset2[j][5])
				c=c+1


'''
c=0
if(len(songl)==0):
	for j in range(len(dataset2)):
		if(c!=5):
			if(songg==dataset2[j][4]):
				songl.append(dataset2[j][5])
				c=c+1
c=0

if(len(movl)==0):
	for j in range(len(dataset2)):
		if(c!=5):
			if(movig==dataset2[j][1]):
				movl.append(dataset2[j][0])
				c=c+1
c=0
if(len(bookl)==0):
	for j in range(len(dataset2)):
		if(c!=5):
			if(i==dataset2[j][12]):
				bookl.append(dataset2[j][10])
				c=c+1'''






print "**********List of songs **********************"
#z=0
#z=len(songl)+len(movl)+len(bookl)
#g=1
for i in range(len(songl)):
	if(len(songl)!=0):
		print i+1 , ": " , songl[i]
print "*************List of Books*********************"
for i in range(len(bookl)):
	if(len(bookl)!=0):
		print i+1 , ": " , bookl[i]
print "*************List of movies**********************"
for i in range(len(movl)):
	if(len(movl)!=0):
		print i+1 , ": " , movl[i]
	
	
