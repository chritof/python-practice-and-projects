from typing import List

def insertion_sort(nums: List[int]) -> List[int]:
    """Return a new list sorted using insertion sort. O(n^2) worst-case."""
    arr = nums[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    print(insertion_sort([9, 3, 1, 5, 4]))
