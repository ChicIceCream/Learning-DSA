array = [1,2,3,4,5,6,7,8,9]
upper_bound, lower_bound = len(array) -1, 0
print(upper_bound, lower_bound)

item = int(input("Enter the number to find : "))
print(item)

found = False

index = lower_bound

if found == False:
    for index in range(len(array[:])):
        if item == array[index]:
            found = True
        
if found:
    print(f"Item Found, it is as index : {array[item]}")
else:
    print("Item not found")
        

    