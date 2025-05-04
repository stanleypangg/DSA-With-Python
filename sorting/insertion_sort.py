"""
    1. Start from left to right
    2. On each iteration, keep left sorted partition and right unsorted partition
    3. Sorted partition grows one each iteration
    4. Compare last element of sorted partition with first element of unsorted
    5. If not in order, insert first element of unsorted in sorted partition in ascending order
    6. If in order, sorted partition is already sorted
    7. Time: O(n^2), Space: O(1)
"""

def insertion_sort(lst: list[int]) -> list[int]:
    for i in range(1, len(lst)):
        j = i
        while lst[j - 1] > lst[j] and j > 0:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
    return lst

print(insertion_sort([2, 6, 2, 1, 7, 43, 2, 4]))