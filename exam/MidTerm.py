 
file = open('insulin.gbk', 'r')
i=0
lines = file.readline().split()
accession = '>'
accession += lines[1]
next_line = file.readline().split()
accession +=('|' +  next_line[1]+ ' '+ next_line[2])
genfile =  file.readline().split()
digit = [0,1,2,3,4,5,6,7,8,9]
for line in file.readline():
    if len(line) >0 and line[0].isdigit(): 
        print line[1:]
        print accession

        







    


    


