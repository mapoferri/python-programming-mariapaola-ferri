seq1='ATTCG'
seq2='ATCGG'


#scores 
match=2
mismatch=-1
gap=-1


def SW(seq1, seq2, match, mismatch, gap):
    rows=len(seq1)+1
    columns=len(seq2)+1
    M = [[0 for col in range(columns)] for row in range(rows)]
    T = [['0' for col in range(columns)] for row in range(rows)]
    #initializing the matrix
    score_matrix[0][0]=0
    T[0][0]='0'
    for i in range(0, columns):
        score_matrix[0][i]=0
        T[0][i] = '0'
    for k in range(0,rows):
        score_matrix[k][0]=0
        T[k][0] = '0'
    #iterating the matrix
    max_score=0
    max_position= None
    for i in range(1,columns):
        for k in range(1,rows):
            if seq1[k-1] == seq2[i-1]:
                #computing all the scores
                #diag_score
                diag_score = score_matrix[k-1][i-1]+match
            else:
                diag_score = score_matrix[k-1][i-1]+mismatch
            left_score = score_matrix[k][i-1] + gap
            up_score = score_matrix[k-1][i] + gap
            
            scores=[diag_score, up_score, left_score, 0]
            
            if max(scores) > max_score:
                max_score = max(scores)
                max_position = (k, i)
            
            score_matrix[k][i] = max_score

            if max_score == diag_score: 
                T[k][i] = ('D')
            elif max_score == up_score:
                T[k][i] = ('U')
            elif max_score == left_score:
                T[k][i] == ('L')
        
            #considering the traceback now:
            
   
    max_row = max_position[0]
    max_column = max_position[1]
    
    s1=''
    s2=''
    while max_score != 0:
        diag_back = score_matrix[max_row-1][max_column-1]
        up_back = score_matrix[max_row-1][max_column]
        left_back = score_matrix[max_row][max_column-1]

        traceback = [diag_back, up_back, left_back]
        score = max(traceback)

        if score == diag_back:
            s1 += seq1[max_row-1]
            s2 += seq2[max_column-1]
            max_row = max_row-1
            max_column = max_column-1

        elif score == up_back:
            s1 += seq1[max_row-1]
            s2 += '-'
            max_row = max_row-1
        elif score == left_back:
            s1 += '-'
            s2 += seq2[max_column-1]
            max_column = max_column-1

        max_score = score
    print ('The highest score in the matrix is: %f' %score_matrix[max_row-1][max_column-1], 'and the cell in position: %s' %(max_position, ))
    return (T, score_matrix)

T, score_matrix = SW(seq1, seq2, match, mismatch, gap)
for i in T:
    print (i)
for i in score_matrix:
    print (i)



















'''          
            if max(scores) > max_score:
                max_score=max(scores)
                max_position=(k,i)
            matrix[k][i]=max(scores)
    #filled the matrix with the maximum values for each cell
    max_row=max_position[0]
    max_column=max_position[1]
    
    s1=''
    s2=''
    #tracebacking
    while max_score != 0:
        
        diag_back=matrix[max_row-1][max_column-1]
        up_back=matrix[max_row-1][max_column]
        left_back=matrix[max_row][max_column-1]
        
        traceback=[diag_back, up_back, left_back]
        traceback_score=max(traceback)

        if traceback_score == diag_back:
            s1 += seq1[max_row-1]
            s2 += seq2[max_column-1]
            max_row=max_row-1
            max_column=max_column-1
        elif traceback_score == left_back:
            s1+= '-'
            s2+= seq2[max_column-1]
            max_column = max_column-1
        elif traceback_score == up_back:
            s1+= seq1[max_row-1]
            s2+= '-'
            max_row=max_row-1
        
    traceback_score=max_score

    
    for lst in matrix:
        print (lst)



M=SW(seq1,seq2, match,mismatch,gap)
print()'''
