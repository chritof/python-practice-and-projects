from binary_search import binary_search
from linear_search import linear_search
from sorting_bubble import bubble_sort
from sorting_insertion import insertion_sort
from two_pointers_palindrome import is_palindrome
from hashmap_two_sum import two_sum

def run():
    assert linear_search([1, 2, 3], 2) == 1
    assert linear_search([1, 2, 3], 9) is None

    assert binary_search([1, 3, 5, 7], 7) == 3
    assert binary_search([1, 3, 5, 7], 2) is None

    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert insertion_sort([3, 1, 2]) == [1, 2, 3]

    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("abc") is False

    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([1, 2, 3], 7) is None

    print("All quick tests passed ✅")

if __name__ == "__main__":
    run()
