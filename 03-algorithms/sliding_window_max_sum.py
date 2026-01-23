from typing import List

def max_sum_subarray_k(nums: List[int], k: int) -> int:
    """
    Return the maximum sum of any contiguous subarray of length k.
    Sliding window. O(n).
    """
    if k <= 0:
        raise ValueError("k must be > 0")
    if k > len(nums):
        raise ValueError("k must be <= len(nums)")

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum

if __name__ == "__main__":
    print(max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3))  # 9 (5+1+3)
