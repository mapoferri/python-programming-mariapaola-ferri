# For this exercise the pseudo-code is required (in this same file) 
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght 
# Use separate functions for the input and the output 
'''
pseudo-code:

-first of all, i am going to open and read the file;
-dividing the file in lines;
-getting all the lines that starts with '>';
-telling python to read this line and if it is doesn't find 'Homo sapiens', then to add it to a new file;
-in this file, with the records, i should print the source organism and the sequence lenght.

'''

#def parsing_fasta(fastafile):
fasta = open('sprot_prot.fasta', 'r')
new_fasta= open('new_fasta.txt', 'w')
l= fasta.readlines()
header=''
sequence=''
n = -1                  #an index number assign to every line in the sequence
for line in l:      #for every line in the file
	n += 1
	if line[0] == '>':  
		if 'Homo sapiens' not in line:
			line = header

	else:	
		sequence += line 

if header: 	
	result= header + '\n' + sequence
	new_fasta.write(result)




	


