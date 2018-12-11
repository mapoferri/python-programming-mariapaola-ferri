#I am inserting from the keyboard every component of my vector, and it is written without brackets: 
vector=[]
def vectors(vector):
	for number in range(0,11):
		number= input('Write here the vector by its components:').split(',')
		vector.append(number)
	print (vector)     #printing the vector
	print (len(vector))

def average_function(vector):
	summing = sum(int(components) for components in vector)
	#for every component of the vector, I am summing them all together, since with the function int() they are considered as numbers, even if first they were recognized as strings
	average= summing/len(vector) 
	print (float(average))     
	
