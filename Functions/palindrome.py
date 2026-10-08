def is_palindrome(S):
    S=S.lower().replace(" ","")
    return S==S[::-1]

print(is_palindrome("A man a plan a canal Panama"))