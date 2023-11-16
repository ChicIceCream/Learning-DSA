import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage for the first implementation
my_list1 = [64, 34, 25, 12, 22, 11, 90]

start_time = time.perf_counter()
bubble_sort(my_list1)
end_time = time.perf_counter()

print("Sorted array (Implementation 1):", my_list1)
print("Time taken: {:.6f} seconds".format(end_time - start_time))


# Example usage for the second implementation
my_list2 = [70, 46, 43, 27, 57, 41, 45, 21, 14]

start_time = time.perf_counter()
top = len(my_list2)
swap = True
while swap or (top > 0):
    swap = False
    for index in range(top - 1):
        if my_list2[index] > my_list2[index + 1]:
            temp = my_list2[index]
            my_list2[index] = my_list2[index + 1]
            my_list2[index + 1] = temp
            swap = True
    top = top - 1
end_time = time.perf_counter()

print("Sorted array (Implementation 2):", my_list2)
print("Time taken: {:.6f} seconds".format(end_time - start_time))

start_time = time.perf_counter()
my_list3 = sorted(my_list2)
end_time = time.perf_counter()
print("Time taken: {:.6f} seconds".format(end_time - start_time))