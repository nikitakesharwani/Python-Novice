a=[2 , 4 , 5 , 1 ,3]
targetSum = 9
flag = False

for i in range(len(a) - 1):
    firstNum = a[i]
    # print(firstNum)
    for j in range(i+1 , len(a)):
        secondNum = a[j]
        if (firstNum + secondNum) == targetSum:
            print([firstNum , secondNum])
            flag = True

if flag == False:
    print([])