
def is_palindrome(number):
    original_number = str(number)
    reversed_number = original_number[::-1]
    return original_number == reversed_number
