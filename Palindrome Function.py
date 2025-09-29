Python 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:19) [Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def is_palindrome(s):
    """
    Checks if a string is a palindrome.
    
    Args:
        s (str): The string to check.
        
    Returns:
        bool: True if `s` is a palindrome, False otherwise.
    """
    return s == s[::-1]  # Compare string to its reverse


# Test Cases
test_strings = ["", "madam", "racecar", "level", "hello", "abba", "a"]
for string in test_strings:
    print(f"'{string}' is a palindrome: {is_palindrome(string)}")