Python 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:19) [Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def hamming_distance(s1: str, s2: str) -> int:
    """
    Compute the Hamming distance between two strings.
    The Hamming distance is the number of differing characters at the same positions.

    Parameters:
    s1 (str): First string
    s2 (str): Second string

    Returns:
    int: The Hamming distance

    Raises:
    ValueError: If the strings are not the same length
    """
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length to compute Hamming distance")

    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


# Example usage
print(hamming_distance("karolin", "kathrin"))  # Output: 3
print(hamming_distance("1011101", "1001001"))  # Output: 2
