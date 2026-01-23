from typing import List, Optional, Tuple

def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Return indices of two numbers that add up to target.
    Uses hashmap. O(n).
    """
    seen = {}  # value -> index
    for i, value in enumerate(nums):
        needed = target - value
        if needed in seen:
            return (seen[needed], i)
        seen[value] = i
    return None

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # (0, 1)
    print(two_sum([3, 2, 4], 6))        # (1, 2)
