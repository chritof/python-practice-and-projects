def is_palindrome(text: str) -> bool:
    """
    Check if text is a palindrome ignoring spaces and casing.
    Uses two pointers. O(n).
    """
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    print(is_palindrome("A man a plan a canal Panama"))  # True
    print(is_palindrome("Hello"))                        # False
