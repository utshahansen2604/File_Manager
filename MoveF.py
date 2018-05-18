import os
import shutil

src=''			#Source Path
dst=''			#Destination Path
exc=[""]			#Exclusion Files
os.chdir(src)
 
for i in os.listdir():
	if(i[len(i)-4]!="."):
		os.chdir(src+"\\"+i)
		for j in os.listdir():
			if((j in exc)):
				 print(j +" skipped!")
			else:	
				shutil.move(src+"\\"+i+"\\"+j,dst+"\\"+j)   
				print("Copied from "+src+"/"+i+"/"+j+" to "+dst+"/"+j+"\n")  