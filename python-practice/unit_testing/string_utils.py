def reverse_text(text):
    return text[::-1]


def is_palindrome(text):
    return text.lower() == text[::-1].lower()