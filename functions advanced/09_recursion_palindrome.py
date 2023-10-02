# def palindrome(word, index):
#     """
#     no recursion
#     """
#     if word == word[::-1]:
#         return f'{word} is a palindrome'
#     return f'{word} is not a palindrome'

def palindrome(word, index):
    """
    recursion
    """
    if index == len(word) // 2:
        return f'{word} is a palindrome'
    if word[index] != word[-1 - index]:
        return f'{word} is not a palindrome'
    return palindrome(word, index + 1)

print(palindrome("abcba", 0))
print(palindrome("peter", 0))
