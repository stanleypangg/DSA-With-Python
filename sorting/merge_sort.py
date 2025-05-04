"""
    1. Recursively list in half
    2. Recursively merge sort smaller arrays
"""

def merge_sort(lst: list[int]) -> list[int]:
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
    
def merge(lst1, lst2):
    merged_list = []
    
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
        
    merged_list.extend(lst1[i:])
    merged_list.extend(lst2[j:])
    
    return merged_list

print(merge_sort([2, 6, 2, 1, 7, 43, 2, 4]))