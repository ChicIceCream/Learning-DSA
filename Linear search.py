# Easy array to understand how linear search works

array = [1,2,3,4,5,6,7,8,9]
upper_bound, lower_bound = len(array) -1, 0
print(upper_bound, lower_bound)

item = int(input("Enter the number to find : "))
# print(item) to check if the it is correct, not needed

# Assigning values
found = False

index = lower_bound

# Starting if statement
if found == False:
    for index in range(len(array[:])): # this cannot be written as enumerate(array[]), because it is a list
        if item == array[index]:
            found = True

# If statement to answer whatever is needed with index
if found:
    print(f"Item Found, it is as index : {array[item]}")
else:
    print("Item not found")