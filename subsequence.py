# Weather a list is a subsequence of a list or not
array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,8]

sequenceIdx = 0
for item in array:
        if item == sequence[sequenceIdx]:
            sequenceIdx+=1
        
        if sequenceIdx == len(sequence):
            print(True)
            break
if sequenceIdx != len(sequence):
     print(False)


        
        
         
