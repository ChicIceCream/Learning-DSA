my_list = [0,1,2,3,4,5,6]
upper_bound, lower_bound = my_list[5], my_list[0] #! Assinging upper and lower bounds
found = False

item = int(input("Enter a number: "))

for index in range(len(my_list)):
    index = int((upper_bound + lower_bound)//2)
    print(index)
    if item == my_list[index]:
        found = True
    
    if item > my_list[index]:
        lower_bound = index + 1
    
    if item < my_list[index]:
        upper_bound = index - 1
    
if found == True:
    print(f"Number is in te list, and at index : {my_list[item]}")
else: 
    print("Number does not exist.")