from typing import List, Optional, TypeVar

T = TypeVar("T")

def linear_search(items: List[T], target: T) -> Optional[int]:
    """Return index of target in items, or None if not found. O(n)."""
    for i, value in enumerate(items):
        if value == target:
            return i
    return None

if __name__ == "__main__":
    data = ["a", "b", "c", "d"]
    print(linear_search(data, "c"))  # 2
    print(linear_search(data, "x"))  # None
    intData = [1, 2, 3, 20, 3, 19]
    print(linear_search(intData, 19))

