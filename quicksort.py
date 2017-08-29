def quicksort(whatever):
    if len(whatever) <= 1:
        return whatever
    pivot = whatever[len(whatever) // 2]                // Pivot = The data arranged within a list is divided and round up by 2 //
    left = [x for x in whatever if x < pivot]           
    middle = [x for x in whatever if x == pivot]
    right = [x for x in whatever if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))

