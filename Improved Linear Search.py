array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

item = int(input("Enter the number to find: "))

found = False

for index, value in enumerate(array): #! Can also use range(len(array)) but enumerate provdes simplicity
    if item == value:
        found = True
        break

if found:
    print(f"Item Found at index: {index}")
else:
    print("Item not found")
