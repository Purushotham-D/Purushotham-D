# #1
# n=5
# while n>0:
# 	 print(n)                #observe indentation 
# 	 n=n-1 
# print("Blast off!") 

# #2
# n=1 
# while True: 
# 	print(n)
# 	n=n+1 
# 	break
# 	print("a")
#3

sum=0 
count=0 
while True:     
	x=input("Enter a number:")     
	if x%2!=0:         
		continue      
	else:         
		sum+=x          
		count+=1     
		if count==5:          
			break 
print("Sum= ", sum) 