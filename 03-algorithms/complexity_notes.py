"""
Time complexity (big-O) quick notes.

O(1): constant time (e.g., list index access)
O(log n): binary search
O(n): linear scan
O(n log n): efficient sorts (Timsort/merge sort)
O(n^2): bubble/selection/insertion sort (worst-case)
"""

def constant_time_example(arr):
    # O(1)
    return arr[0]

def linear_time_example(arr):
    # O(n)
    total = 0
    for x in arr:
        total += x
    return total

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(constant_time_example(arr))
    print(linear_time_example(arr))
