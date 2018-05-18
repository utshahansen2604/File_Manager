import urllib, os, sys
import requests
from bs4 import BeautifulSoup

title="" 												#Title of the TV Series

dst1="" 								 				#Link to Home folder
dst2=""											 		#Link to Season folder

URL ="http://epguides.com/"+"" 							#Link to Episode TV Guide

textfile=title+"_Episodes.txt"  						#Name of the text file
first_epi="" 											#Name of the first episode
file_sample="" 											#Name of naming sample
stopper=[10,20]											#Episode numbers of Season Finale

r = requests.get(URL)

os.chdir(dst2)
final_epi=[]

def epi_scrape():   									#Generate Episode list
	soup = BeautifulSoup(r.content, 'lxml')
	text1=(soup.find_all("a"))
	lines = [a.get_text() for a in text1]
	os.chdir(dst1)
	f=open(textfile,"w+")
	
	
	k=0
	s=1
	e=1
	count=1
	flag=0
	print("\nXXXXXXXXXX Episodes List XXXXXXXXXX\n")
	for i in lines:
		if i==first_epi:
			flag=1	
		if i=="Back toTOP":
			flag=0

		if e>=10:
			E=""
		else:
			E="0"
		if s>=10:
			S=""
		else:
			S="0"	

		#print("S"+S+str(s)+"E"+E+str(e)+" "+i+"\n")
		if flag==1 and i!="":
			print(title+" "+S+str(s)+"E"+E+str(e)+" "+i)
			f.write("S"+S+str(s)+"E"+E+str(e)+" "+i+"\n")
			final_epi.append("S"+S+str(s)+"E"+E+str(e)+" "+i)
		
			if(count==stopper[k]):
				k=k+1
				s=s+1
				e=1
				count=count+1
			else:
				count=count+1
				e=e+1	
	f.close()

epi_scrape()

#print(final_epi)
s1=0
s2=0
e1=0
e2=0

os.chdir(dst2)
x=os.listdir()
print("\nXXXXXXXXXX Files List XXXXXXXXXX \n") 								#Generate File list
for i in x:
	print(i)


for i in range(0,len(file_sample)): 			   							#Fetching the episode indices
	if file_sample[i:i+2]=='S0':
	    #print(str(i)+""+str(i+2)+""+str(i+4)+""+str(i+5))
		s1=(i+1)
		s2=(i+3)
		e1=(i+4)
		e2=(i+6)

print(file_sample[s1:s2]+" "+file_sample[e1:e2])
print(str(s1)+" "+str(s2)+ " "+str(e1)+" "+str(e2))



epi_guide=os.listdir()

print("\nXXXXXXXXXX Enter File Extensions: XXXXXXXXXX \n")					#Input the file extension

exts=str(input()).split(" ")

for ext in exts:
	for i in epi_guide:
		if i.endswith("."+ext)==True:
			#print(i[0]+" "+i[2:4])
			s=i[s1:s2]
			e=i[e1:e2]
			#print(s+" "+e)
			for j in final_epi:
				#print(j[1:3]+" "+j[4:6])
				if s==j[1:3] and e==j[4:6]:
					os.rename(i,title+" "+j+"."+ext)						#Renaming the files
					print(title+" "+j+"."+ext+" renamed!")


