mylist = [16, 19, 21, 27, 36, 42, 55, 67, 76, 89]
upperbound, lowerbound, found = len(mylist) - 1, 0, False
print(upperbound, lowerbound, found)

item = int(input("Enter your number to find from the list: "))

while lowerbound <= upperbound:
    index = (upperbound + lowerbound) // 2
    
    if item == mylist[index]:
        found = True
        break  # Add this line to exit the loop once the item is found
    elif item > mylist[index]:
        lowerbound = index + 1 
    else:
        upperbound = index - 1

if found:
    print(f"Found your number! It is at index {index}")
else: 
    print("Number not found in the list")
