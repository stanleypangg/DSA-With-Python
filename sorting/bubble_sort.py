# Ascending
def bubble_sort(lst: list[int]) -> list[int]:
    n = len(lst)
    # Loop n times
    for i in range(n):
        swapped = False
        
        # Compare each adjacent pairs of elements
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        
        if not swapped:
            break
    
    return lst

# Descending
def bubble_sort_descending(lst: list[int]) -> list[int]:
    n = len(lst)
    for i in range(n):
        # End of list will be sorted
        # Only run as many iterations as needed
        for j in range(n - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    return lst