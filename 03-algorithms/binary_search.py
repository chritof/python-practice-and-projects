from typing import List, Optional

def binary_search(sorted_items: List[int], target: int) -> Optional[int]:
    """Return index of target in sorted_items, or None if not found. O(log n)."""
    left = 0
    right = len(sorted_items) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = sorted_items[mid]

        if guess == target:
            return mid
        if guess < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(nums, 7))   # 3
    print(binary_search(nums, 2))   # None
