password=None
attempts=[]
while password !="horseadd3.14159265359":
	password=input("what is the password")
	attempts.append(password)
	if password!= "horseadd3.14159265359":
		print("wrong password. account locked")
		for i in attempts:
			print(i)
print("correct")
