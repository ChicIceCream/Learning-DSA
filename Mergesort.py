arr = [1,2,6,4,8,9,5,3,2,3]

def mergesort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    l_half = arr[:mid]
    r_half = arr[mid:]
    l_half = mergesort(l_half)
    r_half = mergesort(r_half)  

    return merge(l_half, r_half)
def merge(left, right):
    new = []
    i,j = 0,0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    new.extend(left[i:])
    new.extend(right[j:])
    return new

mergedarr = mergesort(arr)
print(mergedarr)