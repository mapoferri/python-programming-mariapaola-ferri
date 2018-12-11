
#Exercise 1
#Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3

L=range(21,40)
even_numbers=[]
multiples=[]
for i in L:
	if i%2==0:
		even_numbers.append(i)
for i in L:
	if i%3==0:
		multiples.append(i)
	
print (even_numbers)
print (multiples)


# Exercise 2
# Print the last two elements of L 

print (L[-2:])     #starting from the position -2, i am printing all the elements until the end of the list


# Exercise 3
# What's wrong with the following piece of code? Fix it and modify the code in order to have it work AND to have "<i> is in the list" printed at least once


L = ['1', '2', '3']
for i in range(10): #the colon was missing
    if str(i) in L:   #
    	print(str(i)+'is in the list')   #it is expected a level of indentation and we want to print a string, so what we want to print it needs to be defined inside ''
    else:
   	 print(str(i)+ 'not found')         #it is expected a level of indentation and at the end we want to print a string, so it needs to be defined inside ''
    

# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element of the resulting list 



fastafile= open('sprot_prot.fasta','r')
reading_line= fastafile.readline()
print reading_line
half_string=reading_line.split('OS=')[-1:]  
#defining the splitted string by the separator, and printing everything that is after the separator until the last position of the string



# Exercise 5
# Split the second element of the list of Exercise 4 using blanks as separators, concatenate the first and the second elements and print the resulting string

resulting_string= str(half_string).strip('[]')     #eliminating the brackets from the previous list
resulting_string= resulting_string.split(' ') #splitting the resulting string
print (resulting_string[0] + resulting_string[1])



# Exercise 6
# reverse the string 'asor rosa'
string= 'asor rosa'
string[::-1]        #rewriting the string by starting from the last to the first position
print (string)





# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]
List=[1,7,3,9]
List.sort()
print (List)




# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L
List=[1,7,3,9]
L2=[]
for i in List:
	if i not in L2:        #if the element is not present in the new list, add it
		L2.append(i)
		L2.sort()     #sorting the new resulting list
print L2





# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6

f=open('tabella_file.txt','w')
f.write("2 \t4\n3 \t6")     #writing every element on the row separated by a tab, and then going to another line to print the next row





