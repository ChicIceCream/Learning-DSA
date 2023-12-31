# Bubble Sort using while loop and using swap comments

myList = [70,46,43,27,57,41,45,21,14]
print(myList)
top = len(myList)
swap = True

# using while loop so until the array or list is sorted, the for loop will keep sorting
while (swap) or (top > 0):  
    swap = False
    for index in range(top - 1):
        if myList[index] > myList[index + 1]:
            temp = myList[index]
            myList[index] = myList[index + 1]
            myList[index + 1] = temp
            swap = True
    top = top - 1

#output the sorted array
print("This is the sorted array : ", myList)
