my_list = [0,1,2,3,4,5,6]
upper_bound, lower_bound = len(my_list) -1, 0 #! Assinging upper and lower bounds
found = False
print(upper_bound, lower_bound)
item = int(input("Enter a number: "))

# starting loop to check through every element
for index in enumerate(my_list):
    index = int((upper_bound + lower_bound)//2)
    
    # first condition that checks if the item is equal to the index
    if item == my_list[index]:
        found = True
        break # Add this line to exit the loop once the item is found
    
    # second condition that if the item is greater than index
    if item > my_list[index]:
        # if yes, then lowerbound becomes the index + 1
        lower_bound = index + 1
    
    # third condition that if the item is smaller than the item
    if item < my_list[index]:
        # if yes, then upperbound becomes index - 1
        upper_bound = index - 1

# If statement to answer whatever is needed with index
if found == True:
    print(f"Number is in te list, and at index : {my_list[item]}")
else: 
    print("Number does not exist in the list.")