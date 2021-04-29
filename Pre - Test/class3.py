



# inp = input("Enter : ")
# inp = int(inp)
# for i in range(1,inp+1):
#     for j in range(1,inp+1):
 

# Python 3 code for hollow rectangle 
  
# Python 3 code for hollow squares 

# Function to print hollow square 
def print_square(n) : 
	numbers = '123456789ABCDEF'
	for i in range(1, n+1) : 
		for j in range(1, n+1) : 
			if (i == 1 or i == n or
				j == 1 or j == n) :			 
				print(numbers[i-1], end = "")			 
			else : 
				print("  ", end = "")			 
		
		print() 
		
		

# Driver code for above function 
rows = 10
print_square(rows) 

# This code is contributed by Nikita Tiwari. 
