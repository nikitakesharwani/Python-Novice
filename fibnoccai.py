n = int(input('Enter Number- '))
prevNum = 0
nextNum = 1

for i in range (1 , n):
   newNum = prevNum + nextNum
   prevNum = nextNum
   nextNum = newNum
   
print(prevNum)