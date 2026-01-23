from typing import List

def bubble_sort(nums: List[int]) -> List[int]:
    """Return a new list sorted using bubble sort. O(n^2)."""
    arr = nums[:]  # copy
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    print(bubble_sort([5, 1, 4, 2, 8]))
