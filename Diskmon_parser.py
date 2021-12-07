LBA=input('input LBA ')
LBA=int(LBA)
found=0
with open('Diskmon.Log','r') as f:
	for line in f:
		Monitor_Data=[]
		for word in line.split():
			Monitor_Data.append(word)		
		LBAStart=int(Monitor_Data[5])
		LBAEnd = LBAStart+int(Monitor_Data[6])
		if Monitor_Data[4]!='Write' and Monitor_Data[4]!='Read':
			print(Monitor_Data[4])
		if LBAStart <= LBA < LBAEnd:
			print(LBAStart , LBAEnd)
			hitline=int(Monitor_Data[0])
			print(Monitor_Data[4]+" LBA"+ str(LBA)+ " in " + str(hitline))
			found=1   	
			

if found==1:
	print("found in line "+ str(hitline))
else:
	print("no found")	









