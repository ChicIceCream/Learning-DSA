
mylist = [16, 19, 21, 27, 36, 42, 55, 67, 76, 89]
upperbound, lowerbound, found = len(mylist) - 1, 0, False
print(upperbound, lowerbound, found) # not required, just to make sure they are right

item = int(input("Enter your number to find from the list: "))


# starting loop to check through every element
  
while lowerbound <= upperbound:
    index = (upperbound + lowerbound) // 2
    
    # first condition that checks if the item is equal to the index
    if item == mylist[index]:
        found = True
        break  # Add this line to exit the loop once the item is found
    # second condition that if the item is greater than index
    elif item > mylist[index]:
        # if yes, then lowerbound becomes the index + 1
        lowerbound = index + 1 
    # third condition that if the item is smaller than the item
    else:
        # upperbound becomes index - 1
        upperbound = index - 1

# simple condition to check if the element is found
if found:
    print(f"Found your number! It is at index {index}")
else: 
    print("Number not found in the list")