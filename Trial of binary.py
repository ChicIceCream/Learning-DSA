mylist = [16, 19, 21, 27, 36, 42, 55, 67, 76, 89]
upperbound, lowerbound = mylist[-1], mylist[0]
print(upperbound, lowerbound)

item = int(input("Enter a number : "))
index = ((upperbound + lowerbound)/2)
found = False

for index in range(len(mylist)):
    if item == mylist[index]:
        found = True
    
    if item > mylist[index]:
        lowerbound = index + 1
    
    if item < mylist[index]:
        upperbound = index - 1
    
if found == True:
    print("Number found!")
else:
    print("Number not found!")